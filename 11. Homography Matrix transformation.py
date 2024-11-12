import cv2
import numpy as np

src_points = np.float32([[100, 100],
                       [200, 100],
                       [200, 200],
                       [100, 200]])

dst_points = np.float32([[80, 120],
                         [220, 80],
                         [220, 220],
                         [80, 200]])

H, status = cv2.findHomography(src_points, dst_points)

print("Homography matrix:\n", H)

src_image = cv2.imread("data1.jpg")

height, width = src_image.shape[:2]

dst_image = cv2.warpPerspective(src_image, H, (width, height))

cv2.imshow("Transformed Image", dst_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
