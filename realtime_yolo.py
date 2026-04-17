# Usage: python realtime_yolo.py         -> webcam 0
#        python realtime_yolo.py 0       -> webcam explicit
#        python realtime_yolo.py video.mp4

import sys, cv2
from ultralytics import YOLO

def src_parse(a):
    return int(a) if isinstance(a, str) and a.isdigit() else a

def draw(frame, boxes, names):
    if boxes is None: return
    for b in boxes:
        x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
        cls = int(b.cls[0].item())
        conf = float(b.conf[0].item())
        label = f"{names.get(cls, cls)} {conf:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 1)

def main(source=0, model_name="yolov8n.pt", conf=0.35):
    print("Loading model...", model_name)
    try:
        model = YOLO(model_name)
    except Exception as e:
        print("Model load error:", e)
        return
    src = src_parse(source)
    print("Running source:", src)
    try:
        for r in model.predict(source=src, conf=conf, stream=True):
            if r is None:
                continue
            frame = r.orig_img
            draw(frame, getattr(r, "boxes", None), model.names)
            cv2.imshow("YOLOv8", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print("Runtime error:", e)
    finally:
        cv2.destroyAllWindows()
        print("Stopped.")

arg = sys.argv[1] if len(sys.argv) > 1 else 0
main(arg)
