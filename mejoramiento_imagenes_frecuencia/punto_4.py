import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math
import progressbar as pb


def filter_wiener(image: np.ndarray):
    K = 10

    img_z = np.float32(image)
    img_fft = np.fft.fft2(img_z)
    img_sfft = np.fft.fftshift(img_fft)

    x, y = image.shape
    cx, cy = x // 2, y // 2

    a = 0.15
    b = 0.2
    T = 1.0

    H = np.copy(img_sfft)
    for t in range(x):
        for r in range(y):
            aux = np.pi * ((t - cx) * a + (r - cy) * b)
            if aux == 0:
                aux = 0.001
            H[t, r] = (T / aux) * np.sin(aux) * np.e ** (-1j * aux)

    Wiener = ((np.abs(H) ** 2) / ((np.abs(H) ** 2) + K)) * (1 / H)
    G = img_sfft * Wiener

    processed_fftshift = np.fft.ifftshift(G)
    processed_fft = np.fft.ifft2(processed_fftshift)

    img_out = cv.normalize(abs(processed_fft), image, 0, 255, cv.NORM_MINMAX)
    return img_out


def gaussian_blur(image: np.ndarray, var: float, kernel: int) -> np.ndarray:
    blur = cv.GaussianBlur(image, (kernel, kernel), 0)
    return blur


def lineal_movement_degradation(
    image: np.ndarray, a: float, b: float, t: float
) -> np.ndarray:
    image_fft: np.ndarray = np.fft.fft2(image)
    image_fft: np.ndarray = np.fft.fftshift(image_fft)

    height, width = image.shape
    x_center, y_center = height // 2, width // 2

    H = np.copy(image_fft)

    for h in range(height):
        for w in range(width):
            aux = np.pi * ((h - x_center) * a + (w - y_center) * b)
            if aux == 0:
                aux = 0.001
            H[h, w] = (t / aux) * np.sin(aux) * np.e ** (-1j * aux)

    G = H * image_fft

    processed_fftshift = np.fft.ifftshift(G)
    processed_fft = np.fft.ifft2(processed_fftshift)

    img_out: np.ndarray = cv.normalize(
        abs(processed_fft), image, 0, 255, cv.NORM_MINMAX
    )

    return img_out


def main() -> None:
    image: np.ndarray = cv.imread("PortadaLibro.tif", 0)
    image_filter: np.ndarray = lineal_movement_degradation(image, 0.15, 0.2, 100)
    image_gaussian: np.ndarray = gaussian_blur(image, 10, 21)
    image_wiener: np.ndarray = filter_wiener(image)

    plt.subplot(2, 2, 1)
    plt.imshow(image_filter, cmap="gray")

    plt.subplot(2, 2, 2)
    plt.imshow(cv.cvtColor(image_gaussian, cv.COLOR_BGR2RGB))

    plt.subplot(2, 2, 3)
    plt.imshow(image_wiener, cmap="gray")

    plt.show()


if __name__ == "__main__":
    main()
