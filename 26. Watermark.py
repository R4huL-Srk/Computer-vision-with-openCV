import cv2
import numpy as np

image = cv2.imread('data1.jpg')
watermark = cv2.imread('watermark.png', cv2.IMREAD_UNCHANGED)  # Make sure the watermark has transparency

# Resize watermark to fit on the original image if necessary
scale = 0.3
watermark = cv2.resize(watermark, (0, 0), fx=scale, fy=scale)

# Get dimensions of the watermark and the original image
(wH, wW) = watermark.shape[:2]
(h, w) = image.shape[:2]

# Position the watermark at the bottom-right corner
x = w - wW - 10  # 10 pixels from the right
y = h - wH - 10  # 10 pixels from the bottom

# Separate the color and alpha channels of the watermark
if watermark.shape[2] == 4:
    watermark_bgr = watermark[:, :, :3]
    alpha_channel = watermark[:, :, 3] / 255.0  # Normalize alpha channel
else:
    watermark_bgr = watermark
    alpha_channel = np.ones((wH, wW))  # No alpha, treat as fully opaque

# Overlay watermark on the original image
for c in range(3):  # Iterate over each color channel
    image[y:y + wH, x:x + wW, c] = (alpha_channel * watermark_bgr[:, :, c] +
                                    (1 - alpha_channel) * image[y:y + wH, x:x + wW, c])

cv2.imshow("Watermarked image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
