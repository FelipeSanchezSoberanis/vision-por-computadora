import cv2 as cv
import matplotlib.pyplot as plt
from noise_functions import gaussian_blur


def main() -> None:
    image = cv.imread("Fig0309(a)(washed_out_aerial_image).tif")
    image_gaussian = gaussian_blur(image, 3, 1.5)

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
