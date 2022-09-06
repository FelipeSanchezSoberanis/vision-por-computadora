from punto_1 import equalize_image
import cv2 as cv


def main() -> None:
    image = cv.imread("Fig0309(a)(washed_out_aerial_image).tif", cv.IMREAD_GRAYSCALE)

    image_eq_custom = equalize_image(image)
    image_eq_opencv = cv.equalizeHist(image)

    cv.imshow("image", cv.hconcat([image, image_eq_custom, image_eq_opencv]))

    while True:
        k = cv.waitKey(0) & 0xFF
        if k == 27:
            cv.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
