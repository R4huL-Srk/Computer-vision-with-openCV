import cv2
import numpy as np

image = cv2.imread("data1.jpg")

if image is None:
    print("Error loading image.")
    exit()

height, width = image.shape[:2]
source = np.float32([[1, 1],
                     [1000, 50],
                     [50, 1000]])

destination = np.float32([[10, 10],
                          [200, 50],
                          [50, 200]])

matrix = cv2.getAffineTransform(source, destination)

transformed_image = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
