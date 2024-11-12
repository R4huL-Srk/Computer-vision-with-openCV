import cv2
import numpy as np


def dlt(points1, points2):
    A = []
    for (x, y), (xp, yp) in zip(points1, points2):
        A.append([-x, -y, -1, 0, 0, 0, x * xp, y * xp, xp])
        A.append([0, 0, 0, -x, -y, -1, x * yp, y * yp, yp])
    A = np.array(A)

    _, _, Vt = np.linalg.svd(A)
    H = Vt[-1].reshape(3, 3)
    return H / H[2, 2]  


def get_correspondences(img1, img2):

    orb = cv2.ORB_create(500)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)


    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)


    matches = sorted(matches, key=lambda x: x.distance)

    points1 = np.array([kp1[m.queryIdx].pt for m in matches[:4]])
    points2 = np.array([kp2[m.trainIdx].pt for m in matches[:4]])

    return points1, points2

img1 = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE) 
img2 = cv2.imread('image2.png', cv2.IMREAD_GRAYSCALE) 

if img1 is None or img2 is None:
    raise FileNotFoundError("One of the images could not be loaded.")

points1, points2 = get_correspondences(img1, img2)

H = dlt(points1, points2)
print("Homography Matrix:\n", H)

height, width = img2.shape
warped_img = cv2.warpPerspective(img1, H, (width, height))

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Warped Image 1", warped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
