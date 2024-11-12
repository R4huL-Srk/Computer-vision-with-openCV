import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

# Define Laplacian mask with positive center coefficient
laplacian_positive_mask = np.array([[0, 1, 0],
                                    [1, -4, 1],
                                    [0, 1, 0]])

# Apply convolution using the Laplacian mask
edges = cv2.filter2D(image, -1, laplacian_positive_mask)

# Subtract the edges from the original image to sharpen
sharpened_image = cv2.subtract(image, edges)

cv2.imshow("Original Image",image)
cv2.imshow("Sharpened Image",sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
