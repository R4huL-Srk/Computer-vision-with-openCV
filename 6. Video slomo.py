import cv2


def play_video_with_speed_control(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    normal_speed = 30
    slow_motion_speed = 250
    fast_motion_speed = 1

    current_speed = normal_speed

    print("Press 'n' for normal speed, 's' for slow motion, 'f' for fast motion, 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("End of video reached or failed to read the frame.")
            break

        cv2.imshow("Video Playback", frame)

        key = cv2.waitKey(current_speed) & 0xFF

        if key == ord('n'):
            current_speed = normal_speed
            print("Switched to normal speed.")

        elif key == ord('s'):
            current_speed = slow_motion_speed
            print("Switched to slow motion.")

        elif key == ord('f'):
            current_speed = fast_motion_speed
            print("Switched to fast motion.")

        elif key == ord('q'):
            print("Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()


video_path = "videoData.mp4"
play_video_with_speed_control(video_path)
