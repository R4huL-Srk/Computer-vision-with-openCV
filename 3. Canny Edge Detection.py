import cv2

image = cv2.imread("data1.jpg", 0)

blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
