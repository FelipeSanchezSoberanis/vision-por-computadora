import cv2 as cv
import numpy as np
import os

FPS: int = 60
RADIUS_MARGIN: float = 0.05


class Coin:
    def __init__(self, value: float, diameter: int) -> None:
        self.value: float = value
        self.radius: int = int(diameter / 2)


def count_circles(circles) -> dict[Coin, int]:
    coins: dict[Coin, int] = {
        Coin(5, 80): 0,
        Coin(2, 70): 0,
        Coin(1, 65): 0,
        Coin(0.2, 47): 0,
    }

    min_margin: float = 1 - RADIUS_MARGIN
    max_margin: float = 1 + RADIUS_MARGIN

    for i in circles[0, :]:
        radius = i[2]

        for coin in coins:
            if min_margin * coin.radius < radius < max_margin * coin.radius:
                coins[coin] += 1

    return coins


def get_circles(image: cv.Mat):
    image_gray: cv.Mat = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_gray = cv.medianBlur(image_gray, 9)

    return cv.HoughCircles(
        image=image_gray,
        method=cv.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=300,
        param2=40,
        minRadius=20,
        maxRadius=45,
    )


def draw_circles(image: cv.Mat, circles) -> None:
    for i in circles[0, :]:
        center = (np.uint16(i[0]), np.uint16(i[1]))
        radius = np.uint16(i[2])

        cv.circle(image, center, radius, (255, 0, 255), 3)


def main() -> None:
    video = cv.VideoCapture("video_coins.mp4")

    while True:
        frame = video.read()[1]

        circles = get_circles(frame)
        draw_circles(frame, circles)
        coins: dict[Coin, int] = count_circles(circles)

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
