import math
import numpy as np
import progressbar as pb


def gaussian_function_2d(x: int, y: int, sigma: float) -> float:
    return (
        1 / (2 * math.pi * sigma**2) * math.exp(-(x**2 + y**2) / (2 * sigma**2))
    )


def get_weight_matrix(kernel: int, sigma: float) -> list[list[float]]:
    weight_matrix: list[list[float]] = []

    offset: int = -math.floor(kernel / 2)

    sum: float = 0

    for x in range(kernel):
        weight_matrix.append([])
        for y in range(kernel):
            value: float = gaussian_function_2d(x + offset, y + offset, sigma)
            weight_matrix[x].append(value)
            sum += value

    for x, row in enumerate(weight_matrix):
        for y, _ in enumerate(row):
            weight_matrix[x][y] /= sum

    return weight_matrix


def gaussian_blur(image: np.ndarray, kernel: int, sigma: float) -> np.ndarray:
    weight_matrix: list[list[float]] = get_weight_matrix(kernel, sigma)

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
