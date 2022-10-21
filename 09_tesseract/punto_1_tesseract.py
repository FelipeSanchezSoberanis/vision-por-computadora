import cv2 as cv
import numpy as np
import pytesseract


def ordenar_puntos(puntos):
    n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()
    y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])

    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]


def main() -> None:
    video: cv.VideoCapture = cv.VideoCapture("VID_20221020_214710.mp4")

    cv.namedWindow("video", cv.WINDOW_NORMAL)

    while True:
        frame_original: cv.Mat = video.read()[1][0::, 1290::]

        dst = None

        gray = cv.cvtColor(frame_original, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (5, 5), 0)
        canny = cv.Canny(gray, 70, 255)
        canny = cv.dilate(canny, None, iterations=1)
        cnts = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]

        for c in cnts:
            epsilon = 0.01 * cv.arcLength(c, True)
            approx = cv.approxPolyDP(c, epsilon, True)

            if len(approx) == 4 and cv.contourArea(c) > 1000000:
                cv.drawContours(frame_original, [approx], 0, (0, 255, 255), 2)

                puntos = ordenar_puntos(approx)

                pts1: cv.Mat = np.float32(puntos)
                pts2: cv.Mat = np.float32([[0, 0], [1400, 0], [0, 1100], [1400, 1100]])
                M = cv.getPerspectiveTransform(pts1, pts2)
                dst = cv.warpPerspective(frame_original, M, (1400, 1100))
                cv.imshow("video", dst)
                #  print(
                #      pytesseract.image_to_string(dst, lang="eng+equ", config="--psm 6")
                #  )

        if dst is None:
            cv.imshow("video", frame_original)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
