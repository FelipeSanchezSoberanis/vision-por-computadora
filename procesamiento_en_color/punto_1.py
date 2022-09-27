import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from typing import Callable as callable
import math


def harmonic_mean(pixels: list[int]) -> int:
    return len(pixels) / np.sum([1 / (pixel + 0.001) for pixel in pixels])


def remove_max(pixels: list[int]) -> int:
    pixels_no_max: list[int] = [pixel for pixel in pixels if pixel < 0.9 * max(pixels)]
    if len(pixels_no_max):
        return int(np.average(sorted(pixels_no_max)))
    return int(np.average(pixels))


def apply_filter(
    image: np.ndarray, kernel: int, function: callable, image_type: str
) -> np.ndarray:
    height, width, _ = image.shape

    image_filtered: np.ndarray = image.copy()

    iter_min: int = math.floor(kernel / 2)
    iter_max: int = math.ceil(kernel / 2)

    pixels: list[np.ndarray] = []

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

                if image_type == "RGB":
                    if image[h][w][0] == max([pixel[0] for pixel in pixels]):
                        image_filtered[h][w][0] = function(
                            [pixel[0] for pixel in pixels]
                        )
                    if image[h][w][1] == max([pixel[1] for pixel in pixels]):
                        image_filtered[h][w][1] = function(
                            [pixel[1] for pixel in pixels]
                        )
                    if image[h][w][2] == max([pixel[2] for pixel in pixels]):
                        image_filtered[h][w][2] = function(
                            [pixel[2] for pixel in pixels]
                        )
                if image_type == "HLS":
                    if image[h][w][1] == max([pixel[1] for pixel in pixels]):
                        image_filtered[h][w][1] = function(
                            [pixel[1] for pixel in pixels]
                        )

            pixels = []

    return image_filtered


def main() -> None:
    image_lena: np.ndarray = cv.imread("Lena RGB Sal.tif")
    image_lena_HLS: np.ndarray = cv.cvtColor(image_lena, cv.COLOR_BGR2HLS)
    image_lena_denoise_RGB: np.ndarray = apply_filter(image_lena, 3, remove_max, "RGB")
    image_lena_denoise_HSL: np.ndarray = apply_filter(
        image_lena_HLS, 3, remove_max, "HLS"
    )

    image_valle: np.ndarray = cv.imread(
        "Valle de la luna-adicion de ruido gaussiano.jpg"
    )
    image_valle_HLS: np.ndarray = cv.cvtColor(image_valle, cv.COLOR_BGR2HLS)
    image_valle_denoise_RGB: np.ndarray = apply_filter(
        image_valle, 3, harmonic_mean, "RGB"
    )
    image_valle_denoise_HSL: np.ndarray = apply_filter(
        image_valle_HLS, 3, harmonic_mean, "HLS"
    )

    rows, cols = 2, 3

    plt.subplot(rows, cols, 1)
    plt.imshow(cv.cvtColor(image_lena, cv.COLOR_BGR2RGB))
    plt.title("Lena original")
    plt.axis("off")

    plt.subplot(rows, cols, 2)
    plt.imshow(cv.cvtColor(image_lena_denoise_RGB, cv.COLOR_BGR2RGB))
    plt.title("Lena denoised RGB")
    plt.axis("off")

    plt.subplot(rows, cols, 3)
    plt.imshow(cv.cvtColor(image_lena_denoise_HSL, cv.COLOR_HLS2RGB))
    plt.title("Lena denoised HSL")
    plt.axis("off")

    plt.subplot(rows, cols, 4)
    plt.imshow(cv.cvtColor(image_valle, cv.COLOR_BGR2RGB))
    plt.title("Valle original")
    plt.axis("off")

    plt.subplot(rows, cols, 5)
    plt.imshow(cv.cvtColor(image_valle_denoise_RGB, cv.COLOR_BGR2RGB))
    plt.title("Valle denoised RGB")
    plt.axis("off")

    plt.subplot(rows, cols, 6)
    plt.imshow(cv.cvtColor(image_valle_denoise_HSL, cv.COLOR_HLS2RGB))
    plt.title("Valle denoised HSL")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
