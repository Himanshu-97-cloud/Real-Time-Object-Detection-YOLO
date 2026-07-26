# 🎯 Real-Time Object Detection using YOLOv8

## 📌 Overview

This project performs object detection using **YOLOv8**. It provides:

- **Real-time webcam detection** (Local)
- **Image upload detection** (Streamlit Web App)

Detected objects are displayed with **bounding boxes, class labels, and confidence scores**.

---

## 🚀 Features

- ✅ Real-time object detection
- ✅ Image upload through Streamlit
- ✅ Webcam detection (local)
- ✅ Bounding boxes with class labels
- ✅ Confidence score display
- ✅ Lightweight YOLOv8 Nano model

---

## 🛠 Tech Stack

- Python
- OpenCV
- Streamlit
- Ultralytics YOLOv8
- NumPy
- Pillow

---

## 📂 Project Structure

```text
YOLO-Object-Detection/
│── app.py
│── realtime_yolo.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/YOLO-Object-Detection.git
cd YOLO-Object-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

Upload an image and the model will detect objects automatically.

---

## ▶️ Run Real-Time Webcam Detection

```bash
python realtime_yolo.py
```

Press **Q** to exit.

---

## 📦 Requirements

- streamlit
- ultralytics
- opencv-python-headless
- torch
- torchvision
- numpy
- Pillow

---

## ⚠️ Notes

- `yolov8n.pt` is automatically downloaded if not available.
- Webcam detection works only on the local machine.
- The deployed Streamlit app supports image upload.

---

## 👨‍💻 Author

**Himanshu Pal**
