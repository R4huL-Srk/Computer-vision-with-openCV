import cv2
import numpy as np
image = cv2.imread("data1.jpg")
source_points = np.float32([
    [50, 50],     
    [200, 50],    
    [50, 200],   
    [200, 200]    
])

destination_points = np.float32([
    [5, 50],     
    [150, 25],    
    [50, 125],   
    [125, 150]    
])

matrix = cv2.getPerspectiveTransform(source_points, destination_points)

transformed_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))
cv2.imshow('Perspective Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
