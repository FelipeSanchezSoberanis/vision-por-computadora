import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Identidad
def apply_affine_transform(image: np.ndarray) -> np.ndarray:
    rows, cols, _ = image.shape

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv.getAffineTransform(pts1, pts2)
    dst = cv.warpAffine(image, M, (cols, rows))

    return dst


def print_images(images: dict[str, np.ndarray]) -> None:
    rows: int = 2
    cols: int = 8

    for i, (description, image) in enumerate(images.items()):
        plt.subplot(rows, cols, i + 1)
        plt.title(description)
        plt.imshow(image)
        plt.axis("off")

    plt.show()


def main() -> None:

    image = cv.imread("parallel-lines.jpg")
    image_affine = apply_affine_transform(image)

    images: dict[str, np.ndarray] = {"Original": image, "Identidad": image_affine}

    print_images(images)


if __name__ == "__main__":
    main()
