# =================================================================
# About:    This module does a variety of augmentations on the data 
# Author:   Oliver Clements
# Date:     12/5/2024
# =================================================================


# Library Imports
import cv2
import os
import shutil
import numpy as np
from file_mangement import get_dataset_images, get_dataset_labels
from definitions import *


def change_img_exposure(image: np.ndarray, exp_factor: float):
    """ Modifies the exposure of an image"""
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
    # Split HSV image into H, S, and V channels
    h, s, v = cv2.split(hsv_image)
    
    # Adjust exposure by scaling the V channel
    adjusted_v = np.clip(v * exp_factor, 0, 255).astype(np.uint8)
    
    # Merge adjusted V channel with original H and S channels
    adjusted_hsv_image = cv2.merge([h, s, adjusted_v])

     # Convert adjusted HSV image back to RGB color space
    modified_image = cv2.cvtColor(adjusted_hsv_image, cv2.COLOR_HSV2BGR)

    return modified_image


def exposure_handler(img: str, lbl: str) -> None:
    """ increases and decreases the brightness of images"""
    
    # Data Paths
    dataset_img_path = os.path.join(DATA_SET_IMG_DIR, img)
    dataset_lbl_path = os.path.join(DATA_SET_LAB_DIR, lbl)

    # Changing image exposures
    image = cv2.imread(dataset_img_path)
    bright_image = change_img_exposure(image, OVER_EXP_FACTOR)
    dark_image = change_img_exposure(image, UNDER_EXP_FACTOR)

    # Bright image and label rename
    bright_img_name = img.replace(".jpg", OVER_EXP_IMG_KEY)
    bright_lbl_name = lbl.replace(".txt", "overexp.txt")

    # Dark Image label and rename
    dark_img_name = img.replace(".jpg", UNDER_EXP_IMG_KEY)
    dark_lbl_name = lbl.replace(".txt", "underexp.txt")

    # Paths for bright image and label
    bright_img_path = os.path.join(AUGMENTED_IMG_DIR, bright_img_name)
    bright_lbl_path = os.path.join(AUGMENTED_LAB_DIR, bright_lbl_name)

    # Paths for dark image and label
    dark_img_path = os.path.join(AUGMENTED_IMG_DIR, dark_img_name)
    dark_lbl_path = os.path.join(AUGMENTED_LAB_DIR, dark_lbl_name)

    shutil.copy(dataset_lbl_path, bright_lbl_path)
    cv2.imwrite(bright_img_path, bright_image)
    print(f"{bright_img_name} was saved")

    shutil.copy(dataset_lbl_path, dark_lbl_path)
    cv2.imwrite(dark_img_path, dark_image)
    print(f"{dark_img_name} was saved")


def change_img_saturation(image: np.ndarray, saturation_factor: float):
    """ Modifies the saturation of an image"""
    # Convert image from BGR to HSV
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_img[:, :, 1] = hsv_img[:, :, 1] * saturation_factor

    # # Clip the values to the valid range [0, 255]
    # hsv_img[:, :, 1] = cv2.clip(hsv_img[:, :, 1], 0, 255)

    # Convert image back to BGR
    adjusted_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

    return adjusted_img


def saturation_handler(img: str, lbl: str) -> None:
    """ increases and decreases the brightness of images"""
    
    # Data Paths
    dataset_img_path = os.path.join(DATA_SET_IMG_DIR, img)
    dataset_lbl_path = os.path.join(DATA_SET_LAB_DIR, lbl)

    # Changing image exposures
    image = cv2.imread(dataset_img_path)
    over_sat_image = change_img_saturation(image, OVER_SAT_FACTOR)
    under_sat_image = change_img_exposure(image, UNDER_EXP_FACTOR)

    # Bright image and label rename
    over_sat_img_name = img.replace(".jpg", OVER_SAT_IMG_KEY)
    over_sat_lbl_name = lbl.replace(".txt", "oversat.txt")

    # # Dark Image label and rename
    under_sat_img_name = img.replace(".jpg", UNDER_SAT_IMG_KEY)
    under_sat_lbl_name = lbl.replace(".txt", "undersat.txt")

    # Paths for bright image and label
    over_sat_img_path = os.path.join(AUGMENTED_IMG_DIR, over_sat_img_name)
    over_sat_lbl_path = os.path.join(AUGMENTED_LAB_DIR, over_sat_lbl_name)

    # # Paths for dark image and label
    under_sat_img_path = os.path.join(AUGMENTED_IMG_DIR, under_sat_img_name)
    under_sat_lbl_path = os.path.join(AUGMENTED_LAB_DIR, under_sat_lbl_name)

    shutil.copy(dataset_lbl_path, over_sat_lbl_path)
    cv2.imwrite(over_sat_img_path, over_sat_image)
    print(f"{over_sat_img_name} was saved")

    shutil.copy(dataset_lbl_path, under_sat_lbl_path)
    cv2.imwrite(under_sat_img_path, under_sat_image)
    print(f"{under_sat_img_name} saved")
    

def augmentation_runner():
    """ Leader function that directs and controls the other augmentation functions"""
    img_list = get_dataset_images()
    lbl_list = get_dataset_labels()

    for i, img in enumerate(img_list):
        lbl = lbl_list[i]
        exposure_handler(img, lbl)
        saturation_handler(img, lbl)


augmentation_runner()

