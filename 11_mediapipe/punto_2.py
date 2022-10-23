import cv2 as cv
import mediapipe as mp
from punto_1 import LandMarkCoordinates


class BodyLandMarkCoordinates(LandMarkCoordinates):
    visibility: float


class Body:
    def __init__(self, landmarks):
        self.nose: BodyLandMarkCoordinates = landmarks[0]
        self.left_eye_inner: BodyLandMarkCoordinates = landmarks[1]
        self.left_eye: BodyLandMarkCoordinates = landmarks[2]
        self.left_eye_outer: BodyLandMarkCoordinates = landmarks[3]
        self.right_eye_inner: BodyLandMarkCoordinates = landmarks[4]
        self.right_eye: BodyLandMarkCoordinates = landmarks[5]
        self.right_eye_outer: BodyLandMarkCoordinates = landmarks[6]
        self.left_ear: BodyLandMarkCoordinates = landmarks[7]
        self.right_ear: BodyLandMarkCoordinates = landmarks[8]
        self.mouth_left: BodyLandMarkCoordinates = landmarks[9]
        self.mouth_right: BodyLandMarkCoordinates = landmarks[10]
        self.left_shoulder: BodyLandMarkCoordinates = landmarks[11]
        self.right_shoulder: BodyLandMarkCoordinates = landmarks[12]
        self.left_elbow: BodyLandMarkCoordinates = landmarks[13]
        self.right_elbow: BodyLandMarkCoordinates = landmarks[14]
        self.left_wrist: BodyLandMarkCoordinates = landmarks[15]
        self.right_wrist: BodyLandMarkCoordinates = landmarks[16]
        self.left_pinky: BodyLandMarkCoordinates = landmarks[17]
        self.right_pinky: BodyLandMarkCoordinates = landmarks[18]
        self.left_index: BodyLandMarkCoordinates = landmarks[19]
        self.right_index: BodyLandMarkCoordinates = landmarks[20]
        self.left_thumb: BodyLandMarkCoordinates = landmarks[21]
        self.right_thumb: BodyLandMarkCoordinates = landmarks[22]
        self.left_hip: BodyLandMarkCoordinates = landmarks[23]
        self.right_hip: BodyLandMarkCoordinates = landmarks[24]
        self.left_knee: BodyLandMarkCoordinates = landmarks[25]
        self.right_knee: BodyLandMarkCoordinates = landmarks[26]
        self.left_ankle: BodyLandMarkCoordinates = landmarks[27]
        self.right_ankle: BodyLandMarkCoordinates = landmarks[28]
        self.left_heel: BodyLandMarkCoordinates = landmarks[29]
        self.right_heel: BodyLandMarkCoordinates = landmarks[30]
        self.left_foot_index: BodyLandMarkCoordinates = landmarks[31]
        self.right_foot_index: BodyLandMarkCoordinates = landmarks[32]


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cv.namedWindow("MediaPipe Pose", cv.WINDOW_NORMAL)

cap = cv.VideoCapture("Abbs.mp4")
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image.flags.writeable = False
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = pose.process(image)

        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
        )

        body = Body(results.pose_landmarks.landmark)

        cv.imshow("MediaPipe Pose", cv.flip(image, 1))

        if cv.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
