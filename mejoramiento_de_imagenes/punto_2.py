from punto_1 import equalize_image
import cv2 as cv
import matplotlib.pyplot as plt


def main() -> None:
    image = cv.imread("Fig0309(a)(washed_out_aerial_image).tif", cv.IMREAD_GRAYSCALE)

    image_eq_custom = equalize_image(image)
    image_eq_opencv = cv.equalizeHist(image)

    plt.subplot(1, 3, 1)
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(cv.cvtColor(image_eq_custom, cv.COLOR_BGR2RGB))
    plt.title("Custom equalization")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv.cvtColor(image_eq_opencv, cv.COLOR_BGR2RGB))
    plt.title("Open CVs equalization")
    plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
