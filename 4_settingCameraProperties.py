import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# to set some properties
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)  #first parameter is what you want to change, second is value
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Video Capture Window', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

