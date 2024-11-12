import cv2

image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel kernel in the x and y directions
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in x direction
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in y direction

# Combine the Sobel x and y images to get the final edge-detected image
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
sobel_combined = cv2.convertScaleAbs(sobel_combined)

cv2.imshow('Boundary Detected image', sobel_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
