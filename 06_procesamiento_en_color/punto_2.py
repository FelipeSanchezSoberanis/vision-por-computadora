import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from punto_3 import normalize_hue


def segmentate_by_hue(image: np.ndarray, hue: int, margin: float) -> np.ndarray:
    height, width, _ = image.shape

    mask: np.ndarray = np.zeros((height, width), dtype="uint8")

    channel_h, channel_l, channel_s = cv.split(image)

    min_margin, max_margin = 1 - margin, 1 + margin

    for h in range(height):
        for w in range(width):
            if min_margin * hue < channel_h[h][w] < max_margin * hue:
                mask[h][w] = 1

    channel_h = cv.bitwise_and(channel_h, channel_h, mask=mask)
    channel_l = cv.bitwise_and(channel_l, channel_l, mask=mask)
    channel_s = cv.bitwise_and(channel_s, channel_s, mask=mask)

    return cv.merge((channel_h, channel_l, channel_s))


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
    image_toys: np.ndarray = cv.imread("Juguetes de Colores.jpg")
    image_objects: np.ndarray = cv.imread("Figuras de Colores.jpg")
    image_toys_hsl: np.ndarray = cv.cvtColor(image_toys, cv.COLOR_BGR2HLS)
    image_objects_hsl: np.ndarray = cv.cvtColor(image_objects, cv.COLOR_BGR2HLS)

    image_toys_grapes: np.ndarray = segmentate_by_rbg(image_toys, 122, 57, 146, 0.5)
    image_objects_orange: np.ndarray = segmentate_by_rbg(
        image_objects, 243, 163, 22, 0.25
    )
    image_toys_hsl_grapes: np.ndarray = segmentate_by_hue(
        image_toys_hsl, normalize_hue(284), 0.1
    )
    image_objects_hsl_orange: np.ndarray = segmentate_by_hue(
        image_objects_hsl, normalize_hue(38), 0.1
    )

    rows, cols = 2, 4

    plt.subplot(rows, cols, 1)
    plt.imshow(cv.cvtColor(image_toys, cv.COLOR_BGR2RGB))
    plt.title("Original toys")
    plt.axis("off")

    plt.subplot(rows, cols, 2)
    plt.imshow(cv.cvtColor(image_toys_grapes, cv.COLOR_BGRA2RGBA))
    plt.title("Grapes segmented")
    plt.axis("off")

    plt.subplot(rows, cols, 3)
    plt.imshow(cv.cvtColor(image_objects, cv.COLOR_BGR2RGB))
    plt.title("Original objects")
    plt.axis("off")

    plt.subplot(rows, cols, 4)
    plt.imshow(cv.cvtColor(image_objects_orange, cv.COLOR_BGRA2RGBA))
    plt.title("Orange objects segmented")
    plt.axis("off")

    plt.subplot(rows, cols, 5)
    plt.imshow(image_toys_hsl)
    plt.title("Original toys")
    plt.axis("off")

    plt.subplot(rows, cols, 6)
    plt.imshow(cv.cvtColor(image_toys_hsl_grapes, cv.COLOR_HLS2RGB))
    plt.title("Grapes segmented HSL")
    plt.axis("off")

    plt.subplot(rows, cols, 7)
    plt.imshow(image_objects_hsl)
    plt.title("Original objects")
    plt.axis("off")

    plt.subplot(rows, cols, 8)
    plt.imshow(cv.cvtColor(image_objects_hsl_orange, cv.COLOR_HLS2RGB))
    plt.title("Orange objects segmented HSL")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
