import cv2
import matplotlib.pyplot as plt

image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not load image.")
    exit()

blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)

edges = cv2.Canny(blurred_image, 100, 200)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Canny Edges')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()
