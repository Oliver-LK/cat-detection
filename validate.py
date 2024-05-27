# =============================================
# About:    This module tests a CNN  network  
# Author:   Oliver Clements
# Date:     12/4/2024
# =============================================

from ultralytics import YOLO
from file_mangement import get_yolo_model, get_test_images


def test_model():
    """ Allows the user to test the pretrained model"""
    # Gets the models and the images
    model = get_yolo_model()
    test_images = get_test_images()

    # Load the desired model
    YoloModel = YOLO(model)
    
    results = YoloModel(source=test_images, imgsz=800, conf=0.5, save=True, iou=0)

    # Process and display the results
    for result in results:
        boxes = result.boxes        # Boxes object for bounding box outputs
        obb = result.obb            # Oriented boxes object for OBB outputs
        
        result.show()
       

test_model()