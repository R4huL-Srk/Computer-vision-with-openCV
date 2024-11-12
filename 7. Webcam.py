import cv2


def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)  # 0 is usually the default webcam

    # Check if the webca`m opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Define playback speeds (in milliseconds)
    normal_speed = 33  # About 30 fps
    slow_motion_speed = 250  # About half the speed (slower)
    fast_motion_speed = 1  # About twice the speed (faster)

    # Start with normal playback speed
    current_speed = normal_speed

    print("Press 'n' for normal speed, 's' for slow motion, 'f' for fast motion, 'q' to quit.")

    while True:
        # Capture each frame
        ret, frame = cap.read()

        # If frame was not captured correctly, break the loop
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame
        cv2.imshow("Webcam Video", frame)

        # Wait for the specified delay and check for key presses
        key = cv2.waitKey(current_speed) & 0xFF

        # 'n' for normal speed
        if key == ord('n'):
            current_speed = normal_speed
            print("Switched to normal speed.")

        # 's' for slow motion
        elif key == ord('s'):
            current_speed = slow_motion_speed
            print("Switched to slow motion.")

        # 'f' for fast motion
        elif key == ord('f'):
            current_speed = fast_motion_speed
            print("Switched to fast motion.")

        # 'q' to quit
        elif key == ord('q'):
            print("Exiting...")
            break

    # Release the capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
