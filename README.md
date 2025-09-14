# شات بوت كلية العلوم - النسخة المحسنة 🎓

شات بوت ذكي محسن مصمم خصيصاً لكلية العلوم، يستخدم تقنيات الذكاء الاصطناعي المتقدمة مع دعم الأقسام المختلفة ومعالجة أفضل للملفات.

## المميزات الجديدة ✨

### 🏛️ دعم الأقسام المختلفة
- **الفرقة الأولى**: علوم طبيعية، بيولوجي
- **الفرق الأعلى (2-4)**: حاسب آلي، رياضة، فيزياء، ميكروبيولوجي، حيوان وكيمياء، نانو تكنولوجي، جيولوجيا، كيمياء تطبيقية، كيمياء اسبيشيال

### 📄 دعم ملفات متعددة
- **ملفات Word** (.docx, .doc)
- **ملفات PDF** (.pdf)
- **ملفات نصية** (.txt)
- استخراج تلقائي للنص من جميع الأنواع

### 🤖 ذكاء اصطناعي محسن
- معالجة أفضل للأخطاء
- بحث ذكي في البيانات المحلية
- فلترة محسنة للمحتوى
- استجابة أسرع وأكثر دقة

### 🎯 واجهة مستخدم محسنة
- تصميم أكثر حداثة وجمالاً
- دعم كامل للأجهزة المحمولة
- تجربة مستخدم محسنة
- إدارة أفضل للبيانات

## التثبيت والإعداد 🚀

### 1. متطلبات النظام
- Python 3.11 أو أحدث
- 4 جيجابايت رام على الأقل
- 2 جيجابايت مساحة تخزين فارغة
- اتصال بالإنترنت

### 2. تحميل المشروع
```bash
# انسخ ملفات المشروع إلى مجلد جديد
cd /path/to/your/directory
```

### 3. إعداد البيئة الافتراضية
```bash
# إنشاء البيئة الافتراضية
python -m venv venv

# تفعيل البيئة الافتراضية
# في Linux/Mac:
source venv/bin/activate
# في Windows:
venv\Scripts\activate
```

### 4. تثبيت المكتبات
```bash
pip install -r requirements.txt
```

### 5. إعداد متغيرات البيئة
انسخ ملف `.env.example` إلى `.env` وأضف مفاتيح API:

```env
# مفاتيح API (مطلوبة)
DEEPSEEK_API_KEY=your-deepseek-api-key-here
GEMINI_API_KEY=your-gemini-api-key-here

# إعدادات اختيارية
FLASK_ENV=development
FLASK_DEBUG=True
```

### 6. تشغيل التطبيق
```bash
python main.py
```

سيعمل التطبيق على: `http://localhost:5000`

## الحصول على مفاتيح API 🔑

### DeepSeek API
1. اذهب إلى [DeepSeek Platform](https://platform.deepseek.com)
2. أنشئ حساب جديد أو سجل الدخول
3. اذهب إلى قسم API Keys
4. أنشئ مفتاح API جديد
5. انسخ المفتاح وضعه في ملف `.env`

### Gemini API
1. اذهب إلى [Google AI Studio](https://makersuite.google.com)
2. سجل الدخول بحساب Google
3. أنشئ مفتاح API جديد
4. انسخ المفتاح وضعه في ملف `.env`

## كيفية الاستخدام 📖

### 1. الإعداد الأولي
- عند فتح التطبيق لأول مرة، ستظهر نافذة الإعداد
- اختر الفرقة الدراسية (1-4)
- اختر الترم الدراسي (1-2)
- اختر القسم المناسب لفرقتك
- اضغط "تأكيد وبدء الاستخدام"

### 2. طرح الأسئلة
- اكتب سؤالك في مربع النص
- اضغط إرسال أو Enter
- ستحصل على إجابة مخصصة لقسمك وفرقتك

### 3. رفع الصور
- اضغط على أيقونة الكاميرا 📷
- اختر صورة من جهازك
- اكتب سؤالك عن الصورة
- اضغط إرسال

### 4. إدارة البيانات
- اضغط على أيقونة قاعدة البيانات 🗄️
- ارفع ملفات المنهج (Word, PDF, أو نصية)
- حدد الفرقة والترم والقسم للملف
- سيتم استخراج النص تلقائياً

## بنية المشروع 📁

```
improved_chatbot/
├── main.py                     # الملف الرئيسي
├── requirements.txt            # المكتبات المطلوبة
├── .env.example               # مثال لمتغيرات البيئة
├── README.md                  # هذا الملف
├── models/
│   └── user.py               # نماذج قاعدة البيانات
├── routes/
│   ├── user.py               # مسارات المستخدمين
│   ├── chatbot.py            # مسارات الشات بوت
│   └── admin.py              # مسارات إدارة الأقسام
├── services/
│   ├── ai_service.py         # خدمة الذكاء الاصطناعي
│   ├── file_service.py       # خدمة معالجة الملفات
│   └── media_service.py      # خدمة الوسائط المتعددة
├── static/
│   ├── index.html            # الواجهة الرئيسية
│   ├── styles.css            # ملف التصميم
│   └── script.js             # ملف JavaScript
├── database/                 # قاعدة البيانات
├── data/                     # ملفات البيانات المرفوعة
└── uploads/                  # الملفات المؤقتة
```

## API Endpoints 🔗

### الشات العادي
```
POST /api/chat
Content-Type: multipart/form-data

message: "ما هو التمثيل الضوئي؟"
grade: 1
semester: 1
department_code: "BIO"
```

### الشات مع الصور
```
POST /api/chat-image
Content-Type: multipart/form-data

message: "ما هذا المركب الكيميائي؟"
image: [ملف الصورة]
grade: 2
semester: 1
department_code: "CHEM_G2"
```

### رفع البيانات
```
POST /api/upload-data
Content-Type: multipart/form-data

file: [ملف Word/PDF/نصي]
grade: 1
semester: 1
department_code: "BIO"
```

### إدارة الأقسام
```
GET /api/departments?grade=1
POST /api/admin/departments
PUT /api/admin/departments/{id}
DELETE /api/admin/departments/{id}
```

## المشاكل المحلولة 🔧

### 1. مشاكل API السابقة
- ✅ معالجة أفضل لأخطاء الاتصال
- ✅ إعادة المحاولة التلقائية
- ✅ رسائل خطأ واضحة
- ✅ فحص صحة النظام

### 2. مشاكل رفع الملفات
- ✅ دعم ملفات Word و PDF
- ✅ استخراج تلقائي للنص
- ✅ معالجة أفضل للأخطاء
- ✅ حفظ منظم حسب القسم

### 3. تحسينات الواجهة
- ✅ تصميم أكثر حداثة
- ✅ دعم كامل للأجهزة المحمولة
- ✅ تجربة مستخدم محسنة
- ✅ إدارة أفضل للحالات

## النشر على الخادم 🌐

### 1. النشر على خادم Linux
```bash
# تحديث النظام
sudo apt update && sudo apt upgrade -y

# تثبيت Python و pip
sudo apt install python3 python3-pip python3-venv -y

# رفع الملفات إلى الخادم
scp -r improved_chatbot/ user@server:/path/to/deployment/

# الدخول للخادم
ssh user@server

# الانتقال لمجلد المشروع
cd /path/to/deployment/improved_chatbot/

# إعداد البيئة الافتراضية
python3 -m venv venv
source venv/bin/activate

# تثبيت المكتبات
pip install -r requirements.txt

# إعداد متغيرات البيئة
cp .env.example .env
nano .env
# أضف مفاتيح API

# تشغيل التطبيق مع Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

### 2. النشر مع Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
```

## استكشاف الأخطاء 🔧

### مشاكل شائعة وحلولها

#### 1. خطأ في مفاتيح API
```
Error: Invalid API key
```
**الحل**: تأكد من صحة مفاتيح API في ملف `.env`

#### 2. خطأ في تثبيت المكتبات
```
ERROR: Could not install packages
```
**الحل**: 
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

#### 3. خطأ في قراءة ملفات Word
```
Error reading docx file
```
**الحل**: تأكد من تثبيت `python-docx` بشكل صحيح

#### 4. مشاكل في رفع الملفات الكبيرة
```
413 Request Entity Too Large
```
**الحل**: الملفات محدودة بـ 16 ميجابايت، قم بتقسيم الملفات الكبيرة

### فحص صحة النظام
```bash
# فحص حالة النظام
curl http://localhost:5000/api/health

# فحص الاتصال بقاعدة البيانات
python -c "from models.user import db; print('Database OK')"
```

## التطوير والمساهمة 👨‍💻

### إعداد بيئة التطوير
```bash
# استنساخ المشروع
git clone <repository-url>
cd improved_chatbot

# إعداد البيئة الافتراضية
python -m venv venv
source venv/bin/activate  # Linux/Mac
# أو
venv\Scripts\activate     # Windows

# تثبيت المكتبات
pip install -r requirements.txt

# إعداد متغيرات البيئة
cp .env.example .env
# أضف مفاتيح API

# تشغيل في وضع التطوير
export FLASK_ENV=development
export FLASK_DEBUG=True
python main.py
```

### إضافة أقسام جديدة
```python
# في routes/admin.py
# أضف الأقسام الجديدة في دالة init_departments
```

### اختبار التطبيق
```bash
# اختبار API endpoints
curl -X POST http://localhost:5000/api/chat \
  -F "message=ما هو الماء؟" \
  -F "grade=1" \
  -F "semester=1"
```

## الأمان والخصوصية 🔒

### حماية مفاتيح API
- ✅ استخدام متغيرات البيئة
- ✅ عدم تخزين المفاتيح في الكود
- ✅ فحص صحة المفاتيح

### حماية البيانات
- ✅ ملفات البيانات محلية فقط
- ✅ الصور المؤقتة تُحذف تلقائياً
- ✅ تشفير قاعدة البيانات
- ✅ حدود حجم الملفات

### أفضل الممارسات
- ✅ استخدام HTTPS في الإنتاج
- ✅ تحديث المكتبات دورياً
- ✅ مراقبة استخدام API
- ✅ نسخ احتياطية منتظمة

## الدعم والمساعدة 💬

### الحصول على المساعدة
- اقرأ هذا الدليل كاملاً
- تحقق من قسم استكشاف الأخطاء
- استخدم endpoint `/api/health` لفحص النظام

### الإبلاغ عن المشاكل
عند الإبلاغ عن مشكلة، أرفق:
- وصف المشكلة بالتفصيل
- رسالة الخطأ كاملة
- خطوات إعادة إنتاج المشكلة
- معلومات النظام والمتصفح

## التحديثات الجديدة 🆕

### الإصدار 2.0
- ✅ دعم الأقسام المختلفة
- ✅ معالجة ملفات Word و PDF
- ✅ واجهة مستخدم محسنة
- ✅ معالجة أفضل للأخطاء
- ✅ بحث ذكي محسن
- ✅ إدارة أفضل للبيانات

### خطط مستقبلية
- 🔄 دعم المزيد من أنواع الملفات
- 🔄 تحليل أفضل للصور
- 🔄 إنشاء محتوى صوتي ومرئي
- 🔄 تكامل مع المزيد من خدمات AI

## الترخيص 📄

هذا المشروع مرخص تحت رخصة MIT. راجع ملف LICENSE للتفاصيل.

## الشكر والتقدير 🙏

شكر خاص لـ:
- فريق DeepSeek على نموذج الذكاء الاصطناعي المتطور
- Google على Gemini AI
- مجتمع Python ومطوري Flask
- جميع المساهمين في المكتبات مفتوحة المصدر

---

**تم تطوير هذا المشروع المحسن بـ ❤️ لخدمة التعليم العلمي**

للمزيد من المعلومات أو الدعم الفني، لا تتردد في التواصل معنا.

