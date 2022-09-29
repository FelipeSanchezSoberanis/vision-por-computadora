import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def main() -> None:
    image_toys: np.ndarray = cv.imread("Juguetes de Colores.jpg")
    image_objects: np.ndarray = cv.imread("Figuras de Colores.jpg")
    image_toys_hsv: np.ndarray = cv.cvtColor(image_toys, cv.COLOR_BGR2HSV)
    image_objects_hsv: np.ndarray = cv.cvtColor(image_objects, cv.COLOR_BGR2HSV)

    image_toys_grapes: np.ndarray = cv.inRange(
        image_toys_hsv, (284, 61, 57), (284, 61, 57)
    )
    image_objects_orange: np.ndarray = segmentate_by_rbg(
        image_objects, 243, 163, 22, 0.25
    )

    rows, cols = 1, 4

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

    plt.show()


if __name__ == "__main__":
    main()
