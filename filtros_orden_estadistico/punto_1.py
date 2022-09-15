import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def filter_mean(image: np.ndarray, kernel: int) -> np.ndarray:
    mean_array: np.ndarray = np.ones((kernel, kernel)) / kernel**2
    return cv.filter2D(image, -1, mean_array)


def print_images(kernel: int) -> None:
    image: np.ndarray = cv.imread("opencv-logo.jpg")
    image_mean: np.ndarray = filter_mean(image, kernel)

    images: dict[str, np.ndarray] = {"Original": image, "Mean": image_mean}

    for i, (name, image) in enumerate(images.items()):
        plt.subplot(1, 2, i + 1)
        plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        plt.title(name)
        plt.axis("off")


def main() -> None:
    print_images(3)

    axfreq = plt.axes([0.20, 0.1, 0.65, 0.03])
    kernel_slider = plt.Slider(
        ax=axfreq,
        label="Kernel",
        valmin=3,
        valmax=25,
        valstep=1,
        valinit=3,
    )
    kernel_slider.on_changed(print_images)

    plt.show()


if __name__ == "__main__":
    main()
