import cv2

image = cv2.imread('image.jpg')
clone = image.copy()

ref_point = []
cropping = False


def draw_rectangle(event, x, y, flags, param):
    global ref_point, cropping

    # When left mouse button is pressed, record the starting (x, y) coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cropping = False

        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_rectangle)

while True:
    # Display the image and wait for a key press
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # If 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()

    # If 'c' key is pressed, break from the loop and crop the region
    elif key == ord("c"):
        break

if len(ref_point) == 2:
    cropped_image = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
