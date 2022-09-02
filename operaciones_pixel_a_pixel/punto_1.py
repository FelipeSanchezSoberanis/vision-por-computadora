import cv2 as cv
import numpy as np

resolutions: list[float] = [1.5, 0.5, 0.25, 0.125]
methods: list[int] = [cv.INTER_NEAREST, cv.INTER_LINEAR, cv.INTER_CUBIC]
images: list[np.ndarray] = []


image = cv.imread("Legos.jpg")
image_grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

for resolution in resolutions:
    for method in methods:
        images.append(
            cv.resize(
                image_grey, None, fx=resolution, fy=resolution, interpolation=method
            )
        )


for i, image in enumerate(images):
    cv.imshow("{}".format(i), image)

cv.waitKey(0)
cv.destroyAllWindows()
