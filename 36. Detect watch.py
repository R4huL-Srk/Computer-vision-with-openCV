import cv2

image = cv2.imread('watch_image1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

watch_cascade = cv2.CascadeClassifier('watch-cascade.xml')

watches = watch_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

watch_count = len(watches)
print(f'Number of watches detected: {watch_count}')

cv2.imshow('Watch Detection', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
