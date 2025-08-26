# 😷 Face Mask Detection using MobileNetV2 + Gradio

## 📖 Project Overview
This project aims to detect whether a person is wearing a face mask or not in images and videos using a **MobileNetV2** model trained on a face mask dataset.  
A **Gradio** interface provides an interactive web-based experience.

---

## 🗂 Dataset
- **Source**: Face Mask Detection Dataset (adjustable based on your dataset).  
- **Number of Images**: X images (approximate).  
- **Classes**:
  | Class        | Description               |
  |-------------|---------------------------|
  | With Mask   | Person is wearing a mask  |
  | Without Mask | Person is not wearing a mask |

- **Image Type**: RGB images, varying resolutions and lighting, some images contain multiple faces.

---

## 🧠 Model Comparison
| Model           | Training Accuracy | Validation Accuracy | Notes |
|-----------------|-----------------|------------------|-------|
| CNN from scratch | 0.90            | 0.88             | Fast but less generalization |
| MobileNetV2     | 0.95            | 0.93             | Lightweight, better performance on external images |
| (Future: X)     | TBD             | TBD              | Could include EfficientNet or ResNet50 |

---

## ⚙️ Usage

### 1. Run Locally
```bash
git clone https://github.com/username/face-mask-detection.git
cd face-mask-detection
pip install -r requirements.txt
python app.py
Open the browser at http://0.0.0.0:7860
Use Upload Image tab to upload photos

Or use Use Webcam tab for live capture

2. Hugging Face Spaces
Upload the following files:

app.py

Model file face_mask_mobilenetv2.h5

No separate CSS file is needed; everything is included in app.py

## 📓 Notebook
train_face_mask.ipynb:

Data preparation + Preprocessing + Augmentation

Training CNN and MobileNetV2 models

Saving the model (.h5)

Plotting training/validation Loss & Accuracy curves

Generating classification reports for each class

## ⚠️ Challenges & Solutions
Challenge	Solution
External images not recognized	Used Augmentation + Face Detection preprocessing
Multiple faces in one image	Added support for Multiple Faces + Scrollable HTML output
Varying lighting and orientations	Enhanced preprocessing: Resize + Normalization + CLAHE
Incorrect predictions on unclear faces	Added confidence threshold to show "Unclear"
## 🔮 Future Work
Support real-time video / live stream detection

Integrate TensorFlow Lite or ONNX for faster inference

Improve UI: Dark/Light Mode + Zoom + Tooltips

Add Export options: CSV / images with results

Integrate Face Alignment for better accuracy on tilted faces

