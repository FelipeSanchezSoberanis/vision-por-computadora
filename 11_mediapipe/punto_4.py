import cv2 as cv
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

cv.namedWindow("MediaPipe Selfie Segmentation", cv.WINDOW_NORMAL)

cap = cv.VideoCapture("video_call_input.mp4")
bg_video = cv.VideoCapture("CarreteraBosque_fix.mp4")

with mp_selfie_segmentation.SelfieSegmentation(
    model_selection=1
) as selfie_segmentation:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image = cv.cvtColor(cv.flip(image, 1), cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = selfie_segmentation.process(image)

        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1

        bg_image = bg_video.read()[1]
        if bg_image is None:
            bg_video = cv.VideoCapture("CarreteraBosque_fix.mp4")
            bg_image = bg_video.read()[1]

        output_image = np.where(condition, image, bg_image)

        cv.imshow("MediaPipe Selfie Segmentation", output_image)

        if cv.waitKey(33) & 0xFF == ord("q"):
            break
cap.release()
