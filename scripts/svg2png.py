#!/usr/bin/env python3
import sys
import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description="Convierte SVG a PNG con tamaño específico.")
    parser.add_argument('input', help='Archivo SVG de entrada')
    parser.add_argument('output', help='Archivo PNG de salida')
    parser.add_argument('--width', type=int, required=True, help='Ancho en píxeles')
    parser.add_argument('--height', type=int, required=True, help='Alto en píxeles')

    # Meson puede pasar argumentos extra, pero los ignoramos si usamos parse_known_args
    args, _ = parser.parse_known_args()

    print(f"[svg2png] Convirtiendo {args.input} → {args.output} ({args.width}x{args.height})")

    try:
        result = subprocess.run([
            'rsvg-convert',
            '-w', str(args.width),
            '-h', str(args.height),
            '-o', args.output,
            args.input
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error de rsvg-convert: {result.stderr}", file=sys.stderr)
            sys.exit(1)

        print(f"[svg2png] Éxito: {args.output}")
    except FileNotFoundError:
        print("Error: 'rsvg-convert' no está instalado o no está en el PATH", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
