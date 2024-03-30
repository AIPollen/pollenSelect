import cv2
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# ... (rest of the code remains the same)

# Loop through detected circles and select 299x299px regions
crop_number = 0
for circle in circles:
    x, y, r = circle

    # Calculate region boundaries for 299x299px selection
    x1 = x - 149
    y1 = y - 149
    x2 = x + 149
    y2 = y + 149

    # Ensure coordinates stay within image bounds
    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(img_raw.shape[1], x2)
    y2 = min(img_raw.shape[0], y2)

    # Select the 299x299px region without cropping or resizing
    img_region = img_raw[y1:y2, x1:x2]

    # Show selected region
    cv2.imshow("Region" + str(crop_number), img_region)

    # Save selected region
    cv2.imwrite(os.path.join(pollentype_name, f"{pollentype_name}_{crop_number}.jpeg"), img_region, [cv2.IMWRITE_JPEG_QUALITY, 100])

    crop_number += 1

# ... (rest of the code remains the same)
