#!/usr/bin/env python3
"""
Script to create the remaining project detail pages (3, 4, 5, 6)
"""

import json
import os

def load_project_data():
    """Load project data from JSON file"""
    with open('data/projects.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_project_page(project, project_data):
    """Create a project detail page"""
    
    # Get project info
    project_id = project['id']
    title = project['title']
    description = project['description']
    detailed_description = project['detailedDescription']
    category = project['category']
    technologies = project['technologies']
    features = project['features']
    challenges = project['challenges']
    solutions = project['solutions']
    timeline = project['timeline']
    team_size = project['teamSize']
    year = project['year']
    status = project['status']
    images = project['images']
    
    # Determine category display and badges
    category_map = {
        'mobile': ('تطبيقات الجوال', 'Mobile'),
        'web': ('مواقع الويب', 'Web'),
        'data': ('تحليل البيانات', 'Data')
    }
    
    category_display, category_badge = category_map.get(category, ('أخرى', 'Other'))
    
    # Determine status badge
    status_map = {
        'completed': ('مكتمل', 'bg-success'),
        'in-progress': ('قيد التطوير', 'bg-warning'),
        'planning': ('مخطط', 'bg-secondary')
    }
    
    status_display, status_class = status_map.get(status, ('غير محدد', 'bg-secondary'))
    
    # Get main technology for badge color
    tech_colors = {
        'Flutter': 'bg-primary',
        'Python': 'bg-warning',
        'Django': 'bg-success',
        'Flask': 'bg-success',
        'React': 'bg-danger',
        'JavaScript': 'bg-warning'
    }
    
    main_tech = technologies[0] if technologies else 'Unknown'
    tech_color = tech_colors.get(main_tech, 'bg-secondary')
    
    # Generate navigation links
    prev_project = project_id - 1 if project_id > 1 else 6
    next_project = project_id + 1 if project_id < 6 else 1
    
    # Generate related projects (exclude current project)
    all_projects = project_data['projects']
    related_projects = [p for p in all_projects if p['id'] != project_id][:3]
    
    # Create HTML content
    html_content = f'''<!doctype html>
<html lang="ar" dir="rtl">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>فارس | {title}</title>
    <meta name="description" content="{description}">

    <!-- Bootstrap RTL CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.rtl.min.css" integrity="sha384-PRrgQVJ8NNHGieOA1grGdCTIt4h21CzJs6SnWH4YMQ6G5F5+IEzOHz67L4SQaF0o" crossorigin="anonymous">

    <!-- Bootstrap Icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="css/custom.css">
      
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-X037GY8YZP"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-X037GY8YZP');
    </script>
      <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="img/favicon.svg">
    <link rel="icon" type="image/x-icon" href="img/favicon.ico">
    <link rel="apple-touch-icon" href="img/apple-touch-icon.svg">
    <link rel="icon" type="image/svg+xml" sizes="16x16" href="img/favicon-16x16.svg">
    <link rel="icon" type="image/svg+xml" sizes="32x32" href="img/favicon-32x32.svg">
    <link rel="icon" type="image/svg+xml" sizes="192x192" href="img/android-chrome-192x192.svg">
    <link rel="icon" type="image/svg+xml" sizes="512x512" href="img/android-chrome-512x512.svg">
    
    <!-- Web App Manifest -->
    <meta name="theme-color" content="#3498db">
    <meta name="msapplication-TileColor" content="#3498db">
  </head>
  <body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top">
      <div class="container">
        <a class="navbar-brand" href="index.html">
          <i class="bi bi-code-slash me-2"></i>فارس
        </a>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <a class="nav-link" href="index.html">الرئيسية</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="about.html">نبذة عني</a>
            </li>
            <li class="nav-item">
              <a class="nav-link active" href="projects.html">المشاريع</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="courses.html">الدورات</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="articles.html">المقالات</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="contact.html">تواصل معي</a>
            </li>
          </ul>

          <button class="btn btn-outline-secondary btn-sm me-2" id="themeToggle" title="تبديل المظهر">
            <i class="bi bi-moon"></i>
          </button>
        </div>
      </div>
    </nav>

    <!-- Breadcrumb -->
    <section class="section" style="padding-top: 100px; padding-bottom: 20px;">
      <div class="container">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="index.html">الرئيسية</a></li>
            <li class="breadcrumb-item"><a href="projects.html">المشاريع</a></li>
            <li class="breadcrumb-item active" aria-current="page">{title}</li>
          </ol>
        </nav>
      </div>
    </section>

    <!-- Project Header -->
    <section class="section">
      <div class="container">
        <div class="row">
          <div class="col-lg-8">
            <div class="mb-3">
              <span class="badge {tech_color} me-2">{main_tech}</span>
              <span class="badge bg-info me-2">{category_badge}</span>
              <span class="badge {status_class}">{status_display}</span>
            </div>
            <h1 class="display-5 fw-bold mb-3">{title}</h1>
            <p class="lead text-muted mb-4">
              {description}
            </p>
            <div class="d-flex gap-3 mb-4">
              <a href="#" class="btn btn-primary">
                <i class="bi bi-eye me-2"></i>معاينة حية
              </a>
              <a href="#" class="btn btn-outline-secondary">
                <i class="bi bi-github me-2"></i>عرض الكود
              </a>
              <button class="btn btn-outline-info" onclick="shareProject()">
                <i class="bi bi-share me-2"></i>مشاركة
              </button>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="card">
              <div class="card-body">
                <h6 class="card-title">تفاصيل المشروع</h6>
                <ul class="list-unstyled mb-0">
                  <li class="mb-2">
                    <strong>الفئة:</strong> {category_display}
                  </li>
                  <li class="mb-2">
                    <strong>المدة:</strong> {timeline}
                  </li>
                  <li class="mb-2">
                    <strong>الفريق:</strong> {team_size}
                  </li>
                  <li class="mb-2">
                    <strong>السنة:</strong> {year}
                  </li>
                  <li class="mb-2">
                    <strong>الحالة:</strong> <span class="badge {status_class}">{status_display}</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Project Images -->
    <section class="section bg-light">
      <div class="container">
        <h2 class="section-title">صور المشروع</h2>
        <div class="row">
          <div class="col-lg-8">
            <div class="main-image-container mb-4">
              <img src="{images[0]}" class="img-fluid rounded shadow" alt="{title} - الصورة الرئيسية" id="mainImage">
            </div>
          </div>
          <div class="col-lg-4">
            <div class="row">'''
    
    # Add thumbnail images
    for i, image in enumerate(images):
        alt_text = f"صورة {i+1}" if i > 0 else "الصورة الرئيسية"
        html_content += f'''
              <div class="col-6 col-lg-12 mb-3">
                <img src="{image}" class="img-fluid rounded shadow-sm thumbnail-image" alt="{alt_text}" onclick="changeMainImage(this.src, this.alt)">
              </div>'''
    
    html_content += '''
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Project Description -->
    <section class="section">
      <div class="container">
        <div class="row">
          <div class="col-lg-8">
            <h2 class="section-title">نظرة عامة</h2>
            <p class="lead">
              ''' + detailed_description + '''
            </p>
            
            <h3 class="mt-5 mb-3">المميزات الرئيسية</h3>
            <div class="row">
              <div class="col-md-6">
                <ul class="list-unstyled">'''
    
    # Add features (split into two columns)
    mid_point = len(features) // 2
    for feature in features[:mid_point]:
        html_content += f'''
                  <li class="mb-2">
                    <i class="bi bi-check-circle text-success me-2"></i>
                    {feature}
                  </li>'''
    
    html_content += '''
                </ul>
              </div>
              <div class="col-md-6">
                <ul class="list-unstyled">'''
    
    for feature in features[mid_point:]:
        html_content += f'''
                  <li class="mb-2">
                    <i class="bi bi-check-circle text-success me-2"></i>
                    {feature}
                  </li>'''
    
    html_content += '''
                </ul>
              </div>
            </div>

            <h3 class="mt-5 mb-3">التقنيات المستخدمة</h3>
            <div class="row">'''
    
    # Add technologies
    for tech in technologies:
        html_content += f'''
              <div class="col-md-3 col-6 mb-3">
                <div class="text-center">
                  <div class="tech-icon mb-2">
                    <i class="bi bi-code-slash" style="font-size: 2rem; color: #3498db;"></i>
                  </div>
                  <h6>{tech}</h6>
                </div>
              </div>'''
    
    html_content += '''
            </div>
          </div>
          
          <div class="col-lg-4">
            <div class="card mb-4">
              <div class="card-header">
                <h6 class="mb-0">التحديات التقنية</h6>
              </div>
              <div class="card-body">
                <ul class="list-unstyled mb-0">'''
    
    # Add challenges
    for challenge in challenges:
        html_content += f'''
                  <li class="mb-2">
                    <i class="bi bi-exclamation-triangle text-warning me-2"></i>
                    {challenge}
                  </li>'''
    
    html_content += '''
                </ul>
              </div>
            </div>

            <div class="card">
              <div class="card-header">
                <h6 class="mb-0">الحلول المطبقة</h6>
              </div>
              <div class="card-body">
                <ul class="list-unstyled mb-0">'''
    
    # Add solutions
    for solution in solutions:
        html_content += f'''
                  <li class="mb-2">
                    <i class="bi bi-lightbulb text-success me-2"></i>
                    {solution}
                  </li>'''
    
    html_content += f'''
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Project Navigation -->
    <section class="section bg-light">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <a href="projects.html" class="btn btn-outline-primary">
                  <i class="bi bi-arrow-right me-2"></i>العودة للمشاريع
                </a>
              </div>
              <div class="d-flex gap-2">
                <a href="project-{prev_project}.html" class="btn btn-outline-secondary">
                  <i class="bi bi-chevron-right me-2"></i>المشروع السابق
                </a>
                <a href="project-{next_project}.html" class="btn btn-outline-secondary">
                  المشروع التالي<i class="bi bi-chevron-left ms-2"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Related Projects -->
    <section class="section">
      <div class="container">
        <h2 class="section-title">مشاريع ذات صلة</h2>
        <div class="row">'''
    
    # Add related projects
    for related in related_projects:
        related_tech = related['technologies'][0] if related['technologies'] else 'Unknown'
        related_tech_color = tech_colors.get(related_tech, 'bg-secondary')
        related_category_badge = category_map.get(related['category'], ('أخرى', 'Other'))[1]
        
        html_content += f'''
          <div class="col-lg-4 col-md-6 mb-4">
            <div class="card project-card h-100">
              <img src="{related['image']}" class="card-img-top" alt="{related['title']}">
              <div class="card-body">
                <div class="mb-2">
                  <span class="badge {related_tech_color} me-1">{related_tech}</span>
                  <span class="badge bg-info me-1">{related_category_badge}</span>
                </div>
                <h5 class="card-title">{related['title']}</h5>
                <p class="card-text">
                  {related['description'][:100]}...
                </p>
              </div>
              <div class="card-footer bg-transparent">
                <a href="project-{related['id']}.html" class="btn btn-outline-primary btn-sm">
                  <i class="bi bi-eye me-1"></i>عرض التفاصيل
                </a>
              </div>
            </div>
          </div>'''
    
    # Add the rest of the HTML (footer, scripts, etc.)
    html_content += f'''
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="section bg-primary text-white">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto text-center">
            <h2>مهتم بمشروع مشابه؟</h2>
            <p class="lead mb-4">
              يمكنني مساعدتك في تطوير مشروع مخصص لاحتياجاتك باستخدام أحدث التقنيات.
            </p>
            <a href="contact.html" class="btn btn-light btn-lg">
              <i class="bi bi-envelope me-2"></i>تواصل معي
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 mb-4">
            <h5>فارس</h5>
            <p>
              مطور ومصمم مواقع متخصص في Python و Flutter.
              أحب إنشاء حلول تقنية مبتكرة.
            </p>
            <div class="social-icons">
              <a href="#" title="GitHub"><i class="bi bi-github"></i></a>
              <a href="#" title="LinkedIn"><i class="bi bi-linkedin"></i></a>
              <a href="#" title="Twitter"><i class="bi bi-twitter"></i></a>
              <a href="#" title="Instagram"><i class="bi bi-instagram"></i></a>
            </div>
          </div>

          <div class="col-lg-2 col-md-6 mb-4">
            <h5>روابط سريعة</h5>
            <ul class="list-unstyled">
              <li><a href="index.html">الرئيسية</a></li>
              <li><a href="about.html">نبذة عني</a></li>
              <li><a href="projects.html">المشاريع</a></li>
              <li><a href="contact.html">تواصل معي</a></li>
            </ul>
          </div>

          <div class="col-lg-3 col-md-6 mb-4">
            <h5>الخدمات</h5>
            <ul class="list-unstyled">
              <li><a href="#">تطوير تطبيقات الجوال</a></li>
              <li><a href="#">تطوير مواقع الويب</a></li>
              <li><a href="#">التدريب والتعليم</a></li>
              <li><a href="#">استشارات تقنية</a></li>
            </ul>
          </div>

          <div class="col-lg-3 col-md-6 mb-4">
            <h5>تواصل معي</h5>
            <ul class="list-unstyled">
              <li><i class="bi bi-envelope me-2"></i>fares@example.com</li>
              <li><i class="bi bi-phone me-2"></i>+966 50 123 4567</li>
              <li><i class="bi bi-geo-alt me-2"></i>الرياض، السعودية</li>
            </ul>
          </div>
        </div>

        <hr class="my-4">

        <div class="row align-items-center">
          <div class="col-md-4">
            <p class="mb-0">&copy; 2024 فارس. جميع الحقوق محفوظة.</p>
          </div>
          <div class="col-md-4 text-center">
            <div id="visitor-counter" class="text-light">
              <!-- Analytics counter will be inserted here -->
            </div>
          </div>
          <div class="col-md-4 text-md-end">
            <a href="#" class="text-light me-3">سياسة الخصوصية</a>
            <a href="#" class="text-light">شروط الاستخدام</a>
          </div>
        </div>
      </div>
    </footer>

    <!-- Back to Top Button -->
    <button id="backToTop" class="btn btn-primary position-fixed" style="bottom: 20px; left: 20px; display: none; z-index: 1000;">
      <i class="bi bi-arrow-up"></i>
    </button>

    <!-- Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>

    <!-- Custom JavaScript -->
    <script src="js/main.js"></script>

    <!-- Analytics JavaScript -->
    <script src="js/analytics.js"></script>

    <!-- Project Detail JavaScript -->
    <script>
      // Change main image function
      function changeMainImage(src, alt) {{
        const mainImage = document.getElementById('mainImage');
        mainImage.src = src;
        mainImage.alt = alt;
        
        // Add fade effect
        mainImage.style.opacity = '0.5';
        setTimeout(() => {{
          mainImage.style.opacity = '1';
        }}, 150);
      }}

      // Share project function
      function shareProject() {{
        if (navigator.share) {{
          navigator.share({{
            title: '{title} - فارس',
            text: '{description}',
            url: window.location.href
          }});
        }} else {{
          // Fallback for browsers that don't support Web Share API
          const url = window.location.href;
          navigator.clipboard.writeText(url).then(() => {{
            showNotification('تم نسخ رابط المشروع!', 'success');
          }});
        }}
      }}

      // Add smooth scrolling for anchor links
      document.addEventListener('DOMContentLoaded', function() {{
        // Add click handlers for thumbnail images
        const thumbnails = document.querySelectorAll('.thumbnail-image');
        thumbnails.forEach(thumb => {{
          thumb.style.cursor = 'pointer';
          thumb.addEventListener('mouseenter', function() {{
            this.style.opacity = '0.8';
          }});
          thumb.addEventListener('mouseleave', function() {{
            this.style.opacity = '1';
          }});
        }});
      }});
    </script>

    <style>
      .thumbnail-image {{
        transition: opacity 0.3s ease;
        cursor: pointer;
      }}
      
      .thumbnail-image:hover {{
        opacity: 0.8;
      }}
      
      .main-image-container img {{
        transition: opacity 0.3s ease;
      }}
      
      .tech-icon {{
        transition: transform 0.3s ease;
      }}
      
      .tech-icon:hover {{
        transform: scale(1.1);
      }}
      
      .project-card {{
        transition: transform 0.3s ease, box-shadow 0.3s ease;
      }}
      
      .project-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
      }}
    </style>
  </body>
</html>'''
    
    # Write the file
    filename = f"project-{project_id}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Created: {filename}")

def main():
    """Create all remaining project pages"""
    
    # Load project data
    project_data = load_project_data()
    projects = project_data['projects']
    
    # Create pages for projects 3, 4, 5, 6 (1 and 2 already exist)
    for project in projects:
        if project['id'] in [3, 4, 5, 6]:
            create_project_page(project, project_data)
    
    print("\n🎉 All remaining project pages created successfully!")
    print("📄 Created: project-3.html, project-4.html, project-5.html, project-6.html")

if __name__ == "__main__":
    main()
