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

  # Function to detect circles using Hough Transform
  def detect_circles(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)  # Apply blur for noise reduction

    # Set parameters for circle detection (adjust as needed)
    # pd (default = 1) higher -> faster but coarser search
    # minDist (default = 20) higher -> reduces the change of finding closely spaced circles
    # param1 (def 50) higher -> reduces noice, might miss faint circles
    # param2 (def 30) higher might lead to less false positives
    # minRadius (def 10) 
    # maxRadius (def 100)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20,
                              param1=52, param2=30, minRadius=25, maxRadius=100)

    # Check if circles are found
    if circles is not None:
      circles = np.uint16(np.around(circles))[0]  # Convert circles to integers
      return circles
    else:
      print("No circles detected in the image.")
      return None

  # Detect circles
  circles = detect_circles(img_raw.copy())

  # Continue if circles are found
  if circles is not None:
    # Create a copy for drawing circles
    img_circle = img_raw.copy()

    # Draw detected circles on the image
    for circle in circles:
      x, y, r = circle
      cv2.circle(img_circle, (x, y), r, (255, 0, 0), 2)  # Draw green circles

    # Show image with circles
    cv2.imshow("Image with Detected Circles", img_circle)

    # Ask for pollentype name (assuming circles represent pollen)
    pollentype_name = input("Enter the name of the pollentype: ")

    # Create a directory for the pollen type
    os.makedirs(pollentype_name, exist_ok=True)

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
    
    cv2.waitKey(0)

  else:
    print("No circles detected. Automatic selection failed.")

else:
  print("No image selected.")