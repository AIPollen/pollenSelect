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
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20,
                              param1=50, param2=30, minRadius=10, maxRadius=100)

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
      cv2.circle(img_circle, (x, y), r, (0, 255, 0), 2)  # Draw green circles

    # Show image with circles
    cv2.imshow("Image with Detected Circles", img_circle)

    # Ask for pollentype name (assuming circles represent pollen)
    pollentype_name = input("Enter the name of the pollentype: ")

    # Create a directory for the pollen type
    os.makedirs(pollentype_name, exist_ok=True)

    # Loop through detected circles and crop around them
    crop_number = 0
    for circle in circles:
      x, y, r = circle
      # Adjust padding as needed (increase for larger margins)
      x1, y1 = max(0, x - r - 10), max(0, y - r - 10)
      x2, y2 = min(img_raw.shape[1], x + r + 10), min(img_raw.shape[0], y + r + 10)

      # Crop ROI based on circle coordinates and padding
      img_crop = img_raw[y1:y2, x1:x2]

      # Show cropped image
      cv2.imshow("Crop" + str(crop_number), img_crop)

      # Save cropped image
      cv2.imwrite(os.path.join(pollentype_name, f"{pollentype_name}_{crop_number}.jpeg"), img_crop, [cv2.IMWRITE_JPEG_QUALITY, 100])

      crop_number += 1

    cv2.waitKey(0)

  else:
    print("No circles detected. Automatic selection failed.")

else:
  print("No image selected.")
