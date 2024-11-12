import cv2

# Load the pre-trained Haar Cascade for vehicle detection (you can download a car cascade xml file)
vehicle_cascade = cv2.CascadeClassifier('cars.xml')

# Open the video capture
video = cv2.VideoCapture('vehicle_video.mp4')

while True:
    # Read the video frame by frame
    ret, frame = video.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the frame
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw bounding boxes around detected vehicles
    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected vehicles
    cv2.imshow('Vehicle Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
video.release()
cv2.destroyAllWindows()
