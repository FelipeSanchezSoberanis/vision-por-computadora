import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math
import progressbar as pb


def gaussian_blur(image: np.ndarray, weight_matrix: list[list[float]]) -> np.ndarray:
    kernel: int = len(weight_matrix)

    height, width, _ = image.shape

    image_smooth = image.copy()

    pixels: list[int] = []

    progress_bar = pb.ProgressBar(max_value=(width) * (height)).start()

    counter: int = 0
    for y in range(0, width):
        for x in range(0, height):
            for i in range(-math.floor(kernel / 2), math.ceil(kernel / 2)):
                for j in range(-math.floor(kernel / 2), math.ceil(kernel / 2)):
                    if 0 <= x + i < height and 0 <= y + j < width:
                        pixels.append(
                            image[x + i][y + j]
                            * weight_matrix[i + math.floor(kernel / 2)][
                                j + math.floor(kernel / 2)
                            ]
                        )
            average = sum(pixels)
            image_smooth[x][y] = average
            pixels = []

            counter += 1
            progress_bar.update(counter)

    return image_smooth


def main() -> None:
    image = cv.imread("Fig0309(a)(washed_out_aerial_image).tif")
    image_gaussian = gaussian_blur(
        image, [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]]
    )

    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(image_gaussian)
    plt.title("Gaussian")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
