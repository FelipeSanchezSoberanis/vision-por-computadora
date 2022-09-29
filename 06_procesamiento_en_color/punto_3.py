import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def normalize_hue(hue: int) -> int:
    return int(np.interp(hue, [0, 360], [0, 179]))


def normalize_saturation(saturation: int) -> int:
    return int(np.interp(saturation, [0, 100], [0, 255]))


def normalize_value(value: int) -> int:
    return int(np.interp(value, [0, 100], [0, 255]))


def main() -> None:
    image_toys: np.ndarray = cv.imread("Juguetes de Colores.jpg")
    image_objects: np.ndarray = cv.imread("Figuras de Colores.jpg")
    image_toys_hsv: np.ndarray = cv.cvtColor(image_toys, cv.COLOR_BGR2HSV)
    image_objects_hsv: np.ndarray = cv.cvtColor(image_objects, cv.COLOR_BGR2HSV)

    image_toys_grapes: np.ndarray = cv.bitwise_and(
        image_toys_hsv,
        image_toys_hsv,
        mask=cv.inRange(
            image_toys_hsv,
            np.array(
                (normalize_hue(280), normalize_saturation(45), normalize_value(43))
            ),
            np.array(
                (normalize_hue(290), normalize_saturation(75), normalize_value(73))
            ),
        ),
    )

    image_objects_orange: np.ndarray = cv.bitwise_and(
        image_objects_hsv,
        image_objects_hsv,
        mask=cv.inRange(
            image_objects_hsv,
            np.array(
                (normalize_hue(33), normalize_saturation(81), normalize_value(85))
            ),
            np.array(
                (normalize_hue(43), normalize_saturation(100), normalize_value(100))
            ),
        ),
    )

    rows, cols = 1, 4

    plt.subplot(rows, cols, 1)
    plt.imshow(cv.cvtColor(image_toys, cv.COLOR_BGR2RGB))
    plt.title("Original toys")
    plt.axis("off")

    plt.subplot(rows, cols, 2)
    plt.imshow(cv.cvtColor(image_toys_grapes, cv.COLOR_HSV2RGB))
    plt.title("Grapes segmented")
    plt.axis("off")

    plt.subplot(rows, cols, 3)
    plt.imshow(cv.cvtColor(image_objects, cv.COLOR_BGR2RGB))
    plt.title("Original objects")
    plt.axis("off")

    plt.subplot(rows, cols, 4)
    plt.imshow(cv.cvtColor(image_objects_orange, cv.COLOR_HSV2RGB))
    plt.title("Orange objects segmented")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
