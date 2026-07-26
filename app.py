import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="YOLOv8 Object Detection", page_icon="🎯")

st.title("🎯 Real-Time Object Detection using YOLOv8")
st.write("Upload an image and detect objects.")

# Load model
model = YOLO("yolov8n.pt")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

confidence = st.slider(
    "Confidence Threshold",
    0.1,
    1.0,
    0.35
)

if uploaded_file:

    image = Image.open(uploaded_file)

    image_np = np.array(image)

    results = model.predict(image_np, conf=confidence)

    output = results[0].plot()

    st.image(output, caption="Detection Result", use_container_width=True)