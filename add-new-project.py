#!/usr/bin/env python3
"""
Script to help add a new project to the portfolio
"""

import json
import os
from datetime import datetime

def analyze_project_directory(project_path):
    """Analyze a project directory and extract information"""
    
    if not os.path.exists(project_path):
        print(f"❌ Project path not found: {project_path}")
        return None
    
    project_info = {
        "files": [],
        "directories": [],
        "readme_content": "",
        "requirements": [],
        "main_files": [],
        "technologies": set()
    }
    
    # Walk through the project directory
    for root, dirs, files in os.walk(project_path):
        # Limit depth to avoid too much recursion
        level = root.replace(project_path, '').count(os.sep)
        if level < 3:
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_path)
                project_info["files"].append(relative_path)
                
                # Check for important files
                if file.lower() in ['readme.md', 'readme.txt', 'readme.rst']:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            project_info["readme_content"] = f.read()
                    except:
                        pass
                
                elif file.lower() in ['requirements.txt', 'requirements.pip']:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            project_info["requirements"] = [line.strip() for line in f.readlines() if line.strip()]
                    except:
                        pass
                
                elif file.endswith('.py') and 'main' in file.lower():
                    project_info["main_files"].append(relative_path)
                
                # Detect technologies based on file extensions
                if file.endswith('.py'):
                    project_info["technologies"].add("Python")
                elif file.endswith('.js'):
                    project_info["technologies"].add("JavaScript")
                elif file.endswith('.html'):
                    project_info["technologies"].add("HTML")
                elif file.endswith('.css'):
                    project_info["technologies"].add("CSS")
                elif file.endswith('.java'):
                    project_info["technologies"].add("Java")
                elif file.endswith('.cpp') or file.endswith('.c'):
                    project_info["technologies"].add("C++")
                elif file.endswith('.cs'):
                    project_info["technologies"].add("C#")
                elif file.endswith('.php'):
                    project_info["technologies"].add("PHP")
                elif file.endswith('.dart'):
                    project_info["technologies"].add("Dart")
                    project_info["technologies"].add("Flutter")
    
    # Detect additional technologies from requirements
    for req in project_info["requirements"]:
        req_lower = req.lower()
        if 'django' in req_lower:
            project_info["technologies"].add("Django")
        elif 'flask' in req_lower:
            project_info["technologies"].add("Flask")
        elif 'fastapi' in req_lower:
            project_info["technologies"].add("FastAPI")
        elif 'streamlit' in req_lower:
            project_info["technologies"].add("Streamlit")
        elif 'pandas' in req_lower:
            project_info["technologies"].add("Pandas")
        elif 'numpy' in req_lower:
            project_info["technologies"].add("NumPy")
        elif 'matplotlib' in req_lower or 'seaborn' in req_lower:
            project_info["technologies"].add("Data Visualization")
        elif 'opencv' in req_lower:
            project_info["technologies"].add("OpenCV")
        elif 'tensorflow' in req_lower or 'keras' in req_lower:
            project_info["technologies"].add("TensorFlow")
        elif 'pytorch' in req_lower:
            project_info["technologies"].add("PyTorch")
        elif 'requests' in req_lower:
            project_info["technologies"].add("Web Scraping")
        elif 'selenium' in req_lower:
            project_info["technologies"].add("Selenium")
        elif 'beautifulsoup' in req_lower:
            project_info["technologies"].add("BeautifulSoup")
    
    project_info["technologies"] = list(project_info["technologies"])
    
    return project_info

def create_project_entry():
    """Interactive function to create a new project entry"""
    
    print("🚀 إضافة مشروع جديد للمحفظة")
    print("=" * 50)
    
    # Get project path
    project_path = input("📁 أدخل مسار المشروع (مثال: E:\\youtube_playlist_downloader): ").strip()
    
    if not project_path:
        print("❌ يجب إدخال مسار المشروع")
        return
    
    # Analyze project
    print(f"\n🔍 تحليل المشروع في: {project_path}")
    project_info = analyze_project_directory(project_path)
    
    if not project_info:
        return
    
    print(f"✅ تم العثور على {len(project_info['files'])} ملف")
    print(f"🔧 التقنيات المكتشفة: {', '.join(project_info['technologies'])}")
    
    # Get project details
    print("\n📝 تفاصيل المشروع:")
    title = input("🏷️  عنوان المشروع (بالعربية): ").strip()
    title_en = input("🏷️  عنوان المشروع (بالإنجليزية): ").strip()
    
    description = input("📄 وصف مختصر للمشروع: ").strip()
    detailed_description = input("📄 وصف مفصل للمشروع: ").strip()
    
    # Category
    print("\n📂 اختر فئة المشروع:")
    print("1. mobile - تطبيقات الجوال")
    print("2. web - مواقع الويب") 
    print("3. data - تحليل البيانات")
    print("4. desktop - تطبيقات سطح المكتب")
    print("5. automation - أتمتة وأدوات")
    
    category_choice = input("اختر رقم الفئة (1-5): ").strip()
    category_map = {
        "1": "mobile",
        "2": "web", 
        "3": "data",
        "4": "desktop",
        "5": "automation"
    }
    category = category_map.get(category_choice, "automation")
    
    # Technologies
    detected_techs = project_info['technologies']
    print(f"\n🔧 التقنيات المكتشفة: {', '.join(detected_techs)}")
    additional_techs = input("أضف تقنيات أخرى (مفصولة بفاصلة): ").strip()
    
    technologies = detected_techs.copy()
    if additional_techs:
        technologies.extend([tech.strip() for tech in additional_techs.split(',')])
    
    # Features
    print("\n✨ أدخل مميزات المشروع (اضغط Enter مرتين للانتهاء):")
    features = []
    while True:
        feature = input("• ").strip()
        if not feature:
            break
        features.append(feature)
    
    # Status
    print("\n📊 حالة المشروع:")
    print("1. completed - مكتمل")
    print("2. in-progress - قيد التطوير")
    print("3. planning - مخطط")
    
    status_choice = input("اختر رقم الحالة (1-3): ").strip()
    status_map = {
        "1": "completed",
        "2": "in-progress",
        "3": "planning"
    }
    status = status_map.get(status_choice, "completed")
    
    # Additional details
    timeline = input("⏱️  المدة الزمنية للمشروع: ").strip()
    team_size = input("👥 حجم الفريق: ").strip()
    year = input("📅 سنة المشروع: ").strip() or str(datetime.now().year)
    
    # Load existing projects
    try:
        with open('data/projects.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        print("❌ خطأ في قراءة ملف المشاريع")
        return
    
    # Get next project ID
    existing_ids = [p['id'] for p in data['projects']]
    next_id = max(existing_ids) + 1 if existing_ids else 1
    
    # Create new project entry
    new_project = {
        "id": next_id,
        "title": title,
        "title_en": title_en,
        "description": description,
        "detailedDescription": detailed_description,
        "image": f"img/project{next_id}.jpg",
        "images": [
            f"img/project{next_id}.jpg",
            f"img/project{next_id}-screen1.jpg",
            f"img/project{next_id}-screen2.jpg",
            f"img/project{next_id}-screen3.jpg",
            f"img/project{next_id}-demo.jpg"
        ],
        "category": category,
        "technologies": technologies,
        "features": features,
        "challenges": [
            "تحدي تقني 1",
            "تحدي تقني 2", 
            "تحدي تقني 3"
        ],
        "solutions": [
            "حل تقني 1",
            "حل تقني 2",
            "حل تقني 3"
        ],
        "timeline": timeline,
        "teamSize": team_size,
        "demoUrl": "#",
        "githubUrl": "#",
        "status": status,
        "year": year,
        "detailUrl": f"project-{next_id}.html"
    }
    
    # Add to projects list
    data['projects'].append(new_project)
    
    # Update categories count
    for cat in data['categories']:
        if cat['id'] == category:
            cat['count'] += 1
        elif cat['id'] == 'all':
            cat['count'] += 1
    
    # Update technologies list
    for tech in technologies:
        if tech not in data['technologies']:
            data['technologies'].append(tech)
    
    # Save updated data
    try:
        with open('data/projects.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ تم إضافة المشروع بنجاح!")
        print(f"🆔 معرف المشروع: {next_id}")
        print(f"📄 عنوان المشروع: {title}")
        print(f"📂 الفئة: {category}")
        print(f"🔧 التقنيات: {', '.join(technologies)}")
        
        print(f"\n📋 الخطوات التالية:")
        print(f"1. إنشاء صورة للمشروع: img/project{next_id}.jpg")
        print(f"2. إنشاء صفحة تفاصيل المشروع: project-{next_id}.html")
        print(f"3. تحديث صفحة المشاريع الرئيسية")
        
    except Exception as e:
        print(f"❌ خطأ في حفظ البيانات: {e}")

def main():
    """Main function"""
    create_project_entry()

if __name__ == "__main__":
    main()
