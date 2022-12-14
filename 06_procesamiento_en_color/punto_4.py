import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


def equalize_histogram_channels_3(image: np.ndarray, hls: bool = False) -> np.ndarray:
    channel_1, channel_2, channel_3 = cv.split(image)

    if hls:
        channel_2 = cv.equalizeHist(channel_2)
    else:
        channel_1 = cv.equalizeHist(channel_1)
        channel_2 = cv.equalizeHist(channel_2)
        channel_3 = cv.equalizeHist(channel_3)

    return cv.merge((channel_1, channel_2, channel_3))


def main() -> None:
    image_farolas: np.ndarray = cv.imread("Farolas-LED.jpg")
    image_farolas_hls: np.ndarray = cv.cvtColor(image_farolas, cv.COLOR_BGR2HLS)
    image_farolas_eq: np.ndarray = equalize_histogram_channels_3(image_farolas)
    image_farolas_hls_eq: np.ndarray = equalize_histogram_channels_3(
        image_farolas_hls, hls=True
    )

    rows, cols = 1, 3

    plt.subplot(rows, cols, 1)
    plt.imshow(cv.cvtColor(image_farolas, cv.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(rows, cols, 2)
    plt.imshow(cv.cvtColor(image_farolas_eq, cv.COLOR_BGR2RGB))
    plt.title("RBG equalized")
    plt.axis("off")

    plt.subplot(rows, cols, 3)
    plt.imshow(cv.cvtColor(image_farolas_hls_eq, cv.COLOR_HLS2RGB))
    plt.title("HLS equalized")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
