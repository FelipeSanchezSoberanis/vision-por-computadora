from typing import Callable as callable
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib import math


def contraharmonic_mean(pixels: list[int]) -> float:
    return np.mean([pixel**2 for pixel in pixels], dtype="float") / np.mean(
        pixels, dtype="float"
    )


def harmonic_mean(pixels: list[int]) -> float:
    return len(pixels) / np.sum([1 / pixel for pixel in pixels])


def geometric_mean(pixels: list[int]) -> float:
    return np.exp(np.log(pixels).mean())


def filter_mean(image: np.ndarray, kernel: int) -> np.ndarray:
    mean_array: np.ndarray = np.ones((kernel, kernel)) / kernel**2
    return cv.filter2D(image, -1, mean_array)


def apply_filter(
    image: np.ndarray, kernel: int, function: callable[[list[int]], float]
) -> np.ndarray:
    height, width = image.shape

    image_filtered: np.ndarray = image.copy()

    iter_min: int = math.floor(kernel / 2)
    iter_max: int = math.ceil(kernel / 2)

    pixels: list[int] = []

    for h in range(height):
        for w in range(width):
            for i in range(-iter_min, iter_max):
                h_current: int = h + i

                if h_current < 0:
                    h_current += height
                if h_current >= height:
                    h_current -= height

                for j in range(-iter_min, iter_max):
                    w_current: int = w + j

                    if w_current < 0:
                        w_current += width
                    if w_current >= width:
                        w_current -= width

                    pixels.append(image[h_current][w_current])

            image_filtered[h][w] = function(pixels)
            pixels = []

    return image_filtered


def print_images(kernel: int) -> None:
    image: np.ndarray = cv.imread("opencv-logo.jpg", 0)
    image_mean: np.ndarray = filter_mean(image, kernel)
    image_geometric_mean: np.ndarray = apply_filter(image, kernel, geometric_mean)
    image_harmonic_mean: np.ndarray = apply_filter(image, kernel, harmonic_mean)
    image_contraharmonic_mean: np.ndarray = apply_filter(
        image, kernel, contraharmonic_mean
    )

    images: dict[str, np.ndarray] = {
        "Original": image,
        "Mean": image_mean,
        "Geometric mean": image_geometric_mean,
        "Harmonic mean": image_harmonic_mean,
        "Contraharmonic mean": image_contraharmonic_mean,
    }

    for i, (name, image) in enumerate(images.items()):
        plt.subplot(2, 4, i + 1)
        plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        plt.title(name)
        plt.axis("off")


def main() -> None:
    print_images(3)

    #  axfreq = plt.axes([0.20, 0.1, 0.65, 0.03])
    #  kernel_slider = plt.Slider(
    #  ax=axfreq,
    #  label="Kernel",
    #  valmin=3,
    #  valmax=25,
    #  valstep=1,
    #  valinit=3,
    #  )
    #  kernel_slider.on_changed(print_images)

    plt.show()


if __name__ == "__main__":
    main()
