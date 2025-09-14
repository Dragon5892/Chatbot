import os
import sys
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models.user import db
from routes.user import user_bp
from routes.chatbot import chatbot_bp  
from routes.admin import admin_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# إعداد CORS للسماح بالطلبات من أي مصدر
CORS(app)

# تسجيل المسارات
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(chatbot_bp, url_prefix='/api')
app.register_blueprint(admin_bp, url_prefix='/api/admin')

# إعداد قاعدة البيانات
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# إنشاء مجلد قاعدة البيانات
os.makedirs(os.path.join(os.path.dirname(__file__), 'database'), exist_ok=True)

# تهيئة قاعدة البيانات و Migrate
db.init_app(app)
migrate = Migrate(app, db)

# إنشاء الجداول (للتطوير - في الإنتاج استخدم flask db migrate)
with app.app_context():
    try:
        db.create_all()
        print("✅ تم إنشاء جداول قاعدة البيانات بنجاح")
    except Exception as e:
        print(f"⚠️ خطأ في إنشاء الجداول: {e}")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

@app.errorhandler(413)
def too_large(e):
    return jsonify({'error': 'الملف كبير جداً. الحد الأقصى 16 ميجابايت'}), 413

@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'حدث خطأ داخلي في الخادم'}), 500

# معلومات التطبيق والإصدار
@app.route('/api/info')
def app_info():
    return jsonify({
        'name': 'كلية العلوم - بوت الدردشة المحسن',
        'version': '2.0.0',
        'features': {
            'enhanced_file_processing': True,
            'chat_logging': True,
            'user_sessions': True,
            'full_pdf_reading': True,
            'intelligent_chunking': True
        },
        'last_updated': '2024-09-14'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
