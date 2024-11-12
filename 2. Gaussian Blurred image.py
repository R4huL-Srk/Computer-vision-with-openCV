import cv2

image = cv2.imread("data1.jpg")

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imwrite("output2.jpg", blurred_image)

cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
