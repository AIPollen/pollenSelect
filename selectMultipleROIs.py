import cv2
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Create a Tkinter window to access file dialogs
root = Tk()
root.withdraw()  # Hide the main window

# Prompt the user to select an image file
img_path = askopenfilename(title="Select an image")

# Check if a file was selected
if img_path:
    img_raw = cv2.imread(img_path)

    # Select ROIs function
    ROIs = cv2.selectROIs("Select Rois", img_raw)

    # Ask for pollentype name
    pollentype_name = input("Enter the name of the pollentype: ")

    # Create a directory for the pollen type
    os.makedirs(pollentype_name, exist_ok=True)  # Create directory if it doesn't exist, otherwise do nothing

    # Print rectangle points of selected ROIs
    print(ROIs)

    # Crop selected ROIs from raw image
    crop_number = 0

    for rect in ROIs:
        x1, y1, x2, y2 = rect

        # Crop ROI from original image
        img_crop = img_raw[y1:y1+y2, x1:x1+x2]

        # Show cropped image
        cv2.imshow("crop"+str(crop_number), img_crop)

        # Save cropped image in the pollentype directory
        cv2.imwrite(os.path.join(pollentype_name, f"{pollentype_name}_{crop_number}.jpeg"), img_crop)

        crop_number += 1

    cv2.waitKey(0)

else:
    print("No image selected.")

