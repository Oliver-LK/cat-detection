# =================================================
# About:    This module handles the file management 
# Author:   Oliver Clements
# Date:     12/4/2024
# 
# 
# =================================================

# Library imports
import os

# Add any folders to be excluded when searching for dataset folders
FOLDER_EXCLUSIONS = ["runs", "archive001", "sampple_data", "__pycache__", "COSC428_import", ".ipynb_checkpoints"]      # All folders in cwd that are not imported datasets

def cwd_folders() -> list:
    """ Returns a list of all of all folders in the cwd"""
    current_directory = os.getcwd()

    # List all folders in the current directory
    folders = [folder for folder in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, folder))]
    return folders


def get_data_set_folders():
    """ Returns a list of all data set folders"""
    folders = cwd_folders()
    dataset_folders = [folder for folder in folders if folder not in FOLDER_EXCLUSIONS]

    return dataset_folders


def print_dataset_folders(dataset_folders):
    """ Prints the dataset folders"""

    print("Dataset folders found")
    for folder in dataset_folders:
        print(f" - {folder}")


def get_user_wd():
    """ """
    dataset_folders = get_data_set_folders()

    print_dataset_folders(dataset_folders)

    while True:
        user_choice = str(input("Please type the folder you would like to use for the training model: "))

        if user_choice not in dataset_folders:
            print("That is not a valid folder\nPlease see above for the options")

        elif user_choice in dataset_folders:
            print(f"\nSelected folder {user_choice}")
            return user_choice
        
        # return f"error"


def get_desired_files(subdir: str, file_type: str) -> list:
    """ Returns a list of all desired files in a dir"""
    current_directory = os.getcwd()
    model_path =  current_directory + subdir

    filtered_files = [os.path.basename(file) for file in os.listdir(model_path) if os.path.isfile(os.path.join(model_path, file)) and file.endswith(file_type)]

    return filtered_files


def print_models(model_list) -> None:
    """ prints the model list"""
    print("Here is the list of available models")
    for model in model_list:
        print(f" - {model}")


def get_yolo_model() -> str:
    """ Lets the user choose from a list of yolo models"""
    current_directory = os.getcwd()
    model_list = get_desired_files("/models", ".pt")
    print_models(model_list)
    
    while True:
        user_choice = str(input("Please type the model you would like to use: "))

        if user_choice not in model_list:
            print("That is not a valid model.\nHere is a list of the available models")
            print_models(model_list)

        elif user_choice in model_list:
            print(f"\n{user_choice} was selected")
            return f"{current_directory}/models/{user_choice}"


# Currently only configured for JPEGS or JPGS. Others can also be added
def get_test_images() -> list:
    """ Gets the test images"""
    final_image_list = list()
    images_list1 = get_desired_files("/test_images", ".jpeg")
    images_list2 = get_desired_files("/test_images", ".jpg")
    images_list3 = get_desired_files("/test_images", ".JPG")

    for image in images_list1:
        final_image_list.append("./test_images/" + image)

    for image in images_list2:
        final_image_list.append("./test_images/" + image)

    for image in images_list3:
        final_image_list.append("./test_images/" + image)

    return final_image_list

def get_dataset_images() -> list:
    """ Gets a list of all the image names and directories that are used in the data set"""
    image_list = get_desired_files("/dataset_images/images", ".jpg")
    
    return image_list


def get_dataset_labels() -> list:
    """ Gets a list of all the image names and directories that are used in the data set"""
    label_list = get_desired_files("/dataset_images/labels", ".txt")
    
    return label_list

