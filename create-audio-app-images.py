#!/usr/bin/env python3
"""
Script to create placeholder images for Audio Splitter and Repeater app
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
    
    # Add audio-related decorative elements
    # Draw audio wave pattern
    wave_y = height - 60
    for i in range(0, width, 20):
        wave_height = random.randint(10, 40)
        draw.rectangle([i, wave_y - wave_height, i + 10, wave_y], fill=text_color)
    
    # Draw play button symbol
    play_x = 30
    play_y = 30
    play_points = [
        (play_x, play_y),
        (play_x + 30, play_y + 15),
        (play_x, play_y + 30)
    ]
    draw.polygon(play_points, fill=text_color)
    
    # Add border
    draw.rectangle([10, 10, width-10, height-10], outline=text_color, width=3)
    
    # Save image
    img.save(filename, 'JPEG', quality=85)
    print(f"Created: {filename}")

def main():
    """Create all Audio Splitter and Repeater app images"""
    
    # Create img directory if it doesn't exist
    os.makedirs('img', exist_ok=True)
    
    # Audio app colors (purple/blue theme for audio/media)
    colors_audio = [
        (142, 68, 173),   # Purple
        (155, 89, 182),   # Light Purple
        (52, 152, 219),   # Blue
        (41, 128, 185),   # Dark Blue
        (46, 204, 113),   # Green
    ]
    
    # Main project image
    create_placeholder_image(1200, 800, "مقسم ومكرر الصوت\nAudio Splitter & Repeater", "img/project8.jpg", colors_audio[0])
    
    # Interface screen
    create_placeholder_image(1200, 800, "مقسم ومكرر الصوت\nالواجهة الرئيسية\n🎵 Main Interface", "img/project8-interface.jpg", colors_audio[1])
    
    # Waveform visualization
    create_placeholder_image(1200, 800, "مقسم ومكرر الصوت\nعرض الموجة الصوتية\n📊 Waveform View", "img/project8-waveform.jpg", colors_audio[2])
    
    # Settings screen
    create_placeholder_image(1200, 800, "مقسم ومكرر الصوت\nالإعدادات\n⚙️ Settings", "img/project8-settings.jpg", colors_audio[3])
    
    # Study history screen
    create_placeholder_image(1200, 800, "مقسم ومكرر الصوت\nتاريخ الدراسة\n📈 Study History", "img/project8-history.jpg", colors_audio[4])
    
    print("\n✅ All Audio Splitter and Repeater app images created successfully!")
    print("📁 Images saved in the 'img' directory")
    print("🎵 Audio processing app themed images with media colors")

if __name__ == "__main__":
    main()
