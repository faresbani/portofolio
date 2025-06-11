#!/usr/bin/env python3
"""
Script to create favicon files in multiple formats
"""

import os

def create_favicon_svg(size, filename):
    """Create SVG favicon with specified size"""
    svg_content = f'''<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#3498db;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2980b9;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background circle -->
  <circle cx="{size//2}" cy="{size//2}" r="{size//2-1}" fill="url(#grad)" stroke="#2c3e50" stroke-width="1"/>
  
  <!-- Letter F in Arabic -->
  <text x="{size//2}" y="{size//2 + size//4}" font-family="Arial, sans-serif" font-size="{size//2}" font-weight="bold" 
        fill="white" text-anchor="middle">ف</text>
</svg>'''
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"✅ Created: {filename}")

def create_simple_ico_svg():
    """Create a simple SVG that works as ICO replacement"""
    svg_content = '''<svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
  <rect width="16" height="16" fill="#3498db" rx="2"/>
  <text x="8" y="12" font-family="Arial" font-size="10" font-weight="bold" 
        fill="white" text-anchor="middle">ف</text>
</svg>'''
    
    with open('img/favicon.ico', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("✅ Created: img/favicon.ico (SVG format)")

def create_apple_touch_icon():
    """Create Apple touch icon"""
    svg_content = '''<svg width="180" height="180" viewBox="0 0 180 180" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#3498db;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2980b9;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background with rounded corners for iOS -->
  <rect width="180" height="180" fill="url(#grad)" rx="20"/>
  
  <!-- Letter F in Arabic -->
  <text x="90" y="120" font-family="Arial, sans-serif" font-size="80" font-weight="bold" 
        fill="white" text-anchor="middle">ف</text>
</svg>'''
    
    with open('img/apple-touch-icon.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("✅ Created: img/apple-touch-icon.svg")

def main():
    """Create all favicon files"""
    print("🎨 Creating Favicon Files...")
    print("=" * 40)
    
    # Ensure img directory exists
    os.makedirs('img', exist_ok=True)
    
    # Create different sizes
    create_favicon_svg(16, 'img/favicon-16x16.svg')
    create_favicon_svg(32, 'img/favicon-32x32.svg')
    create_favicon_svg(192, 'img/android-chrome-192x192.svg')
    create_favicon_svg(512, 'img/android-chrome-512x512.svg')
    
    # Create ICO replacement
    create_simple_ico_svg()
    
    # Create Apple touch icon
    create_apple_touch_icon()
    
    print("\n🎉 All favicon files created!")
    print("\nFiles created:")
    print("- img/favicon.ico (main favicon)")
    print("- img/favicon-16x16.svg")
    print("- img/favicon-32x32.svg") 
    print("- img/apple-touch-icon.svg")
    print("- img/android-chrome-192x192.svg")
    print("- img/android-chrome-512x512.svg")
    
    print("\n📝 Next steps:")
    print("1. Run 'python update-favicon-links.py' to update HTML files")
    print("2. Deploy to Netlify")
    print("3. Clear browser cache to see new icon")

if __name__ == "__main__":
    main()
