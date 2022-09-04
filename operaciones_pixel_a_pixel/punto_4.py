import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def read_image() -> np.ndarray:
    return cv.imread("LegosGrises 1.jpg")


def plot_histogram(image: np.ndarray) -> None:
    histogram = cv.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(histogram)


def apply_threshold(image: np.ndarray, min: int, max: int) -> np.ndarray:
    _, image_thresh = cv.threshold(image, min, max, cv.THRESH_BINARY)
    return image_thresh


def main() -> None:
    image = read_image()
    plot_histogram(image)
    image_thresh = apply_threshold(image, 100, 130)

    cv.imshow("image", image_thresh)
    plt.show()

    while True:
        k = cv.waitKey(0) & 0xFF
        if k == 27:
            cv.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
