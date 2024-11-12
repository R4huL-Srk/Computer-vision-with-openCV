import cv2
import numpy as np

# Load an image in grayscale mode
image = cv2.imread('data1.jpg', 0)  # replace 'image_path' with the actual path to your image

# Define the kernel for the morphological operation
kernel = np.ones((15, 15), np.uint8)  # Larger kernel for more prominent features

# Apply the Top Hat operation
top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Top Hat Image",top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
