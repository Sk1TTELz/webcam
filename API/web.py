import cv2

def capture_camera():
    try:
        capture = cv2.VideoCapture(0)

        while True:
            ret, frame = capture.read()
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
        capture.release()
    except Exception as e:
        print("Failed to connect camera", e)
capture_camera()
