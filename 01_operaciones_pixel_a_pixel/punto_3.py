import cv2 as cv
import numpy as np
from numpy._typing import NDArray


def read_images() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    image1 = cv.imread("BajoContrasteGrises.jpg")
    image2 = cv.imread("SobreeExpuestaGrises.jpg")
    image3 = cv.imread("SubexpuestaGrises.jpg")

    return image1, image2, image3


def print_images(image1, image2, image3) -> None:
    cv.imshow("image1", image1)
    cv.imshow("image2", image2)
    cv.imshow("image3", image3)


def gamma_correction(src: np.ndarray, gamma: float) -> np.ndarray:
    if gamma == 0:
        gamma = 0.00000001

    gamma_inv = 1 / gamma

    table = [((i / 255) ** gamma_inv) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv.LUT(src, table)


def on_change(slider_gamma: int):
    gamma: NDArray[np.float64] = np.interp(slider_gamma, [0, 1000], [0, 4])

    image1, image2, image3 = read_images()

    image1 = gamma_correction(image1, float(gamma))
    image2 = gamma_correction(image2, float(gamma))
    image3 = gamma_correction(image3, float(gamma))

    print_images(image1, image2, image3)


def main():
    image1, image2, image3 = read_images()

    print_images(image1, image2, image3)

    cv.createTrackbar("slider", "image1", 0, 1000, on_change)

    while True:
        k = cv.waitKey(0) & 0xFF
        if k == 27:
            cv.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
