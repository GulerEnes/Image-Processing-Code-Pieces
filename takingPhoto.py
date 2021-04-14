import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
while True:
    _, frame = cam.read()
    k = cv2.waitKey(1)
    if k % 256 == 27:  # ESC pressed escaping
        break
    elif k % 256 == 32:  # SPACE pressed taking photo
        cv2.imwrite("cvImage.png", frame)
        break
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame = cv2.putText(frame, "Press 'Space' to take photo", (10, 20), font, .5, (0, 0, 255), 1, cv2.LINE_AA)
    frame = cv2.putText(frame, "ESC to exit", (10, 40), font, .5, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imshow("test", frame)

cam.release()
cv2.destroyAllWindows()
