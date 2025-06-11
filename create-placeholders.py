#!/usr/bin/env python3
"""
Script to create placeholder images for the portfolio website
This script creates simple colored placeholder images with text
"""

import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_placeholder_image(width, height, text, filename, bg_color=None):
    """Create a placeholder image with text"""
    
    # Random background color if not specified
    if bg_color is None:
        colors = [
            (52, 152, 219),   # Blue
            (46, 204, 113),   # Green
            (155, 89, 182),   # Purple
            (241, 196, 15),   # Yellow
            (230, 126, 34),   # Orange
            (231, 76, 60),    # Red
            (52, 73, 94),     # Dark Blue
            (149, 165, 166),  # Gray
        ]
        bg_color = random.choice(colors)
    
    # Create image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fallback to default if not available
    try:
        font_size = min(width, height) // 10
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            font_size = min(width, height) // 10
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
    text_color = (255, 255, 255)  # White text
    if font:
        draw.text((x, y), text, fill=text_color, font=font)
    else:
        draw.text((x, y), text, fill=text_color)
    
    # Save image
    img.save(filename)
    print(f"Created: {filename}")

def main():
    """Create all placeholder images for the portfolio"""
    
    # Create img directory if it doesn't exist
    os.makedirs('img', exist_ok=True)
    
    # Define images to create
    images = [
        # Hero and about images
        (800, 600, "Hero Avatar", "img/hero-avatar.jpg"),
        (400, 400, "About Photo", "img/about-photo.jpg"),
        (600, 400, "About Illustration", "img/about-illustration.jpg"),
        
        # Project images
        (400, 250, "Task Manager App", "img/project1.jpg"),
        (400, 250, "E-commerce Site", "img/project2.jpg"),
        (400, 250, "Data Analysis Tool", "img/project3.jpg"),
        (400, 250, "Weather App", "img/project4.jpg"),
        (400, 250, "Library System", "img/project5.jpg"),
        (400, 250, "Analytics Dashboard", "img/project6.jpg"),
        
        # Course images
        (400, 250, "Python Course", "img/course-python.jpg"),
        (400, 250, "Flutter Course", "img/course-flutter.jpg"),
        (400, 250, "Web Development", "img/course-web.jpg"),
        (400, 250, "Django Course", "img/course-django.jpg"),
        (400, 250, "UI/UX Design", "img/course-ui.jpg"),
        (400, 250, "Bootstrap Course", "img/course-bootstrap.jpg"),
        
        # Article images
        (600, 300, "Featured Article", "img/article-featured.jpg"),
        (400, 250, "Flutter Best Practices", "img/article1.jpg"),
        (400, 250, "Python for Beginners", "img/article2.jpg"),
        (400, 250, "CSS Grid Layout", "img/article3.jpg"),
        (400, 250, "Developer Tips", "img/article4.jpg"),
        (400, 250, "Django vs Flask", "img/article5.jpg"),
        (400, 250, "State Management", "img/article6.jpg"),
        
        # Student testimonial images
        (100, 100, "أحمد", "img/student1.jpg"),
        (100, 100, "فاطمة", "img/student2.jpg"),
        (100, 100, "محمد", "img/student3.jpg"),
    ]
    
    # Create all images
    for width, height, text, filename in images:
        if not os.path.exists(filename):
            create_placeholder_image(width, height, text, filename)
        else:
            print(f"Skipped: {filename} (already exists)")
    
    print(f"\nCreated placeholder images in 'img/' directory")
    print("You can replace these with your actual images later.")

if __name__ == "__main__":
    main()
