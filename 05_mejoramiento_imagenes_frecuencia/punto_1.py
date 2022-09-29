import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def get_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return np.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


def homomorphic_filter(
    image: np.ndarray,
    gamma_h: float,
    gamma_l: float,
    c: float,
    r: float,
) -> np.ndarray:

    image_ln: np.ndarray = np.log(image + 0.001)

    image_dft: np.ndarray = np.fft.fft2(image_ln)
    image_dft = np.fft.fftshift(image_dft)

    height, width = image_dft.shape

    h_center = height / 2
    w_center = width / 2

    for h in range(height):
        for w in range(width):
            image_dft[h][w] *= (gamma_h - gamma_l) * (
                1 - np.exp(-c * (get_distance(h_center, w_center, h, w) ** 2 / r**2))
            ) + gamma_l

    image_dft = np.fft.ifftshift(image_dft)

    image_inv: np.ndarray = np.fft.ifft2(image_dft)

    image_exp: np.ndarray = np.exp(image_inv)

    return cv.normalize(abs(image_exp), image, 0, 255, cv.NORM_MINMAX)


def main() -> None:
    image_mars: np.ndarray = cv.imread("mars_moon_phobos.tif", 0)
    image_mars_homomorphic: np.ndarray = homomorphic_filter(image_mars, 0.25, 2, 1, 80)
    image_paisaje: np.ndarray = cv.imread("Paisaje.jpg", 0)
    image_paisaje_homomorphic: np.ndarray = homomorphic_filter(
        image_paisaje, 0.25, 2, 1, 80
    )

    plt.subplot(2, 2, 1)
    plt.imshow(cv.cvtColor(image_mars, cv.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Original mars")

    plt.subplot(2, 2, 2)
    plt.imshow(image_mars_homomorphic, cmap="gray")
    plt.axis("off")
    plt.title("Homomorphic mars")

    plt.subplot(2, 2, 3)
    plt.imshow(cv.cvtColor(image_paisaje, cv.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Original paisaje")

    plt.subplot(2, 2, 4)
    plt.imshow(image_paisaje_homomorphic, cmap="gray")
    plt.axis("off")
    plt.title("Homomorphic paisaje")

    plt.show()


if __name__ == "__main__":
    main()
