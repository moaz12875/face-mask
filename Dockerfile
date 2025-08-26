# نبدأ من Python الرسمي
FROM python:3.10-slim

# ضبط مكان العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع
COPY requirements.txt .
COPY app.py .
COPY mobilenet_mask.h5 .
COPY style.css .
COPY examples ./examples

# تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

# فتح البورت اللي هيشغل عليه Gradio
EXPOSE 7860

# أمر التشغيل
CMD ["python", "app.py"]