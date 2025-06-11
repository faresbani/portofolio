#!/usr/bin/env python3
"""
Simple script to create remaining placeholder images as SVG files
"""

import os

def create_svg_placeholder(width, height, text, color, filename):
    """Create an SVG placeholder image"""
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="{color}"/>
  <rect x="{width//8}" y="{height//4}" width="{width*3//4}" height="{height//2}" rx="10" fill="white" opacity="0.2"/>
  <text x="{width//2}" y="{height//2}" font-family="Arial, sans-serif" font-size="16" font-weight="bold" 
        fill="white" text-anchor="middle">{text}</text>
  <text x="{width//2}" y="{height//2 + 20}" font-family="Arial, sans-serif" font-size="12" 
        fill="rgba(255,255,255,0.8)" text-anchor="middle">{width}×{height}</text>
</svg>'''
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Created: {filename}")

def main():
    """Create all remaining placeholder images"""
    
    # Ensure img directory exists
    os.makedirs('img', exist_ok=True)
    
    # Define remaining images to create
    images = [
        # Personal images
        (300, 300, "صورة شخصية", "#2ecc71", "img/about-photo.jpg"),
        
        # Remaining project images
        (400, 250, "تطبيق الطقس", "#34495e", "img/project4.jpg"),
        (400, 250, "نظام المكتبة", "#8e44ad", "img/project5.jpg"),
        (400, 250, "لوحة التحكم", "#27ae60", "img/project6.jpg"),
        
        # Course images
        (400, 250, "دورة Python", "#3776ab", "img/course-python.jpg"),
        (400, 250, "دورة Flutter", "#02569b", "img/course-flutter.jpg"),
        (400, 250, "تطوير المواقع", "#e34c26", "img/course-web.jpg"),
        (400, 250, "دورة Django", "#092e20", "img/course-django.jpg"),
        (400, 250, "تصميم UI/UX", "#ff6b6b", "img/course-ui.jpg"),
        (400, 250, "دورة Bootstrap", "#7952b3", "img/course-bootstrap.jpg"),
        
        # Article images
        (600, 300, "مقال مميز", "#fd79a8", "img/article-featured.jpg"),
        (400, 250, "Flutter Tips", "#00b894", "img/article1.jpg"),
        (400, 250, "Python Guide", "#0984e3", "img/article2.jpg"),
        (400, 250, "CSS Grid", "#a29bfe", "img/article3.jpg"),
        (400, 250, "Dev Tips", "#ffeaa7", "img/article4.jpg"),
        (400, 250, "Django vs Flask", "#fab1a0", "img/article5.jpg"),
        (400, 250, "State Management", "#ff7675", "img/article6.jpg"),
        
        # Student images (circular)
        (100, 100, "أحمد", "#6c5ce7", "img/student1.jpg"),
        (100, 100, "فاطمة", "#fd79a8", "img/student2.jpg"),
        (100, 100, "محمد", "#fdcb6e", "img/student3.jpg"),
    ]
    
    # Create all images
    for width, height, text, color, filename in images:
        if not os.path.exists(filename):
            create_svg_placeholder(width, height, text, color, filename)
        else:
            print(f"Skipped: {filename} (already exists)")
    
    print(f"\n✅ Created placeholder images in 'img/' directory")
    print("🚀 Your website is now ready for deployment!")

if __name__ == "__main__":
    main()
