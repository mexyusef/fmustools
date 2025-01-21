import os
import sys
import random
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt

# pip install tensorflow keras numpy pillow matplotlib opencv-python-headless
# wget https://github.com/matterport/Mask_RCNN/releases/download/v2.1/mask_rcnn_coco.h5

def remove_background():
    # Import Mask R-CNN
    sys.path.append(os.path.abspath("./Mask_RCNN"))
    from mrcnn import utils
    from mrcnn.config import Config
    from mrcnn.model import MaskRCNN

    # Configuration for the model
    class InferenceConfig(Config):
        # Set batch size to 1 since we'll be processing single images
        GPU_COUNT = 1
        IMAGES_PER_GPU = 1

    config = InferenceConfig()
    config.display()

    # Load the pre-trained model
    model = MaskRCNN(mode="inference", model_dir="./", config=config)
    model.load_weights("mask_rcnn_coco.h5", by_name=True)

    # Load the input image
    image = cv2.imread("input.jpg")

    # Run the model to detect objects and masks
    results = model.detect([image], verbose=1)

    # Get the mask for the first object in the image
    mask = results[0]['masks'][:,:,0]

    # Apply the mask to the image
    masked_image = image.copy()
    masked_image[mask == 0] = 0

    # Save the output image
    cv2.imwrite("output.jpg", masked_image)
