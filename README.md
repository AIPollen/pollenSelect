# Select Pollen

Selects multiple pollen grains from one image for machine learning datasets.

## selectManualROIs

This Python script allows you to select Regions of Interest (ROIs) from a pollen image and save them as separate JPEG files.

### Overview
This Python script simplifies the process of creating a machine learning dataset of pollen grains. It allows you to efficiently select and crop multiple pollen from a single image, saving you time and effort.

### Requirements
Python 3.x
OpenCV-Python (pip install opencv-python)
NumPy (pip install numpy)

### Instructions:

1. Clone or download this repository.
2. Run the script using python selectManualROIs.py (or your preferred Python interpreter).
3. A window will open to facilitate file selection. Navigate to your image and click "Open".
4. Draw rectangles around the pollen grains you want to extract in the displayed image window. Press Enter or space to confirm your selection.
5. Type escape if you finished the selection of pollen.
6. Enter a name for the pollen type when prompted.
7. Cropped images will be saved within the newly created directory with the pollen type name and a sequential number appended (e.g., pollen_type_0.jpeg).

### Notes
This script uses OpenCV for image processing and Tkinter for the file dialog.
The script saves cropped images as JPEGs with 100% quality.

## selectAutoRIOs
Select pollen based on shape and diameter. 

#### Credits
Inspired by: https://blog.electroica.com/select-roi-or-multiple-rois-bounding-box-in-opencv-python/

#### License
MIT