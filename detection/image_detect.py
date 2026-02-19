import cv2

def detect_image(model, image):
    results = model(image)
    output = image.copy()

    for r in results:
        for box in r.boxes:
            x1,y1,x2,y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cv2.rectangle(output,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(output,f"Pothole:{conf:.2f}",(x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
    return output
