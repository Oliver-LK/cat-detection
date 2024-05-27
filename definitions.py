# =================================================================
# About:    Definitions files
#           
# Author:   Oliver Clements
# Date:     13/5/2024
# =================================================================


CONFIG_FILE = "data.yaml"

ALLOWED_IMG_TYPES = [".png", ".jpeg", ".jpg"]

# Dataset
DATA_SET_IMG_DIR = "./dataset_images/images"
DATA_SET_LAB_DIR = "./dataset_images/labels"

# Augmented
AUGMENTED_IMG_DIR = "./augmented_images/images"
AUGMENTED_LAB_DIR = "./augmented_images/labels"


#  ====== Augmentations ======
# Exposure
OVER_EXP_FACTOR = 1.25
UNDER_EXP_FACTOR = 0.8
OVER_EXP_IMG_KEY = "overexp.jpg"
UNDER_EXP_IMG_KEY = "underexp.jpg"

# Saturation
OVER_SAT_FACTOR = 1.25
UNDER_SAT_FACTOR = 0.7
OVER_SAT_IMG_KEY = "oversat.jpg"
UNDER_SAT_IMG_KEY = "undersat.jpg"