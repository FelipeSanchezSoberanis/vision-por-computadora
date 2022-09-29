import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import progressbar
import math


def smooth_image(image: np.ndarray, kernel: int) -> np.ndarray:
    height, width, _ = image.shape

    image_smooth = image.copy()

    pixels: list[int] = []

    progress_bar = progressbar.ProgressBar(max_value=(width) * (height)).start()

    counter: int = 0
    for y in range(0, width):
        for x in range(0, height):
            for i in range(-math.floor(kernel / 2), math.ceil(kernel / 2)):
                for j in range(-math.floor(kernel / 2), math.ceil(kernel / 2)):
                    if 0 <= x + i < height and 0 <= y + j < width:
                        pixels.append(image[x + i][y + j])
            average = sum([pixel / len(pixels) for pixel in pixels])
            image_smooth[x][y] = average
            pixels = []

            counter += 1
            progress_bar.update(counter)

    return image_smooth


def main() -> None:
    image = cv.imread("Fig0309(a)(washed_out_aerial_image).tif")

    image_smooth = smooth_image(image, 3)

    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.axis("off")
    plt.imshow(image)

    plt.subplot(1, 2, 2)
    plt.title("Smoothed")
    plt.axis("off")
    plt.imshow(image_smooth)

    plt.show()


if __name__ == "__main__":
    main()
