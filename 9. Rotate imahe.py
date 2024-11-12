import cv2

image = cv2.imread("data1.jpg")

(h, w) = image.shape[:2]

center = (w // 2, h // 2)

angle = 225
scale = 1.0

rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
