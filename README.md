
# 😷 Face Mask Detection using MobileNetV2  

This project focuses on detecting whether a person is wearing a face mask in images or webcam feed using a **MobileNetV2** model.  
The final app is deployed with a **Gradio** interface, featuring real-time predictions, interactive output, and a custom CSS design.

---

## 📂 Dataset

The dataset used is a **Face Mask Detection Dataset** (public datasets from Kaggle or collected manually).  

- Contains **X images** of faces with and without masks.  
- Each image is labeled as:  
  - **With Mask** → Person is wearing a mask  
  - **Without Mask** → Person is not wearing a mask  

---

## 🤖 Model Comparison  

Several models were trained and compared for accuracy and generalization:

| Model                  | Training Accuracy | Validation Accuracy | Notes |
|-------------------------|-----------------|------------------|-------|
| CNN from scratch        | 0.90            | 0.88             | Fast but less robust on new images |
| MobileNetV2             | 0.95            | 0.93             | Lightweight, better performance on external images |
| (Future: EfficientNet)  | TBD             | TBD              | Could improve generalization |

✅ MobileNetV2 was selected as the final model for its balance between performance and size.

---

## ⚡ Features

- **Data Preprocessing:**  
  - Resize to 224x224, normalization  
  - Data augmentation: rotation, zoom, flips  

- **Face Detection:**  
  - OpenCV Haar Cascade used to detect faces before classification  
  - Returns whole image if no face is found  

- **Gradio Web App:**  
  - Upload image or capture from webcam  
  - Interactive HTML output indicating **With Mask / Without Mask**  
  - Custom CSS dark-themed interface  

---
## How to use
Use our demo on Hugging Face Spaces:

[👉Try it live](https://huggingface.co/spaces/Moaz-ai/facemask)

## 📒 Notebook

Included Jupyter Notebook (`notebooks/train_face_mask.ipynb`) for:  

- **Data Exploration & Augmentation**  
- **Model Training & Evaluation**  
- **Plotting Loss/Accuracy Curves**  
- **Classification Reports**
- 
[View on colab](https://colab.research.google.com/drive/1chIbzk77Qx0lVEby71agiKIq2MnLS50I#scrollTo=56H4t4Tt_6z)
---

## ⚠️ Challenges & Solutions

| Problem | Solution |
|---------|----------|
| **External images not recognized** | Applied data augmentation + face detection preprocessing |
| **Multiple faces in one image** | Added support for processing first detected face; could extend to multiple faces |
| **Varying lighting and orientations** | Enhanced preprocessing: resizing, normalization, optional CLAHE |
| **Unclear predictions** | Added HTML output and confidence threshold for "Unclear" cases |

---

## 🎯 Future Work

- Real-time video/live stream detection  
- Integrate TensorFlow Lite or ONNX for faster inference  
- Enhance UI: Dark/Light mode toggle, zoom, tooltips  
- Add export options: CSV/images with results  
- Implement face alignment for tilted faces  

---

**Prepared by Moaz Mohamed**  
[LinkedIn](https://www.linkedin.com/in/moaz-mohamed-545725375/)
