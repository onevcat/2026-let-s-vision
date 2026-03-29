import fs from 'node:fs'
import path from 'node:path'
import { createRequire } from 'node:module'

const require = createRequire(import.meta.url)

function patchFile(filePath, replacements) {
  if (!fs.existsSync(filePath)) {
    console.warn(`[patch-font-cdn] Skip missing file: ${filePath}`)
    return
  }

  let content = fs.readFileSync(filePath, 'utf8')
  let changed = false

  for (const [from, to] of replacements) {
    if (content.includes(from)) {
      content = content.replaceAll(from, to)
      changed = true
    }
  }

  if (changed) {
    fs.writeFileSync(filePath, content, 'utf8')
    console.log(`[patch-font-cdn] Patched: ${filePath}`)
  }
  else {
    console.log(`[patch-font-cdn] No changes needed: ${filePath}`)
  }
}

function run() {
  const penguinRoot = path.dirname(require.resolve('slidev-theme-penguin/package.json'))
  const penguinUnoConfig = path.join(penguinRoot, 'uno.config.ts')
  const asUiPkg = require.resolve('@alvarosabu/ui/package.json', { paths: [penguinRoot] })
  const asUiStyle = path.join(path.dirname(asUiPkg), 'dist/style.css')

  patchFile(penguinUnoConfig, [
    [
      'presetWebFonts(fonts) as unknown as Preset,',
      `presetWebFonts({
      ...fonts,
      provider: 'none',
    }) as unknown as Preset,`,
    ],
  ])

  patchFile(asUiStyle, [
    ['https://fonts.gstatic.com', 'https://gstatic.loli.net'],
    ['https://fonts.googleapis.com', 'https://fonts.loli.net'],
  ])
}

run()
