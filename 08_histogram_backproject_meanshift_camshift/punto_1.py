import cv2 as cv
import numpy as np


def main() -> None:
    video: cv.VideoCapture = cv.VideoCapture("wooden_star_video.mp4")

    reference: cv.Mat = cv.imread("wooden_star_extracted.png")
    reference_hsv: cv.Mat = cv.cvtColor(reference, cv.COLOR_BGR2HSV)
    reference_mask: cv.Mat = cv.inRange(
        reference_hsv, np.array((0.0, 60.0, 32.0)), np.array((180.0, 255.0, 255.0))
    )
    reference_hist: cv.Mat = cv.calcHist(
        [reference_hsv], [0], reference_mask, [180], [0, 180]
    )
    reference_hist = cv.normalize(
        reference_hist, reference_hist, 0, 255, cv.NORM_MINMAX
    )

    termination_criteria = (
        cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,
        10,
        1,
    )

    cv.namedWindow("video", cv.WINDOW_NORMAL)

    track_window: None | tuple[int, int, int, int] = None

    while True:
        frame: cv.Mat = video.read()[1]
        frame = cv.rotate(frame, 1)

        if not track_window:
            track_window = (770, 1730, 600, 600)

        frame_hsv: cv.Mat = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        frame_dst: cv.Mat = cv.calcBackProject(
            [frame_hsv], [0], reference_hist, [0, 180], 1
        )

        track_window = cv.meanShift(frame_dst, track_window, termination_criteria)[1]

        if track_window:
            x, y, w, h = track_window
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)

            cv.imshow("video", frame)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
