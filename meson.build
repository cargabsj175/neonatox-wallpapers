project('neonatox-wallpapers', 'c',
  version: '1.0.0',
  license: 'GPLv3'
)

# Directorio de instalación
wallpaper_dir = join_paths(get_option('prefix'), get_option('datadir'), 'backgrounds', 'neonatox')

# Archivos SVG
svg_paths = [
  'data/neonatox-blue.svg',
  'data/neonatox-gray.svg',
  'data/neonatox-green.svg',
  'data/neonatox-orange.svg',
  'data/neonatox-red.svg',
]

# Resoluciones
resolutions = [
  ['1920', '1080'],
  ['2560', '1440'],
  ['3840', '2160']
]

# Script de conversión
svg2png_script = find_program('scripts/svg2png.py')

# Generar cada PNG y marcarlo para instalación
foreach svg_path : svg_paths
  # Extraer nombre: data/neonatox-blue.svg → neonatox-blue
  parts = svg_path.split('/')
  filename = parts[1]  # "neonatox-blue.svg"
  svg_name = filename.split('.')[0]  # "neonatox-blue"

  foreach res : resolutions
    width = res[0]
    height = res[1]
    output_name = '@0@-@1@x@2@.png'.format(svg_name, width, height)

    custom_target(
      output_name,
      input: svg_path,
      output: output_name,
      command: [
        svg2png_script,
        '@INPUT@',
        '@OUTPUT@',
        '--width', width,
        '--height', height
      ],
      depend_files: svg_path,
      install: true,
      install_dir: wallpaper_dir
    )
  endforeach
endforeach

# Instalar SVGs originales
install_data(svg_paths, install_dir: join_paths(wallpaper_dir, 'svg'))

# ✅ Instalar index.xml como copia directa
configure_file(
  input: 'data/index.xml.in',
  output: 'index.xml',
  install_dir: wallpaper_dir,
  install: true,
  copy: true  # ✅ Indica que es solo una copia
)

# Mensaje final
message('Wallpapers instalados en:\n  ' + wallpaper_dir)
