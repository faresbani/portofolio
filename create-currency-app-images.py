#!/usr/bin/env python3
"""
Script to create placeholder images for Currency Today app
"""

import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_placeholder_image(width, height, text, filename, bg_color=None, text_color=None):
    """Create a placeholder image with text"""
    
    # Default colors
    if bg_color is None:
        bg_color = (52, 152, 219)  # Blue
    if text_color is None:
        text_color = (255, 255, 255)  # White
    
    # Create image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fallback to default if not available
    try:
        font_size = min(width, height) // 15
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            font_size = min(width, height) // 15
            font = ImageFont.load_default()
        except:
            font = None
    
    # Calculate text position
    if font:
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    else:
        text_width = len(text) * 10
        text_height = 20
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Add some decorative elements for currency app
    # Draw currency symbols
    symbols = ['$', '€', '£', '¥', '₹']
    for i, symbol in enumerate(symbols):
        symbol_x = 20 + (i * 30)
        symbol_y = 20
        draw.text((symbol_x, symbol_y), symbol, fill=text_color, font=font)
    
    # Add border
    draw.rectangle([10, 10, width-10, height-10], outline=text_color, width=3)
    
    # Save image
    img.save(filename, 'JPEG', quality=85)
    print(f"Created: {filename}")

def main():
    """Create all Currency Today app images"""
    
    # Create img directory if it doesn't exist
    os.makedirs('img', exist_ok=True)
    
    # Currency app colors (green theme for money/finance)
    colors_currency = [
        (46, 204, 113),   # Green
        (39, 174, 96),    # Dark Green
        (52, 152, 219),   # Blue
        (155, 89, 182),   # Purple
        (241, 196, 15),   # Gold/Yellow
    ]
    
    # Main project image
    create_placeholder_image(800, 600, "Currency Today\nتطبيق تحويل العملات", "img/project7.jpg", colors_currency[0])
    
    # Currency converter screen
    create_placeholder_image(800, 600, "Currency Today\nشاشة التحويل\n$ → €", "img/project7-converter.jpg", colors_currency[1])
    
    # Exchange rates screen
    create_placeholder_image(800, 600, "Currency Today\nأسعار الصرف\nUSD, EUR, GBP", "img/project7-rates.jpg", colors_currency[2])
    
    # Charts screen
    create_placeholder_image(800, 600, "Currency Today\nالرسوم البيانية\n📈 Historical Data", "img/project7-charts.jpg", colors_currency[3])
    
    # Settings screen
    create_placeholder_image(800, 600, "Currency Today\nالإعدادات\n⚙️ Settings", "img/project7-settings.jpg", colors_currency[4])
    
    print("\n✅ All Currency Today app images created successfully!")
    print("📁 Images saved in the 'img' directory")
    print("💰 Currency app themed images with financial colors")

if __name__ == "__main__":
    main()
