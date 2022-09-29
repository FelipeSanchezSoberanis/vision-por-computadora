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


def exponential_distribution(x: float, _lambda: float) -> float:
    return _lambda * math.exp(-_lambda * x)


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
    image_rayleigh: np.ndarray = image.copy()

    height, width = image_rayleigh.shape

    x_axis: list[float] = [x for x in range(256)]
    y_axis: list[float] = [rayleigh_distribution(x, sigma) for x in x_axis]

    for h in range(height):
        for w in range(width):
            image_rayleigh[h][w] += random.choices(x_axis, y_axis)

    return image_rayleigh


def add_exponential_noise(image: np.ndarray, _lambda: float) -> np.ndarray:
    image_exponential: np.ndarray = image.copy()

    height, width = image_exponential.shape

    x_axis: list[float] = [x for x in range(256)]
    y_axis: list[float] = [exponential_distribution(x, _lambda) for x in x_axis]

    for h in range(height):
        for w in range(width):
            image_exponential[h][w] += random.choices(x_axis, y_axis)

    return image_exponential


def add_salt_and_pepper_noise(image: np.ndarray, probability: float) -> np.ndarray:
    image_salt_and_pepper: np.ndarray = image.copy()

    height, width = image_salt_and_pepper.shape

    for h in range(height):
        for w in range(width):
            if random.random() <= probability:
                image_salt_and_pepper[h][w] = -255 + random.random() * 255 * 2

    return image_salt_and_pepper


def main() -> None:
    image = cv.imread("noise_tester.jpg", 0)
    image_gaussian = add_gaussian_noise(image, 10, 10)
    image_rayleigh = add_rayleigh_noise(image, 10)
    image_exponential = add_exponential_noise(image, 0.125)
    image_salt_and_pepper = add_salt_and_pepper_noise(image, 0.9)

    data: dict[str, np.ndarray] = {
        "Original": image,
        "Gaussian": image_gaussian,
        "Rayleigh": image_rayleigh,
        "Exponential": image_exponential,
        "Salt and pepper": image_salt_and_pepper,
    }

    for i, (image_name, image_data) in enumerate(data.items()):
        i *= 2

        plt.subplot(3, 4, i + 1)
        plt.title("{}".format(image_name))
        plt.imshow(cv.cvtColor(image_data, cv.COLOR_BGR2RGB))
        plt.axis("off")

        plt.subplot(3, 4, i + 2)
        plt.title("{} histogram".format(image_name))
        plt.plot(cv.calcHist([image_data], [0], None, [255], [0, 255]))

    plt.show()


if __name__ == "__main__":
    main()
