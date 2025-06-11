#!/usr/bin/env python3
"""
Script to ensure visitor counter works on all pages
"""

import os
import re

def check_analytics_script(file_path):
    """Check if analytics script is included in HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return 'analytics.js' in content

def add_analytics_script(file_path):
    """Add analytics script to HTML file if not present"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has analytics script
    if 'analytics.js' in content:
        return False, "Already has analytics script"
    
    # Find the main.js script tag
    main_js_pattern = r'<script src="js/main\.js"></script>'
    
    if re.search(main_js_pattern, content):
        # Add analytics script after main.js
        new_content = re.sub(
            main_js_pattern,
            '<script src="js/main.js"></script>\n    \n    <!-- Analytics JavaScript -->\n    <script src="js/analytics.js"></script>',
            content
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Added analytics script"
    else:
        return False, "Could not find main.js script tag"

def check_visitor_counter_div(file_path):
    """Check if visitor counter div exists in HTML file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return 'visitor-counter' in content

def add_visitor_counter_div(file_path):
    """Add visitor counter div to footer if not present"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has visitor counter
    if 'visitor-counter' in content:
        return False, "Already has visitor counter div"
    
    # Look for footer copyright section
    copyright_pattern = r'<div class="col-md-6">\s*<p class="mb-0">&copy; 2024 فارس\. جميع الحقوق محفوظة\.</p>\s*</div>\s*<div class="col-md-6 text-md-end">'
    
    if re.search(copyright_pattern, content, re.MULTILINE):
        # Replace with 3-column layout including visitor counter
        new_footer = '''<div class="col-md-4">
            <p class="mb-0">&copy; 2024 فارس. جميع الحقوق محفوظة.</p>
          </div>
          <div class="col-md-4 text-center">
            <div id="visitor-counter" class="text-light">
              <!-- Analytics counter will be inserted here -->
            </div>
          </div>
          <div class="col-md-4 text-md-end">'''
        
        new_content = re.sub(
            copyright_pattern,
            new_footer,
            content,
            flags=re.MULTILINE
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Added visitor counter div"
    else:
        return False, "Could not find footer copyright section"

def main():
    """Fix visitor counter on all HTML pages"""
    print("🔧 Fixing Visitor Counter on All Pages")
    print("=" * 50)
    
    # Find all HTML files
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html') and not file.startswith(('analytics-', 'generate-', 'mobile-', 'visitor-', 'favicon-')):
            html_files.append(file)
    
    if not html_files:
        print("❌ No HTML files found")
        return
    
    print(f"📁 Found {len(html_files)} HTML files:")
    for file in html_files:
        print(f"   - {file}")
    
    print(f"\n🔍 Checking analytics script...")
    
    # Check and fix analytics script
    for file in html_files:
        has_script = check_analytics_script(file)
        if has_script:
            print(f"✅ {file}: Analytics script present")
        else:
            success, message = add_analytics_script(file)
            if success:
                print(f"✅ {file}: {message}")
            else:
                print(f"⚠️  {file}: {message}")
    
    print(f"\n🔍 Checking visitor counter div...")
    
    # Check and fix visitor counter div
    for file in html_files:
        has_counter = check_visitor_counter_div(file)
        if has_counter:
            print(f"✅ {file}: Visitor counter div present")
        else:
            success, message = add_visitor_counter_div(file)
            if success:
                print(f"✅ {file}: {message}")
            else:
                print(f"⚠️  {file}: {message}")
    
    print(f"\n🧪 Testing visitor counter...")
    
    # Check if analytics.js file exists
    if os.path.exists('js/analytics.js'):
        print("✅ js/analytics.js file exists")
    else:
        print("❌ js/analytics.js file missing!")
    
    # Check if main.js file exists
    if os.path.exists('js/main.js'):
        print("✅ js/main.js file exists")
    else:
        print("❌ js/main.js file missing!")
    
    print(f"\n🎉 Visitor Counter Fix Complete!")
    print(f"\n📝 Next steps:")
    print(f"1. Open visitor-counter-test.html to test")
    print(f"2. Deploy updated files to Netlify")
    print(f"3. Check visitor counter on live site")
    print(f"4. Visit different pages to see counter update")
    
    print(f"\n💡 Troubleshooting:")
    print(f"- If counter doesn't appear: Check browser console (F12)")
    print(f"- If numbers don't update: Clear browser cache")
    print(f"- If errors occur: Check js/analytics.js is loading")

if __name__ == "__main__":
    main()
