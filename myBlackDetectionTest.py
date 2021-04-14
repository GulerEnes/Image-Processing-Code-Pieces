import cv2 as cv


def nothing(x):
    print(x)


cap = cv.VideoCapture(0)
cv.namedWindow('Video Capture Window')
cv.createTrackbar('x', 'Video Capture Window', 2, 255, nothing)
cv.createTrackbar('y', 'Video Capture Window', 2, 255, nothing)
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    x = cv.getTrackbarPos('x', 'Video Capture Window')
    y = cv.getTrackbarPos('y', 'Video Capture Window')
    #_, maskedFrame = cv.threshold(gray, x, 255, cv.THRESH_BINARY)
    #maskedFrame2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    maskedFrame3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 2*x+1, y)
    bilateral = cv.bilateralFilter(maskedFrame3, 9, 75, 75)
    if ret:

        cv.imshow('Video Capture Window', bilateral)

        if cv.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()





