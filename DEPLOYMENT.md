# دليل النشر والاستضافة

## الملفات المطلوبة للنشر

تأكد من وجود جميع الملفات التالية قبل النشر:

### الملفات الأساسية:
- `index.html` - الصفحة الرئيسية
- `about.html` - صفحة نبذة عني
- `projects.html` - صفحة المشاريع
- `courses.html` - صفحة الدورات
- `articles.html` - صفحة المقالات
- `contact.html` - صفحة التواصل

### مجلد CSS:
- `css/custom.css` - ملف الأنماط المخصص

### مجلد JavaScript:
- `js/main.js` - ملف JavaScript الرئيسي

### مجلد الصور:
- `img/` - جميع الصور المطلوبة (انظر README.md للقائمة الكاملة)

### ملفات إضافية:
- `README.md` - دليل الاستخدام
- `generate-placeholders.html` - أداة إنشاء الصور التجريبية

## خطوات النشر

### 1. إعداد الصور

#### الطريقة الأولى: استخدام أداة إنشاء الصور التجريبية
1. افتح `generate-placeholders.html` في المتصفح
2. انقر بالزر الأيمن على كل صورة واحفظها في مجلد `img/`
3. استخدم الأسماء المقترحة للملفات

#### الطريقة الثانية: استخدام صورك الخاصة
1. أنشئ مجلد `img/` إذا لم يكن موجوداً
2. أضف صورك الشخصية والمشاريع
3. تأكد من استخدام الأسماء الصحيحة للملفات

### 2. تخصيص المحتوى

#### تحديث المعلومات الشخصية:
```html
<!-- في جميع الملفات، استبدل: -->
فارس → اسمك
fares@example.com → بريدك الإلكتروني
+966 50 123 4567 → رقم هاتفك
الرياض، السعودية → موقعك
```

#### تحديث روابط وسائل التواصل:
```html
<!-- في الفوتر، حدث الروابط: -->
<a href="#" title="GitHub"> → <a href="https://github.com/yourusername" title="GitHub">
<a href="#" title="LinkedIn"> → <a href="https://linkedin.com/in/yourusername" title="LinkedIn">
```

### 3. اختبار الموقع محلياً

```bash
# في مجلد المشروع
python -m http.server 8000

# أو باستخدام Node.js
npx serve .

# ثم افتح المتصفح على
http://localhost:8000
```

### 4. خيارات الاستضافة

#### أ) GitHub Pages (مجاني)
1. أنشئ repository جديد على GitHub
2. ارفع جميع الملفات
3. اذهب إلى Settings > Pages
4. اختر source: Deploy from a branch
5. اختر branch: main
6. احفظ الإعدادات

#### ب) Netlify (مجاني)
1. اذهب إلى [netlify.com](https://netlify.com)
2. اسحب مجلد المشروع إلى الموقع
3. أو اربط repository من GitHub
4. سيتم النشر تلقائياً

#### ج) Vercel (مجاني)
1. اذهب إلى [vercel.com](https://vercel.com)
2. اربط حساب GitHub
3. اختر repository المشروع
4. انقر Deploy

#### د) Firebase Hosting (مجاني)
```bash
# تثبيت Firebase CLI
npm install -g firebase-tools

# تسجيل الدخول
firebase login

# إعداد المشروع
firebase init hosting

# النشر
firebase deploy
```

### 5. إعداد نطاق مخصص (اختياري)

#### لـ GitHub Pages:
1. اشتري نطاق من مزود خدمة
2. في إعدادات repository > Pages
3. أضف النطاق المخصص
4. حدث DNS records عند مزود النطاق

#### لـ Netlify:
1. في لوحة تحكم Netlify
2. اذهب إلى Domain settings
3. أضف النطاق المخصص
4. اتبع تعليمات DNS

### 6. تحسين الأداء

#### ضغط الصور:
- استخدم أدوات مثل TinyPNG أو ImageOptim
- حول الصور إلى تنسيق WebP إذا أمكن
- استخدم أحجام مناسبة (لا تزيد عن 1MB للصورة)

#### تحسين CSS و JavaScript:
```bash
# تصغير CSS
npx clean-css-cli css/custom.css -o css/custom.min.css

# تصغير JavaScript
npx terser js/main.js -o js/main.min.js
```

#### إضافة ملف robots.txt:
```
User-agent: *
Allow: /

Sitemap: https://yourwebsite.com/sitemap.xml
```

#### إضافة ملف sitemap.xml:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yourwebsite.com/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://yourwebsite.com/about.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <!-- أضف باقي الصفحات -->
</urlset>
```

### 7. تحليلات الموقع

#### Google Analytics:
1. أنشئ حساب على Google Analytics
2. احصل على tracking code
3. أضفه قبل `</head>` في جميع الصفحات

#### Google Search Console:
1. أضف موقعك إلى Search Console
2. تحقق من الملكية
3. أرسل sitemap.xml

### 8. نصائح إضافية

- **النسخ الاحتياطي**: احتفظ بنسخة احتياطية من الملفات
- **التحديثات**: حدث المحتوى بانتظام
- **الأمان**: استخدم HTTPS دائماً
- **السرعة**: اختبر سرعة الموقع باستخدام PageSpeed Insights
- **الاستجابة**: اختبر الموقع على أجهزة مختلفة

### 9. استكشاف الأخطاء

#### مشاكل شائعة:
- **الصور لا تظهر**: تأكد من مسارات الصور الصحيحة
- **الخطوط العربية**: تأكد من تحديد UTF-8 encoding
- **المظهر المظلم**: تأكد من تحميل JavaScript بشكل صحيح
- **الروابط المكسورة**: تحقق من جميع الروابط الداخلية

#### أدوات مفيدة:
- [W3C Validator](https://validator.w3.org/) - للتحقق من صحة HTML
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - للتحقق من صحة CSS
- [PageSpeed Insights](https://pagespeed.web.dev/) - لاختبار السرعة
- [GTmetrix](https://gtmetrix.com/) - لتحليل الأداء

---

**ملاحظة**: تذكر تحديث جميع المعلومات الشخصية قبل النشر!
