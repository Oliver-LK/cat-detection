# =================================================================
# About:    This module uploads the data to roboflow
#           Primarily used to upload the augmented data
# Author:   Oliver Clements
# Date:     13/5/2024
# =================================================================

import glob
from roboflow import Roboflow
from definitions import AUGMENTED_IMG_DIR, AUGMENTED_LAB_DIR

def upload_data_to_roboflow():
    """ Uploads data and annotation to roboflow"""
    # Initialize Roboflow client
    rf = Roboflow(api_key="Your Key Goes Here")

    file_extension_type = ".jpg"

    # Get the upload project from Roboflow workspace
    project = rf.workspace("Workspace").project("Project")

    # Upload images
    image_glob = glob.glob(AUGMENTED_IMG_DIR + '/*' + file_extension_type)
    for image_path in image_glob:
        try:
            annotation_path = image_path.replace("/images/", "/labels/").replace(".jpg", ".txt")
            print(image_path)
            print(f"{annotation_path}\n")
            print(project.single_upload(
                image_path=image_path,
                annotation_path=annotation_path,
                num_retry_uploads=3,
                tag_names=['Maple', 'Tabby'],
            
            ))
        except KeyboardInterrupt:
            break
    # Upload the label map
    print(project.single_upload("label_map.labels", num_retry_uploads=3))

upload_data_to_roboflow()