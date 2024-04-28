'''from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")

model.train(data="config.yaml", epochs=3)  # train the model
'''
from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='data.yaml',
   imgsz=640,
   epochs=15,
   name='yolov8n_custom'
)