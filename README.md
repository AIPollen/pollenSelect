# Select Pollen

Selects multiple pollen grains from one image for machine learning datasets.

## Overview
This Python script simplifies the process of creating a machine learning dataset of pollen grains. It allows you to efficiently select and crop multiple pollen from a single image, saving you time and effort.

## Requirements
Python 3.x
OpenCV-Python (pip install opencv-python)
NumPy (pip install numpy)

## Image Selection
Replace "image.jpeg" in the script with the actual path and filename of your image containing the pollen grains.

## Pollen Selection
When running the script, the image will display in a window.
Use your mouse to click and drag a bounding box around each pollen grain you want to select for your dataset.
After selecting a pollen grain, press the Enter key to confirm your selection.
Multiple pollen grains can be selected in this way. The selected area will be cropped and saved in the imagefolder named crop0.jpeg etc.
Repeat selection and press the Enter key to select additional pollen grains.
To stop selecting pollen and exit the script, press the Esc key.

## Future Implementations
Automatic image loading: The script could be enhanced to automatically iterate through a directory of images, streamlining the selection process for multiple images.

## Credits
Inspired by: https://blog.electroica.com/select-roi-or-multiple-rois-bounding-box-in-opencv-python/

## License
MIT