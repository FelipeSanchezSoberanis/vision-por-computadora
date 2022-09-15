import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import noises, punto_1 as filters


def main() -> None:
    print("0 de 12")
    image: np.ndarray = cv.imread("image-max.jpg", 0)
    print("1 de 12")
    image_gaussian: np.ndarray = noises.add_gaussian_noise(image, 0, 2)
    print("2 de 12")
    image_gaussian_denoised: np.ndarray = filters.apply_filter(
        image_gaussian, 3, filters.harmonic_mean
    )
    print("3 de 12")
    image_salt: np.ndarray = noises.add_salt_noise(image, 0.025)
    print("4 de 12")
    image_salt_denoised: np.ndarray = filters.apply_filter(image, 3, min)
    print("5 de 12")
    image_pepper: np.ndarray = noises.add_pepper_noise(image, 0.025)
    print("6 de 12")
    image_pepper_denoised: np.ndarray = filters.apply_filter(image, 3, max)
    print("7 de 12")
    image_salt_and_pepper: np.ndarray = noises.add_salt_and_pepper_noise(image, 0.025)
    print("8 de 12")
    image_salt_and_pepper_denoised: np.ndarray = filters.apply_filter(
        image, 3, filters.mode
    )
    print("9 de 12")
    image_combined: np.ndarray = noises.add_gaussian_noise(image, 0, 2)
    print("10 de 12")
    image_combined = noises.add_salt_and_pepper_noise(image_combined, 0.025)
    print("11 de 12")
    image_combined_denoised = filters.apply_filter(
        image_combined, 3, filters.mean_alpha
    )
    print("12 de 12")

    images: dict[str, np.ndarray] = {
        "Gaussian": image_gaussian,
        "Gaussian denoised": image_gaussian_denoised,
        "Salt": image_salt,
        "Salt denoised": image_salt_denoised,
        "Pepper": image_pepper,
        "Pepper denoised": image_pepper_denoised,
        "Salt and pepper": image_salt_and_pepper,
        "Salt and pepper denoised": image_salt_and_pepper_denoised,
        "Image combined": image_combined,
        "Image combined denoised": image_combined_denoised,
    }

    for i, (name, image) in enumerate(images.items()):
        plt.subplot(3, 4, i + 1)
        plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        plt.title(name)
        plt.axis("off")

    plt.show()


if __name__ == "__main__":
    main()
