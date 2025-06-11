#!/usr/bin/env python3
"""
Script to add favicon links to all HTML pages
"""

import os
import re

def add_favicon_links(file_path):
    """Add favicon links to an HTML file"""
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon links already exist
    if 'favicon' in content.lower():
        print(f"⚠️  Favicon links already exist in {file_path}")
        return False
    
    # Favicon links HTML
    favicon_links = '''    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="img/favicon.svg">
    <link rel="icon" type="image/x-icon" href="img/favicon.ico">
    <link rel="apple-touch-icon" href="img/apple-touch-icon.svg">
    <link rel="icon" type="image/svg+xml" sizes="16x16" href="img/favicon-16x16.svg">
    <link rel="icon" type="image/svg+xml" sizes="32x32" href="img/favicon-32x32.svg">
    <link rel="icon" type="image/svg+xml" sizes="192x192" href="img/android-chrome-192x192.svg">
    <link rel="icon" type="image/svg+xml" sizes="512x512" href="img/android-chrome-512x512.svg">
    
    <!-- Web App Manifest -->
    <meta name="theme-color" content="#3498db">
    <meta name="msapplication-TileColor" content="#3498db">'''
    
    # Find the closing </head> tag and insert favicon links before it
    if '</head>' in content:
        content = content.replace('</head>', favicon_links + '\n  </head>')
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Added favicon links to {file_path}")
        return True
    else:
        print(f"❌ Could not find </head> tag in {file_path}")
        return False

def create_web_manifest():
    """Create a web app manifest file"""
    manifest = '''{
  "name": "فارس - Portfolio",
  "short_name": "فارس",
  "description": "موقع فارس الشخصي - مطور ومصمم مواقع",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#3498db",
  "orientation": "portrait-primary",
  "icons": [
    {
      "src": "img/android-chrome-192x192.svg",
      "sizes": "192x192",
      "type": "image/svg+xml"
    },
    {
      "src": "img/android-chrome-512x512.svg", 
      "sizes": "512x512",
      "type": "image/svg+xml"
    }
  ]
}'''
    
    with open('manifest.json', 'w', encoding='utf-8') as f:
        f.write(manifest)
    print("✅ Created: manifest.json")

def main():
    """Add favicon links to all HTML files"""
    
    print("🔗 Adding Favicon Links to HTML Files...")
    print("=" * 50)
    
    # Find all HTML files
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html') and not file.startswith(('analytics-', 'generate-')):
            html_files.append(file)
    
    if not html_files:
        print("❌ No HTML files found in current directory")
        return
    
    print(f"📁 Found {len(html_files)} HTML files:")
    for file in html_files:
        print(f"   - {file}")
    
    # Add favicon links to each file
    print(f"\n🚀 Adding favicon links...")
    success_count = 0
    
    for file in html_files:
        if add_favicon_links(file):
            success_count += 1
    
    # Create web manifest
    create_web_manifest()
    
    print(f"\n✅ Successfully added favicon links to {success_count}/{len(html_files)} files")
    
    if success_count > 0:
        print(f"\n🎨 Favicon setup complete!")
        print(f"📝 Next steps:")
        print(f"1. Deploy your updated files to Netlify")
        print(f"2. Clear browser cache (Ctrl+F5 or Cmd+Shift+R)")
        print(f"3. Check your website - you should see the new icon!")
        
        print(f"\n💡 Customization options:")
        print(f"- Edit img/favicon.svg to change the design")
        print(f"- Replace 'ف' with your initial in the SVG files")
        print(f"- Change colors in the SVG gradient")

if __name__ == "__main__":
    main()
