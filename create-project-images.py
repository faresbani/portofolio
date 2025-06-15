#!/usr/bin/env python3
"""
Script to create placeholder images for project detail pages
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
    
    # Add some decorative elements
    draw.rectangle([10, 10, width-10, height-10], outline=text_color, width=3)
    
    # Save image
    img.save(filename, 'JPEG', quality=85)
    print(f"Created: {filename}")

def main():
    """Create all project placeholder images"""
    
    # Create img directory if it doesn't exist
    os.makedirs('img', exist_ok=True)
    
    # Project 1 - Task Management App (Flutter)
    colors_mobile = [
        (52, 152, 219),   # Blue
        (155, 89, 182),   # Purple
        (46, 204, 113),   # Green
        (241, 196, 15),   # Yellow
    ]
    
    create_placeholder_image(800, 600, "تطبيق إدارة المهام\nالشاشة الرئيسية", "img/project1-screen1.jpg", colors_mobile[0])
    create_placeholder_image(800, 600, "تطبيق إدارة المهام\nشاشة الإحصائيات", "img/project1-screen2.jpg", colors_mobile[1])
    create_placeholder_image(800, 600, "تطبيق إدارة المهام\nشاشة الإعدادات", "img/project1-screen3.jpg", colors_mobile[2])
    create_placeholder_image(800, 600, "تطبيق إدارة المهام\nمعمارية التطبيق", "img/project1-architecture.jpg", colors_mobile[3])
    
    # Project 2 - E-commerce Website (Django)
    colors_web = [
        (231, 76, 60),    # Red
        (230, 126, 34),   # Orange
        (39, 174, 96),    # Green
        (142, 68, 173),   # Purple
    ]
    
    create_placeholder_image(1200, 800, "موقع التجارة الإلكترونية\nالصفحة الرئيسية", "img/project2-homepage.jpg", colors_web[0])
    create_placeholder_image(1200, 800, "موقع التجارة الإلكترونية\nصفحة المنتجات", "img/project2-products.jpg", colors_web[1])
    create_placeholder_image(1200, 800, "موقع التجارة الإلكترونية\nلوحة الإدارة", "img/project2-admin.jpg", colors_web[2])
    create_placeholder_image(1200, 800, "موقع التجارة الإلكترونية\nصفحة الدفع", "img/project2-checkout.jpg", colors_web[3])
    
    # Project 3 - Data Analysis Tool (Python)
    colors_data = [
        (52, 73, 94),     # Dark Blue
        (44, 62, 80),     # Darker Blue
        (127, 140, 141),  # Gray
        (149, 165, 166),  # Light Gray
    ]
    
    create_placeholder_image(1200, 800, "أداة تحليل البيانات\nلوحة التحكم", "img/project3-dashboard.jpg", colors_data[0])
    create_placeholder_image(1200, 800, "أداة تحليل البيانات\nالرسوم البيانية", "img/project3-charts.jpg", colors_data[1])
    create_placeholder_image(1200, 800, "أداة تحليل البيانات\nاستيراد البيانات", "img/project3-import.jpg", colors_data[2])
    create_placeholder_image(1200, 800, "أداة تحليل البيانات\nالتقارير", "img/project3-reports.jpg", colors_data[3])
    
    # Project 4 - Weather App (Flutter)
    colors_weather = [
        (52, 152, 219),   # Sky Blue
        (46, 204, 113),   # Green
        (241, 196, 15),   # Sun Yellow
        (155, 89, 182),   # Purple
    ]
    
    create_placeholder_image(800, 600, "تطبيق الطقس\nالشاشة الرئيسية", "img/project4-main.jpg", colors_weather[0])
    create_placeholder_image(800, 600, "تطبيق الطقس\nالتنبؤات", "img/project4-forecast.jpg", colors_weather[1])
    create_placeholder_image(800, 600, "تطبيق الطقس\nالمدن المحفوظة", "img/project4-cities.jpg", colors_weather[2])
    create_placeholder_image(800, 600, "تطبيق الطقس\nالإعدادات", "img/project4-settings.jpg", colors_weather[3])
    
    # Project 5 - Library Management (Flask)
    colors_library = [
        (39, 174, 96),    # Green
        (41, 128, 185),   # Blue
        (142, 68, 173),   # Purple
        (230, 126, 34),   # Orange
    ]
    
    create_placeholder_image(1200, 800, "نظام إدارة المكتبة\nفهرس الكتب", "img/project5-catalog.jpg", colors_library[0])
    create_placeholder_image(1200, 800, "نظام إدارة المكتبة\nالاستعارة والإرجاع", "img/project5-borrowing.jpg", colors_library[1])
    create_placeholder_image(1200, 800, "نظام إدارة المكتبة\nإدارة الأعضاء", "img/project5-members.jpg", colors_library[2])
    create_placeholder_image(1200, 800, "نظام إدارة المكتبة\nالتقارير", "img/project5-reports.jpg", colors_library[3])
    
    # Project 6 - Analytics Dashboard (React)
    colors_analytics = [
        (52, 73, 94),     # Dark Blue
        (231, 76, 60),    # Red
        (46, 204, 113),   # Green
        (241, 196, 15),   # Yellow
    ]
    
    create_placeholder_image(1200, 800, "لوحة التحكم التحليلية\nنظرة عامة", "img/project6-overview.jpg", colors_analytics[0])
    create_placeholder_image(1200, 800, "لوحة التحكم التحليلية\nالرسوم البيانية", "img/project6-charts.jpg", colors_analytics[1])
    create_placeholder_image(1200, 800, "لوحة التحكم التحليلية\nالوقت الفعلي", "img/project6-realtime.jpg", colors_analytics[2])
    create_placeholder_image(1200, 800, "لوحة التحكم التحليلية\nالعرض المحمول", "img/project6-mobile.jpg", colors_analytics[3])
    
    print("\n✅ All project images created successfully!")
    print("📁 Images saved in the 'img' directory")
    print("🎨 Each project has 4 additional screenshot images")

if __name__ == "__main__":
    main()
