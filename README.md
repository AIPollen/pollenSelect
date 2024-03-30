# Select Pollen

Selects multiple pollen grains from one image for machine learning datasets.

## Requirements
Python 3.x
OpenCV-Python (pip install opencv-python) of (pip3 install opencv-contrib-python)
NumPy (pip install numpy)

## selectManualROIs

This Python script allows you to manually select Regions of Interest (ROIs) from a pollen image and save them as separate JPEG files.

### Overview
This Python script simplifies the process of creating a machine learning dataset of pollen grains. It allows you to efficiently select and crop multiple pollen from a single image, saving you time and effort.


### Instructions:

1. Clone or download this repository.
2. Run the script using python selectManualROIs.py (or your preferred Python interpreter).
3. A window will open to facilitate file selection. Navigate to your image and click "Open".
4. Draw rectangles around the pollen grains you want to extract in the displayed image window. Press Enter or space to confirm your selection.
5. Type escape if you finished the selection of pollen.
6. Enter a name for the pollen type when prompted.
7. Cropped images will be saved within the newly created directory with the pollen type name and a sequential number appended (e.g., pollen_type_0.jpeg).


## selectAutoRIOs
Offers a faster approach to make a dataset of pollen images based on detection of circles and save them as separate JPEG files. 

### Overview
This script employs the Hough Transform in OpenCV to automatically identify circular objects (likely pollen grains) in an image. 
Adjust the parameters for circle detection as needed, this minimized the amount of datacleaning afterwards. 
- pd (default = 1) higher -> faster but coarser search
- minDist (default = 20) higher -> reduces the change of finding closely spaced circles
- param1 (def 50) higher -> reduces noice, might miss faint circles
- param2 (def 30) higher might lead to less false positives
- minRadius (def 10) 
- maxRadius (def 100)
Crops as perfect square and resizes to 224x224 pixels (for TeachableMachine, adjust as needed)

### Instructions:

1. Clone or download this repository.
2. Run the script using python selectAutoROIs.py (or your preferred Python interpreter).
3. A window will open to facilitate file selection. Navigate to your image and click "Open".
4. Green circles give an indication of the selection.
5. Enter a name for the pollen type or pollen sample.
6. Cropped images will be saved within the newly created directory with the pollen type name and a sequential number appended (e.g., pollen_type_0.jpeg).
7. Adjust parameters if pollen are not selected or if too much noise is selected.

### Notes
This scripts uses OpenCV for image processing and Tkinter for the file dialog.
The script saves cropped images as JPEGs with 100% quality.

#### Credits
Inspired by: https://blog.electroica.com/select-roi-or-multiple-rois-bounding-box-in-opencv-python/

#### License
MIT