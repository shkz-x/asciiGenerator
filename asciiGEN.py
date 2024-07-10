#!/usr/bin/env python3
# myAsciiGenerator | by shkz

import argparse
from pyfiglet import Figlet

def list_fonts():
    fonts = Figlet().getFonts()
    print("Available fonts:")
    for font in fonts:
        print(f" - {font}")

def genAscii(text, font_name):
    try:
        font = Figlet(font=font_name)
    except Exception as e:
        print(f"Error: {e}")
        return None

    a_line = "\n■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n\n"

    
    ascii_text = font.renderText(text)

    # Return banner
    return f"{a_line}{ascii_text}{a_line}"

def main():
    
    parser = argparse.ArgumentParser(description="Generate ASCII banners.")
    parser = argparse.ArgumentParser(description="Example: python3 asciiGEN.py 'Your_Text' -f epic")
    parser.add_argument('text', type=str, nargs='?', help="Text to convert to ASCII")
    parser.add_argument('-f', '--font', type=str, default='3d', help="Font name (default: 3d)")
    parser.add_argument('-o', '--output', type=str, help="Output file")
    parser.add_argument('-l', '--list-fonts', action='store_true', help="List available fonts")

    args = parser.parse_args()

    if args.list_fonts:
        list_fonts()
    elif args.text:
        
        # Generating the ASCII banner
        banner = genAscii(args.text, args.font)
        if banner:
            print(banner)
            if args.output:
                try:
                    with open(args.output, 'w') as file:
                        file.write(banner)
                    print(f"Banner saved to {args.output}")
                except Exception as e:
                    print(f"Error writing to file: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
