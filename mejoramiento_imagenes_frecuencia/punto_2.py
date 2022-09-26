import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


image = cv.imread("Lena.tif")
gauss = cv.GaussianBlur(image, (7, 7), 0)
unsharp_image = cv.addWeighted(image, 2, gauss, -1, 0)

plt.subplot(1, 2, 1)
plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.imshow(cv.cvtColor(unsharp_image, cv.COLOR_BGR2RGB))

plt.show()
