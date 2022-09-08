import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math
import progressbar as pb


def matrix_is_square(matrix: list[list[float]]) -> bool:
    length: int = len(matrix)

    for row in matrix:
        if not len(row) == length:
            return False

    return True


def gaussian_blur(image: np.ndarray, weight_matrix: list[list[float]]) -> np.ndarray:
    if not matrix_is_square(weight_matrix):
        raise RuntimeError("Weigth matrix is not square")

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
                    x_temp = x + i
                    y_temp = y + j

                    if x_temp < 0:
                        x_temp += height
                    if x_temp >= height:
                        x_temp -= height

                    if y_temp < 0:
                        y_temp += width
                    if y_temp >= width:
                        y_temp -= width

                    pixels.append(
                        image[x_temp][y_temp]
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
        image,
        [
            [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
            [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
            [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
            [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
            [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25],
        ],
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
