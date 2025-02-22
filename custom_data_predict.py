import os

from ultralytics import YOLO
import cv2

#cap = cv2.VideoCapture('marol_bitki_detection.mp4') # this line it to use video file like a video source
cap = cv2.VideoCapture(0) #this line it for use realtime camera close it if you want to use another video source
ret, frame = cap.read()
H, W, _= frame.shape
out = cv2.VideoWriter('letuce_detect_result_1.avi', cv2.VideoWriter_fourcc(*'MJPG'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

#model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'best.pt')
model_path = os.path.join('.', 'runs', 'detect', 'yolov8n_custom', 'weights', 'last.pt') 

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.1


#results = model("SUNP0253.jpg")
#print(results)

while ret:

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    #out.write(frame) #this line is to save video_file_result
    cv2.imshow('frame', frame) 
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
