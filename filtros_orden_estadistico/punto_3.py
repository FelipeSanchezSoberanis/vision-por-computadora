import cv2 as cv
import progressbar as pb
import math
import matplotlib.pyplot as plt
import numpy as np
import noises


def adaptative_median_filter(
    image: np.ndarray, kernel_max: int, initial_kernel: int = 3
) -> np.ndarray:
    height, width = image.shape

    image_filtered: np.ndarray = image.copy()

    z_min: int
    z_max: int
    z_med: float
    z_xy: int
    s_max: int = kernel_max
    a_1: float
    a_2: float
    b_1: float
    b_2: float

    pixels: list[int] = []

    progress_bar = pb.ProgressBar(max_value=(width) * (height)).start()
    counter: int = 0

    for h in range(height):
        for w in range(width):
            kernel: int = initial_kernel

            iter_min: int = math.floor(kernel / 2)
            iter_max: int = math.ceil(kernel / 2)

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

            while True:
                z_min = min(pixels)
                z_max = max(pixels)
                z_med = float(np.median(pixels))
                z_xy = image[h][w]

                a_1 = z_med - z_min
                a_2 = z_med - z_max

                if a_1 > 0 and a_2 < 0:
                    b_1 = z_xy - z_min
                    b_2 = z_xy - z_max

                    if b_1 > 0 and b_2 < 0:
                        image_filtered[h][w] = z_xy
                    else:
                        image_filtered[h][w] = z_med
                    break
                else:
                    kernel += 1

                    if kernel <= s_max:
                        continue
                    else:
                        image_filtered[h][w] = z_xy
                        break

            counter += 1
            progress_bar.update(counter)

            pixels = []

    return image_filtered


def main() -> None:
    image: np.ndarray = cv.imread("image-max.jpg", 0)
    image_salt_and_pepper: np.ndarray = noises.add_salt_and_pepper_noise(image, 0.2)
    image_filtered: np.ndarray = adaptative_median_filter(image_salt_and_pepper, 5)

    plt.subplot(1, 2, 1)
    plt.imshow(cv.cvtColor(image_salt_and_pepper, cv.COLOR_BGR2RGB))
    plt.title("Salt and pepper")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv.cvtColor(image_filtered, cv.COLOR_BGR2RGB))
    plt.title("Adaptative median filter")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
