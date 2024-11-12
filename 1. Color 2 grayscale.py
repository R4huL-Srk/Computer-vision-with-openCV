import cv2

image = cv2.imread("data1.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Gray image ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""from PIL import Image
image = Image.open("data1.jpg")
gray_image = image.convert("L")
gray_image.save("output1.jpg")
gray_image.show()"""
