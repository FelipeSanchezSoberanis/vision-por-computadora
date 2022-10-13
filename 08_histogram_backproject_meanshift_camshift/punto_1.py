import numpy as np
import cv2 as cv

p1: dict[str, int] = {"x": 891, "y": 1877}
p2: dict[str, int] = {"x": 1373, "y": 2413}

cap = cv.VideoCapture("wooden_star_video.mp4")
# take first frame of the video
ret, frame = cap.read()
frame = cv.rotate(frame, 1)
# setup initial location of window
x, y, w, h = (
    p1["x"],
    p1["x"],
    p2["x"] - p1["x"],
    p2["y"] - p1["y"],
)  # simply hardcoded the values
track_window = (x, y, w, h)
# set up the ROI for tracking
roi = frame[y : y + h, x : x + w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0.0, 60.0, 32.0)), np.array((180.0, 255.0, 255.0)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

cv.namedWindow("img2", cv.WINDOW_NORMAL)

while 1:
    ret, frame = cap.read()
    frame = cv.rotate(frame, 1)
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
        cv.imshow("img2", img2)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
