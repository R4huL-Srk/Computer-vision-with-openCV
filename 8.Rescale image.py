import cv2

image = cv2.imread("data1.jpg")

scale_percent = 65
height, width = image.shape[:2]
width = int(width * scale_percent / 100)
height = int(height * scale_percent / 100)
dimensions = (width, height)

resized_image = cv2.resize(image, dimensions)

cv2.imshow("data1.jpg", image)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
