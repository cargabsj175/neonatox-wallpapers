# NeonatoX Wallpapers

Una colección elegante y moderna de fondos de pantalla en estilo neón con tonos vibrantes: azul, gris, verde, naranja y rojo. Diseñados para lucir bien en cualquier entorno de escritorio: GNOME, XFCE, Sway, Hyprland y más.

> ✅ SVG + PNG generados automáticamente  
> 🛠️ Instalador con Meson  
> 🖼️ Compatible con Wayland y X11  
> 🎨 Ideal para temas oscuros y minimalistas

---

## Previsualización

Las imágenes de previsualización son generadas en 1920x1080.

- **Azul**: Fondo limpio con acentos en azul neón.
- **Gris**: Elegancia neutra con brillos sutiles.
- **Verde**: Energía fresca y moderna.
- **Naranja**: Calidez y contraste alto.
- **Rojo**: Impacto visual y estilo dramático.

> *Nota: Las imágenes no están incluidas en este repositorio, pero se generan durante la instalación.*

---

## Instalación

### Requisitos

- meson y ninja (para construcción)
- rsvg-convert (de librsvg2-bin) para convertir SVG → PNG
- sudo (si instalas en /usr)

En Ubuntu/Debian:
sudo apt install meson ninja-build librsvg2-bin

En Arch Linux:
sudo pacman -S meson ninja librsvg

En Fedora:
sudo dnf install meson ninja-build librsvg2-tools

### Compilar e instalar

# Clonar (opcional)
git clone https://github.com/tu-usuario/neonatox-wallpapers.git
cd neonatox-wallpapers

# Configurar
meson setup builddir --prefix=/usr

# Compilar e instalar (requiere sudo si es global)
ninja -C builddir
sudo ninja -C builddir install

> Usa --prefix=$HOME/.local para instalación local sin sudo.

### Ubicación de los fondos instalados:
/usr/share/backgrounds/neonatox/        # Sistema (requiere sudo)
~/.local/share/backgrounds/neonatox/   # Usuario (sin sudo)

Los fondos estarán disponibles en:
- GNOME: Configuración → Fondos de pantalla
- XFCE: Configuración → Escritorio → Fondo
- Sway/Hyprland: Reinicia o recarga swaybg

---

## Desinstalar

Meson no incluye un comando de desinstalación, pero puedes eliminar manualmente:

sudo rm -rf /usr/share/backgrounds/neonatox/

# O para instalación local:
rm -rf ~/.local/share/backgrounds/neonatox/

---

## Estructura del proyecto

neonatox-wallpapers/
├── data/
│   ├── neonatox-blue.svg
│   ├── neonatox-gray.svg
│   ├── neonatox-green.svg
│   ├── neonatox-orange.svg
│   └── neonatox-red.svg
├── scripts/
│   └── svg2png.py           # Script de conversión SVG → PNG
├── meson.build              # Sistema de construcción con Meson
└── README.md                # Este archivo

---

## Cómo personalizar

1. Edita cualquiera de los archivos SVG en la carpeta `data/` con Inkscape, GIMP o cualquier editor vectorial.
2. Vuelve a ejecutar `ninja -C builddir` para regenerar los PNG.
3. Instala de nuevo con `sudo ninja -C builddir install`.

---

## Licencia

Este proyecto está licenciado bajo la **Licencia Pública General de GNU (GPL) versión 3**.

Puedes ver la licencia completa en: https://www.gnu.org/licenses/gpl-3.0.html

---

## Notas

- Los fondos en formato PNG se generan automáticamente durante la compilación.
- Compatible con entornos Wayland (Sway, Hyprland) y X11.
- Incluye archivo `index.xml` para que los fondos aparezcan correctamente en GNOME y XFCE.

Hecho con cuidado para usuarios de Linux que aman el estilo limpio y moderno.
