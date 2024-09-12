# Lettuce and Bad Plant Detection Using YOLOv8
This project focuses on leveraging machine learning to detect lettuce plants and unwanted or "bad" plants in agricultural fields. Using the YOLOv8n model, the system was designed as part of the Unmanned Agriculture Vehicle competition at Teknofest, where the goal was to create a system that could autonomously identify and differentiate between healthy lettuce plants and undesirable plants, optimizing agricultural productivity.

Project Video:
A video demonstration showcasing the system’s ability to detect lettuce and bad plants in action is available on YouTube.
  - https://youtu.be/nEUbbnlmOuk?si=2DTKxZJFgaN-Z8I3

Components and Methodology:
- Data Collection:

  - Video Footage: Using a GoPro camera, data was collected in the field to capture images and videos of lettuce and bad plants. This raw data formed the foundation of the custom dataset needed to train the model.
  - Roboflow for Labeling: The images were labeled using Roboflow, which allowed for the precise identification of lettuce and bad plants, helping the model learn to differentiate between them.
- YOLOv8n Model (yolov8n.pt):

  - Model Training: The same methodology from a previous project (underwater circle detection) was applied here. Using the YOLOv8n model, a custom training process was set up to identify and detect lettuce and bad plants.
  - High Accuracy: The model achieved exceptional accuracy in detecting both lettuce and bad plants, ensuring its viability in real-world agricultural applications.
  - Config Files: The model parameters, such as the dataset path and class names, were defined in the config.yaml file, while the training process was managed by the custom_dataset_yolo_train.py script.

- Prediction System:

  - Script: The custom_data_predict.py file was used to make predictions, running on video files but also capable of processing real-time camera input.
  - Outputs: The trained model can identify and classify plants in live footage, making it suitable for use in unmanned agricultural vehicles or drones.

- Teknofest Unmanned Agriculture Vehicle Competition:

  - Participation: This project was submitted as part of Teknofest’s Unmanned Agriculture Vehicle competition, where the aim was to create autonomous systems capable of assisting in
  farming operations.
  - Objective: The primary task was to detect and differentiate lettuce plants from bad plants, helping farmers manage their crops more efficiently.

Training and Model Files:

After the training process, the resulting custom model can be found in the directory: runs\detect\yolov8n_custom\weights. This folder contains two important files:

  - best.pt: The best-performing model during training.
  - last.pt: The most recent version of the model after training.

Real-World Applications:
- Scalability: This system can be easily deployed on agricultural drones, robots, or autonomous tractors to automatically monitor crop health and identify problem areas in the field.
- Versatility: The model can be retrained or adapted to detect other plant species or agricultural conditions, making it a flexible solution for precision farming.
- Efficiency: By automating the process of plant identification, the system can help reduce labor costs, minimize herbicide use, and improve crop yields, making it highly practical in modern agriculture.

Modular and Practical:
- Field Adaptability: The system is designed to work in real-world conditions, with the ability to process live video footage from agricultural fields.
- Easy Deployment: Once trained, the model can be embedded into various agricultural vehicles or systems for real-time monitoring and plant management.
