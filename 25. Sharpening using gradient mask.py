import cv2
import numpy as np

# Load the original image
image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

# Compute the gradients using Sobel operator
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in x direction
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in y direction

# Calculate the gradient magnitude (edge strength)
gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)

# Convert gradient magnitude to a suitable range for display and combination
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
gradient_magnitude = gradient_magnitude.astype(np.uint8)

# Add the gradient mask to the original image to enhance edges (sharpening)
sharpened_image = cv2.addWeighted(image, 1, gradient_magnitude, 1, 0)

cv2.imshow("Original Image",image)
cv2.imshow("Sharpened image",sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
