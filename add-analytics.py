#!/usr/bin/env python3
"""
Script to automatically add Google Analytics to all HTML pages
"""

import os
import re

def add_analytics_to_file(file_path, measurement_id):
    """Add Google Analytics code to an HTML file"""
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if analytics is already added
    if 'gtag' in content or 'google-analytics' in content:
        print(f"⚠️  Analytics already exists in {file_path}")
        return False
    
    # Google Analytics code
    analytics_code = f'''    
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={measurement_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{measurement_id}');
    </script>'''
    
    # Find the closing </head> tag and insert analytics code before it
    if '</head>' in content:
        content = content.replace('</head>', analytics_code + '\n  </head>')
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Added analytics to {file_path}")
        return True
    else:
        print(f"❌ Could not find </head> tag in {file_path}")
        return False

def main():
    """Add Google Analytics to all HTML files"""
    
    print("🔍 Google Analytics Setup Script")
    print("=" * 50)
    
    # Use the provided measurement ID
    measurement_id = "G-X037GY8YZP"

    print(f"📊 Using Google Analytics ID: {measurement_id}")

    confirm = input("Add Google Analytics to all HTML pages? (y/n): ").lower()
    if confirm != 'y':
        print("❌ Operation cancelled")
        return
    
    # Find all HTML files
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html') and not file.startswith('analytics-setup'):
            html_files.append(file)
    
    if not html_files:
        print("❌ No HTML files found in current directory")
        return
    
    print(f"\n📁 Found {len(html_files)} HTML files:")
    for file in html_files:
        print(f"   - {file}")
    
    confirm = input(f"\nAdd Google Analytics to all these files? (y/n): ").lower()
    if confirm != 'y':
        print("❌ Operation cancelled")
        return
    
    # Add analytics to each file
    print(f"\n🚀 Adding Google Analytics...")
    success_count = 0
    
    for file in html_files:
        if add_analytics_to_file(file, measurement_id):
            success_count += 1
    
    print(f"\n✅ Successfully added analytics to {success_count}/{len(html_files)} files")
    
    if success_count > 0:
        print(f"\n📊 Next steps:")
        print(f"1. Deploy your updated files to Netlify/GitHub")
        print(f"2. Visit your website to test tracking")
        print(f"3. Check Google Analytics in 24-48 hours for data")
        print(f"4. View real-time data immediately in GA dashboard")
    
    print(f"\n🔗 Your Google Analytics dashboard:")
    print(f"   https://analytics.google.com")

if __name__ == "__main__":
    main()
