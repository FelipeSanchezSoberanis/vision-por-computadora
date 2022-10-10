import cv2 as cv
import os
import numpy as np


FPS: int = 60


class Coin:
    def __init__(self, value: float, diameter: int) -> None:
        self.value: float = value
        self.radius: int = int(diameter / 2)


def get_eccentricity(width: float, height: float) -> float:
    return width / height


def get_r_from_circle_area(area: float) -> float:
    return np.sqrt(area / np.pi)


def preprocess_frame(frame: cv.Mat) -> cv.Mat:
    frame_preprocessed: cv.Mat = frame.copy()

    frame_preprocessed = cv.cvtColor(frame_preprocessed, cv.COLOR_BGR2GRAY)
    frame_preprocessed = cv.GaussianBlur(frame_preprocessed, (5, 5), 0)
    _, frame_preprocessed = cv.threshold(
        frame_preprocessed, 150, 255, cv.THRESH_BINARY_INV
    )

    #  cv.imshow("preprocess", frame_preprocessed)

    return frame_preprocessed


def main() -> None:
    video = cv.VideoCapture("video_coins.mp4")

    while True:
        coins: dict[Coin, int] = {
            Coin(5, 80): 0,
            Coin(2, 70): 0,
            Coin(1, 60): 0,
            Coin(0.2, 47): 0,
        }

        frame: cv.Mat = video.read()[1]

        frame_preprocessed: cv.Mat = preprocess_frame(frame)
        (total_labels, _, values, centroids) = cv.connectedComponentsWithStats(
            frame_preprocessed, 4, cv.CV_32S
        )

        for i in range(total_labels):
            r: np.uint16 = np.uint16(get_r_from_circle_area(values[i, cv.CC_STAT_AREA]))

            if (
                0.9
                < get_eccentricity(
                    values[i, cv.CC_STAT_WIDTH], values[i, cv.CC_STAT_HEIGHT]
                )
                < 1.1
                and r > 20
            ):
                cv.circle(
                    frame,
                    (np.uint16(centroids[i])),
                    r,
                    (0, 255, 0),
                    thickness=2,
                )

                for coin, count in coins.items():
                    if coin.radius * 0.9 < r < coin.radius * 1.1:
                        coins[coin] += 1
                        break

                os.system("clear")
                for coin, count in coins.items():
                    print("Coin: {}. Count: {}".format(coin.value, count))

        cv.imshow("video", frame)

        if cv.waitKey(int(1 / FPS * 1000)) & 0xFF == ord("q"):
            break

    video.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
