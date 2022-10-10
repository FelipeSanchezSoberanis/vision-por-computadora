import cv2 as cv
import numpy as np


FPS: int = 60


def preprocess_frame(frame: cv.Mat) -> cv.Mat:
    frame_preprocessed: cv.Mat = frame.copy()

    frame_preprocessed = cv.cvtColor(frame_preprocessed, cv.COLOR_BGR2GRAY)
    frame_preprocessed = cv.GaussianBlur(frame_preprocessed, (7, 7), 0)

    return frame_preprocessed


def get_connected_components(frame: cv.Mat):
    return cv.connectedComponentsWithStats(frame, 4, cv.CV_32S)


def main() -> None:
    video = cv.VideoCapture("video_coins.mp4")

    while True:
        frame: cv.Mat = video.read()[1]

        frame_preprocessed: cv.Mat = preprocess_frame(frame)
        (total_labels, label_ids, values, centroid) = get_connected_components(
            frame_preprocessed
        )

        for i in range(total_labels):
            cv.circle(frame, np.uint16(centroid[i]), 5, (255, 0, 255))

        cv.imshow("video", frame)

        if cv.waitKey(int(1 / FPS * 1000)) & 0xFF == ord("q"):
            break

    video.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
