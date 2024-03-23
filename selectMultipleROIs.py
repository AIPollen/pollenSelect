import cv2
import numpy as np

# Image path
img_path = "/Users/marcory/Documents/PollenOnderzoek/AIPollen/pollenSelect/pollenSelect/testImages/80euroAdapterSneeuwklokje.jpg"

# Read image
img_raw = cv2.imread(img_path)

# Select ROIs function
ROIs = cv2.selectROIs("Select Rois", img_raw)

# Print rectangle points of selected ROIs
print(ROIs)

# Crop selected ROIs from raw image

# Counter to save images with different names
crop_number = 0

# Loop over every bounding box saved in array "ROIs"
for rect in ROIs:
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]

    # Crop ROI from original image
    img_crop = img_raw[y1:y1+y2, x1:x1+x2]

    # Show cropped image
    cv2.imshow("crop"+str(crop_number), img_crop)

    # Save cropped image
    cv2.imwrite("crop"+str(crop_number)+".jpeg", img_crop)

    crop_number += 1

# Hold windows open
cv2.waitKey(0)

