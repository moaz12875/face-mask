import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# تحميل الموديل
model = tf.keras.models.load_model("mobilenet_mask.h5")

# دالة التنبؤ
def predict(img):
    img = img.resize((224,224))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)[0]
    if pred[0] > pred[1]:
        text = "😷 With Mask"
    else:
        text = "❌ Without Mask"
    return {"With Mask": float(pred[0]), "Without Mask": float(pred[1])}, text

# Gradio Blocks UI
with gr.Blocks(css="style.css") as demo:
    gr.Markdown(
        """
        # 😷 Face Mask Detection  
        Detect whether a person is **wearing a mask** or **not** using MobileNetV2.  
        """
    )

    with gr.Tab("📤 Upload Image"):
        with gr.Row():
            image_input = gr.Image(type="pil", label="Upload an image")
            with gr.Column():
                output_label = gr.Label(num_top_classes=2, label="Prediction")
                output_text = gr.Textbox(label="Result", interactive=False)
        btn = gr.Button("🔍 Predict")
        btn.click(fn=predict, inputs=image_input, outputs=[output_label, output_text])

    with gr.Tab("📷 Webcam"):
        with gr.Row():
            webcam_input = gr.Image(source="webcam", type="pil", label="Take a photo")
            with gr.Column():
                cam_label = gr.Label(num_top_classes=2, label="Prediction")
                cam_text = gr.Textbox(label="Result", interactive=False)
        gr.Button("📸 Predict from Camera").click(predict, webcam_input, [cam_label, cam_text])

    with gr.Tab("🖼️ Gallery"):
        gr.Examples(
            examples=[
                ["examples/with_mask.jpg"],
                ["examples/without_mask.jpg"],
            ],
            inputs=image_input,
            outputs=[output_label, output_text],
            fn=predict,
            cache_examples=True
        )

demo.launch()