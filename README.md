🎯 Real-Time Object Detection using YOLOv8
📌 Overview
This project performs real-time object detection using YOLOv8. It supports webcam input as well as video file input and displays bounding boxes with class labels and confidence scores.

🚀 Features
Real-time object detection
Webcam and video file support
Bounding boxes with labels and confidence
Lightweight YOLOv8 model (yolov8n)
🛠 Tech Stack
Python
OpenCV
Ultralytics YOLOv8
⚙️ Setup Instructions
1. Install dependencies
pip install ultralytics opencv-python
2. Download YOLOv8 model
Download model automatically or manually:

yolo detect predict model=yolov8n.pt source=0
OR download from: https://github.com/ultralytics/ultralytics

3. Run the project
Webcam:
python realtime_yolo.py
Video file:
python realtime_yolo.py video.mp4
⌨️ Controls
Press Q to exit
⚠️ Notes
yolov8n.pt model file is not included due to size
Video files are not included
Model will download automatically if not present
👨‍💻 Author
Himanshu Pal
