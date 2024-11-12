import cv2
import numpy as np

# Load image
image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

# Define Laplacian mask with diagonal neighbors
laplacian_extended_mask = np.array([[-1, -1, -1],
                                    [-1, 9, -1],
                                    [-1, -1, -1]])

# Apply convolution using the Laplacian mask with diagonal neighbors
sharpened_image = cv2.filter2D(image, -1, laplacian_extended_mask)

cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image",sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
