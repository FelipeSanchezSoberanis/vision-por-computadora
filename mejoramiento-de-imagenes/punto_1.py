import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from numpy._typing import NDArray


def calculate_histogram(
    image: np.ndarray,
) -> tuple[NDArray[np.uint8], NDArray[np.float64]]:
    width, height = image.shape

    x = np.linspace(0, 255, num=256, dtype=np.uint8)
    y = np.zeros(256)

    for w in range(width):
        for h in range(height):
            v = image[w, h]
            y[v] = y[v] + 1

    return x, y


def equalize_image(image: np.ndarray) -> NDArray[np.float64]:
    width, height = image.shape
    _, y = calculate_histogram(image)

    k = 255 / (width * height)
    sum = 0

    equalized_image = np.zeros(image.shape, image.dtype)

    for w in range(width):
        for h in range(height):
            for s in range(image[w, h]):
                sum += y[s]
            equalized_image[w, h] = k * sum
            sum = 0

    return equalized_image


def main() -> None:
    image_original = cv.imread(
        "Fig0309(a)(washed_out_aerial_image).tif", cv.IMREAD_GRAYSCALE
    )
    image_equalized = equalize_image(image_original)

    x_original, y_original = calculate_histogram(image_original)
    x_eq, y_eq = calculate_histogram(image_equalized)

    cv.imshow("imagen", cv.hconcat([image_original, image_equalized]))

    while True:
        k = cv.waitKey(0) & 0xFF
        if k == 27:
            cv.destroyAllWindows()
            break

    plt.subplot(1, 2, 1)
    plt.bar(x_original, y_original)
    plt.subplot(1, 2, 2)
    plt.bar(x_eq, y_eq)
    plt.show()


if __name__ == "__main__":
    main()
