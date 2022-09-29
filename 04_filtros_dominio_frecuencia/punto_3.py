import cv2 as cv
import matplotlib.pyplot as plt
from typing import Callable as callable
import numpy as np
from punto_2 import (
    filter_comparator_ideal,
    filter_comparator_gaussian,
    filter_comparator_butterworth,
)


def high_pass_filter(
    image: np.ndarray,
    r: int,
    comparator: callable[[int, int, int, int, int, int], bool | float],
    order: int = 0,
) -> np.ndarray:
    image_dft: np.ndarray = np.fft.fft2(image)
    dft_shift: np.ndarray = np.fft.fftshift(image_dft)

    height, width = dft_shift.shape
    x_center, y_center = int(height / 2), int(width / 2)

    for x in range(height):
        for y in range(width):
            dft_shift[x][y] *= 1 - comparator(x_center, y_center, x, y, r, order)

    idft_shift: np.ndarray = np.fft.ifftshift(dft_shift)
    image_filtered: np.ndarray = np.fft.ifft2(idft_shift)
    image_filtered = abs(image_filtered)

    return image_filtered


def main() -> None:
    image_original: np.ndarray = cv.imread("test-letter.png", 0)
    image_ideal: np.ndarray = high_pass_filter(
        image_original, 30, filter_comparator_ideal
    )
    image_butterworth: np.ndarray = high_pass_filter(
        image_original, 30, filter_comparator_butterworth, order=10
    )
    image_gaussian: np.ndarray = high_pass_filter(
        image_original, 30, filter_comparator_gaussian
    )

    plt.subplot(2, 2, 1)
    plt.imshow(image_original, cmap="gray")

    plt.subplot(2, 2, 2)
    plt.imshow(image_ideal, cmap="gray")

    plt.subplot(2, 2, 3)
    plt.imshow(image_butterworth, cmap="gray")

    plt.subplot(2, 2, 4)
    plt.imshow(image_gaussian, cmap="gray")

    plt.show()


if __name__ == "__main__":
    main()
