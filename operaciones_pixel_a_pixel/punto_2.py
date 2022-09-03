import cv2 as cv

cap = cv.VideoCapture(0)
ret, current_frame = cap.read()
previous_frame = current_frame

while cap.isOpened():
    current_frame_gray = cv.cvtColor(current_frame, cv.COLOR_BGR2GRAY)
    previous_frame_gray = cv.cvtColor(previous_frame, cv.COLOR_BGR2GRAY)

    frame_diff = cv.absdiff(current_frame_gray, previous_frame_gray)

    cv.imshow("frame diff", frame_diff)
    cv.imshow("current frame", current_frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

    previous_frame = current_frame.copy()
    ret, current_frame = cap.read()

cap.release()
cv.destroyAllWindows()
