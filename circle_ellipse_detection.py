import numpy as np
import cv2 as cv
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage import img_as_float

def nothing(x):
    print(x)


cap = cv.VideoCapture(0)
cv.namedWindow('output')
cv.createTrackbar('p1', 'output', 100, 255, nothing)
cv.createTrackbar('p2', 'output', 50, 255, nothing)
cv.createTrackbar('minR', 'output', 0, 255, nothing)
cv.createTrackbar('maxR', 'output', 0, 255, nothing)

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)

    p1 = cv.getTrackbarPos('p1', 'output')
    p2 = cv.getTrackbarPos('p2', 'output')
    minR = cv.getTrackbarPos('minR', 'output')
    maxR = cv.getTrackbarPos('maxR', 'output')

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=minR, maxRadius=maxR)

    rgb_frame = img_as_float(gray)
    edges = canny(rgb_frame, sigma=2.0, low_threshold=0.55, high_threshold=0.8)
    ellipses = hough_ellipse(edges, accuracy=20, threshold=150, min_size=0, max_size=500)
    print(ellipses)
    try:
        detected_circles = np.uint16(np.around(circles))
        for (x, y, r) in detected_circles[0, :]:
            cv.circle(frame, (x, y), r, (0, 255, 0), 3)
            cv.circle(frame, (x, y), 2, (0, 0, 255), 3)

        best = list(ellipses[-1])
        print(best)
        y, x, a, b = [int(round(x)) for x in best[1:5]]
        print("test")
        orientation = best[5]
        print(x)
        if x is not None:
            cv.ellipse(frame, (x, y), (a, b), 0, 0, 360, (0, 0, 255), 3)
            cv.circle(frame, (x, y), 2, (255, 0, 0), 3)

    except:

        cv.imshow('output', frame)
    if ret:
        cv.imshow('output', frame)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()


