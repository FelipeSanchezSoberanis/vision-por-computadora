from typing import Callable as callable
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def get_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return np.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


def filter_in_frequency_by_radius(
    image: np.ndarray,
    r: list[int],
    comparator: callable[[int, int, int, int, list[int], int], bool | float],
    order: int = 0,
) -> np.ndarray:
    image_dft: np.ndarray = np.fft.fft2(image)
    dft_shift: np.ndarray = np.fft.fftshift(image_dft)

    height, width = dft_shift.shape
    x_center, y_center = int(height / 2), int(width / 2)

    for x in range(height):
        for y in range(width):
            dft_shift[x][y] *= comparator(x_center, y_center, x, y, r, order)

    idft_shift: np.ndarray = np.fft.ifftshift(dft_shift)
    image_filtered: np.ndarray = np.fft.ifft2(idft_shift)
    image_filtered = abs(image_filtered)

    return image_filtered


def filter_comparator_butterworth(
    x_center: int, y_center: int, x: int, y: int, r: list[int], n: int
) -> float:
    return 1 / (1 + (get_distance(x, y, x_center, y_center) / r[0]) ** (2 * n))


def band_pass_filter_comparator_ideal(
    x_center: int, y_center: int, x: int, y: int, r: list[int], _: int
) -> bool:
    return (
        get_distance(x, y, x_center, y_center) >= r[0]
        and get_distance(x, y, x_center, y_center) <= r[1]
    )


def band_reject_filter_comparator_ideal(
    x_center: int, y_center: int, x: int, y: int, r: list[int], _: int
) -> bool:
    return (
        get_distance(x, y, x_center, y_center) <= r[0]
        or get_distance(x, y, x_center, y_center) >= r[1]
    )


def high_pass_filter_comparator_ideal(
    x_center: int, y_center: int, x: int, y: int, r: list[int], _: int
) -> bool:
    return get_distance(x, y, x_center, y_center) >= r[0]


def low_pass_filter_comparator_ideal(
    x_center: int, y_center: int, x: int, y: int, r: list[int], _: int
) -> bool:
    return get_distance(x, y, x_center, y_center) <= r[0]


def main() -> None:
    image_original: np.ndarray = cv.imread("face.jpg", 0)
    image_low_pass: np.ndarray = filter_in_frequency_by_radius(
        image_original, [10], low_pass_filter_comparator_ideal
    )
    image_high_pass: np.ndarray = filter_in_frequency_by_radius(
        image_original, [100], high_pass_filter_comparator_ideal
    )
    image_band_pass: np.ndarray = filter_in_frequency_by_radius(
        image_original, [10, 30], band_pass_filter_comparator_ideal
    )
    image_band_reject: np.ndarray = filter_in_frequency_by_radius(
        image_original, [10, 30], band_reject_filter_comparator_ideal
    )
    image_butterworth: np.ndarray = filter_in_frequency_by_radius(
        image_original, [10], filter_comparator_butterworth, order=10
    )

    plt.subplot(3, 2, 1)
    plt.imshow(cv.cvtColor(image_original, cv.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(3, 2, 2)
    plt.imshow(image_high_pass, cmap="gray")
    plt.title("High pass")
    plt.axis("off")

    plt.subplot(3, 2, 3)
    plt.imshow(image_low_pass, cmap="gray")
    plt.title("Low pass")
    plt.axis("off")

    plt.subplot(3, 2, 4)
    plt.imshow(image_band_pass, cmap="gray")
    plt.title("Band pass")
    plt.axis("off")

    plt.subplot(3, 2, 5)
    plt.imshow(image_band_reject, cmap="gray")
    plt.title("Band reject")
    plt.axis("off")

    plt.subplot(3, 2, 5)
    plt.imshow(image_butterworth, cmap="gray")
    plt.title("Butterworth")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
