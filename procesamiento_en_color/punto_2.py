import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


#  ROJO: rgb(235, 46, 40)


def segmentate_by_rbg(
    image: np.ndarray, r: int, g: int, b: int, margin: float
) -> np.ndarray:
    height, width, _ = image.shape

    mask: np.ndarray = np.zeros((height, width), dtype="uint8")

    channel_b, channel_g, channel_r = cv.split(image)

    min_margin, max_margin = 1 - margin, 1 + margin

    for h in range(height):
        for w in range(width):
            if (
                min_margin * b < channel_b[h][w] < max_margin * b
                and min_margin * g < channel_g[h][w] < max_margin * g
                and min_margin * r < channel_r[h][w] < max_margin * r
            ):
                mask[h][w] = 1

    channel_b *= mask
    channel_g *= mask
    channel_r *= mask
    channel_a: np.ndarray = mask * 255

    return cv.merge((channel_b, channel_g, channel_r, channel_a))


def main() -> None:
    image: np.ndarray = cv.imread("Figuras de Colores.jpg")
    image_red: np.ndarray = segmentate_by_rbg(image, 235, 46, 40, 1)

    rows, cols = 1, 2

    plt.subplot(rows, cols, 1)
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(rows, cols, 2)
    plt.imshow(cv.cvtColor(image_red, cv.COLOR_BGRA2RGBA))
    plt.title("Original")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
