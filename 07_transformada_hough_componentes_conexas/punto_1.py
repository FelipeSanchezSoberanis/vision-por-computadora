import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    image: cv.Mat = cv.imread("coins.png", 0)
    image_blur: cv.Mat = cv.medianBlur(image, 101)
    circles = cv.HoughCircles(
        image=image_blur,
        method=cv.HOUGH_GRADIENT,
        dp=1,
        minDist=800,
        param1=150,
        param2=10,
        minRadius=int(915 / 2 * 0.75),
        maxRadius=int(915 / 2 * 2),
    )

    image = cv.cvtColor(image, cv.COLOR_GRAY2BGR)

    for circle in circles[0, :]:
        cv.circle(
            img=image,
            center=(int(circle[0]), int(circle[1])),
            radius=int(circle[2]),
            color=(0, 255, 0),
            thickness=10,
        )

    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.show()


if __name__ == "__main__":
    main()
