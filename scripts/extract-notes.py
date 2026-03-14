#!/usr/bin/env python3
"""Extract slide notes and click structure from slides.md.

Usage:
    python3 scripts/extract-notes.py [slides.md]

Output: JSON array, one entry per slide, with:
  - page: "S01", "S02", ...
  - lines: "25-77"
  - layout: e.g. "default", "center", "two-cols-header"
  - title: slide title text
  - clicks_declared: number from frontmatter `clicks:` (null if absent)
  - click_elements: list of click triggers found in the slide body
      each entry: {"type": "v-click"|"v-clicks"|"v-click-range"|"$clicks", "line": N, "detail": "..."}
  - notes: the raw speaker notes text (content inside <!-- ... -->)
  - notes_lines: "70-76" (line range of the notes block)
"""

import re
import sys
import json


def parse_slides(path="slides.md"):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Split into slides by --- separator
    slides = []
    current_start = None
    in_frontmatter = False
    frontmatter_lines = []
    body_lines = []
    slide_num = 0

    # First pass: find slide boundaries (lines starting with ---)
    boundaries = []
    i = 0
    # Skip global frontmatter
    if lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1  # skip closing ---

    # Find slide separators
    while i < len(lines):
        if lines[i].strip() == "---":
            boundaries.append(i)
        i += 1

    # Parse each slide
    for idx in range(0, len(boundaries) - 1, 2):
        fm_start = boundaries[idx]
        fm_end = boundaries[idx + 1]

        # Body starts after frontmatter closing ---
        body_start = fm_end + 1

        # Body ends at next slide's --- or EOF
        if idx + 2 < len(boundaries):
            body_end = boundaries[idx + 2]
        else:
            body_end = len(lines)

        slide_num += 1

        # Parse frontmatter
        fm_text = "".join(lines[fm_start + 1 : fm_end])
        layout_match = re.search(r"^layout:\s*(.+)", fm_text, re.MULTILINE)
        clicks_match = re.search(r"^clicks:\s*(\d+)", fm_text, re.MULTILINE)

        layout = layout_match.group(1).strip() if layout_match else "-"
        clicks_declared = int(clicks_match.group(1)) if clicks_match else None

        # Parse body
        body = lines[body_start:body_end]
        body_text = "".join(body)

        # Extract title
        title = ""
        for line in body:
            m = re.match(r"^#\s+(.+)", line)
            if m:
                # Strip HTML tags for cleaner title
                title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
                break

        # Extract click elements
        click_elements = []
        for j, line in enumerate(body):
            lineno = body_start + j + 1  # 1-indexed

            # v-click attribute
            for m in re.finditer(r'v-click(?:="([^"]*)")?', line):
                detail = m.group(1) or ""
                click_elements.append(
                    {"type": "v-click", "line": lineno, "detail": detail}
                )

            # v-clicks component
            if "<v-clicks" in line:
                click_elements.append(
                    {"type": "v-clicks", "line": lineno, "detail": ""}
                )

            # $clicks variable
            for m in re.finditer(r"\$clicks\s*>=\s*(\d+)", line):
                click_elements.append(
                    {
                        "type": "$clicks",
                        "line": lineno,
                        "detail": f">= {m.group(1)}",
                    }
                )

        # Extract notes (last <!-- ... --> block in the slide)
        notes = ""
        notes_lines = ""
        # Search backwards for the last comment block
        comment_blocks = list(
            re.finditer(r"<!--\s*\n(.*?)-->", body_text, re.DOTALL)
        )
        if comment_blocks:
            last_comment = comment_blocks[-1]
            notes = last_comment.group(1).strip()
            # Calculate line numbers
            pre_text = body_text[: last_comment.start()]
            note_start_line = body_start + pre_text.count("\n") + 1
            note_end_line = (
                note_start_line + last_comment.group(0).count("\n")
            )
            notes_lines = f"{note_start_line}-{note_end_line}"

        slides.append(
            {
                "page": f"S{slide_num:02d}",
                "lines": f"{fm_start + 1}-{body_end}",
                "layout": layout,
                "title": title,
                "clicks_declared": clicks_declared,
                "click_count": len(click_elements),
                "click_elements": click_elements,
                "notes": notes,
                "notes_lines": notes_lines,
            }
        )

    return slides


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "slides.md"
    slides = parse_slides(path)
    print(json.dumps(slides, ensure_ascii=False, indent=2))
