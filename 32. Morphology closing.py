import cv2
import numpy as np

# Load an image in grayscale mode
image = cv2.imread('data1.jpg', 0)  # replace 'image_path' with the actual path to your image

# Apply a binary threshold to the image (optional for clear visualization)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define the kernel for the morphological operation
kernel = np.ones((5, 5), np.uint8)

# Apply the closing operation
closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Closing Technique", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
