# =============================================
# About:    This module trains the CNN     
# Author:   Oliver Clements
# Date:     12/4/2024
# =============================================


# Library and module imports
import os
from ultralytics import YOLO
from file_mangement import get_user_wd
from definitions import CONFIG_FILE


def train():
    """ Trains the network"""

    dataset_folder = get_user_wd()

    data_config_path = dataset_folder + "/" + CONFIG_FILE

    # Load a model
    model = YOLO("yolov8n.pt")  # Init a yolo model

    # Use the model
    model.train(data=data_config_path, 
                epochs=75, 
                # device='mps',               
                imgsz=800, 
                plots=True,
                name=dataset_folder)  # train the model
    

train()
