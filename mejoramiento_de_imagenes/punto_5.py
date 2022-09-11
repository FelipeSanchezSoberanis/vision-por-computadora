import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math
import random


def gaussian_distribution(x: float, mean: float, sigma: float) -> float:
    return (
        1
        / (sigma * math.sqrt(2 * math.pi))
        * math.exp((-1 / 2) * ((x - mean) / sigma) ** 2)
    )


def rayleigh_distribution(x: float, sigma: float) -> float:
    return x / sigma**2 * math.exp(-(x**2) / (2 * sigma**2))


def add_gaussian_noise(image: np.ndarray, mean: float, sigma: float) -> np.ndarray:
    image_gaussian: np.ndarray = image.copy()

    height, width = image_gaussian.shape

    x_axis: list[float] = [x for x in range(-255, 256)]
    y_axis: list[float] = [gaussian_distribution(x, mean, sigma) for x in x_axis]

    for h in range(height):
        for w in range(width):
            image_gaussian[h][w] += random.choices(x_axis, y_axis)

    return image_gaussian


def add_rayleigh_noise(image: np.ndarray, sigma: float) -> np.ndarray:
    image_gaussian: np.ndarray = image.copy()

    height, width = image_gaussian.shape

    x_axis: list[float] = [x for x in range(256)]
    y_axis: list[float] = [rayleigh_distribution(x, sigma) for x in x_axis]

    for h in range(height):
        for w in range(width):
            image_gaussian[h][w] += random.choices(x_axis, y_axis)

    return image_gaussian


def main() -> None:
    image = cv.imread("noise_tester.jpg", 0)
    image_gaussian = add_gaussian_noise(image, 10, 10)
    image_rayleigh = add_rayleigh_noise(image, 10)

    plt.subplot(3, 2, 1)
    plt.title("Original")
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(3, 2, 2)
    plt.title("Original histogram")
    plt.plot(cv.calcHist([image], [0], None, [255], [0, 255]))

    plt.subplot(3, 2, 3)
    plt.title("Gaussian")
    plt.imshow(cv.cvtColor(image_gaussian, cv.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(3, 2, 4)
    plt.title("Gaussian histogram")
    plt.plot(cv.calcHist([image_gaussian], [0], None, [255], [0, 255]))

    plt.subplot(3, 2, 5)
    plt.title("Rayleigh")
    plt.imshow(cv.cvtColor(image_rayleigh, cv.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(3, 2, 6)
    plt.title("Rayleigh histogram")
    plt.plot(cv.calcHist([image_rayleigh], [0], None, [255], [0, 255]))

    plt.show()


if __name__ == "__main__":
    main()
