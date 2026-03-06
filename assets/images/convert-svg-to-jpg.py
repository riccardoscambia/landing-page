#!/usr/bin/env python3
"""
Convert SVG files to JPG format for Open Graph images
Requires: pip install cairosvg pillow (or use built-in macOS conversion)
"""

import subprocess
import os
from pathlib import Path

def convert_svg_to_jpg_macos(svg_path, jpg_path, width=1200, height=630):
    """Convert SVG to JPG using macOS qlmanage and sips"""
    try:
        # Convert SVG to PNG first using qlmanage
        png_path = svg_path.replace('.svg', '_temp.png')
        
        # Use qlmanage to generate thumbnail
        cmd = [
            'qlmanage',
            '-t',
            '-s', str(max(width, height)),
            '-o', str(Path(svg_path).parent),
            svg_path
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        
        # Rename the generated file
        temp_output = svg_path.replace('.svg', '.svg.png')
        if os.path.exists(temp_output):
            os.rename(temp_output, png_path)
        
        # Convert PNG to JPG with sips
        cmd_jpg = [
            'sips',
            '-s', 'format', 'jpeg',
            '-s', 'formatOptions', 'high',
            '-z', str(height), str(width),
            png_path,
            '--out', jpg_path
        ]
        subprocess.run(cmd_jpg, capture_output=True, check=True)
        
        # Cleanup temp PNG
        if os.path.exists(png_path):
            os.remove(png_path)
            
        print(f"✓ Converted: {Path(svg_path).name} → {Path(jpg_path).name}")
        return True
        
    except Exception as e:
        print(f"✗ Error converting {svg_path}: {e}")
        return False

def main():
    # List of SVG files to convert
    svg_files = [
        'og-image.svg',
        'og-image-biography.svg',
        'og-image-american-idol.svg',
        'og-image-vocal-style.svg',
        'og-image-news.svg'
    ]
    
    script_dir = Path(__file__).parent
    success_count = 0
    
    print("Converting SVG files to JPG (1200x630px)...\n")
    
    for svg_file in svg_files:
        svg_path = script_dir / svg_file
        jpg_path = script_dir / svg_file.replace('.svg', '.jpg')
        
        if svg_path.exists():
            if convert_svg_to_jpg_macos(str(svg_path), str(jpg_path)):
                success_count += 1
        else:
            print(f"✗ File not found: {svg_file}")
    
    print(f"\n{success_count}/{len(svg_files)} files converted successfully!")
    
    if success_count == len(svg_files):
        print("\n✓ All OG images ready for use!")
        print("  Test with: https://developers.facebook.com/tools/debug/")

if __name__ == '__main__':
    main()
