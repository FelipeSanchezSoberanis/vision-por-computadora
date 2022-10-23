from time import time
import cv2 as cv
import mediapipe as mp
from punto_1 import LandMarkCoordinates, distance_between_points


class Timer:
    start_time: float
    is_started: bool

    def start(self):
        self.start_time = time()
        self.is_started = True

    def stop(self):
        self.is_started = False

    def get_time_elapsed(self) -> float:
        return time() - self.start_time


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

cv.namedWindow("MediaPipe Face Mesh", cv.WINDOW_NORMAL)

cap = cv.VideoCapture("face_input.mp4")

timer = Timer()

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
) as face_mesh:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image = cv.flip(image, 0)

        image.flags.writeable = False
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style(),
                )
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style(),
                )
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style(),
                )

                left_eye_top: LandMarkCoordinates = face_landmarks.landmark[159]
                left_eye_bottom: LandMarkCoordinates = face_landmarks.landmark[145]
                right_eye_top: LandMarkCoordinates = face_landmarks.landmark[386]
                right_eye_bottom: LandMarkCoordinates = face_landmarks.landmark[374]

                if (
                    distance_between_points(left_eye_top, left_eye_bottom) < 0.01
                    and distance_between_points(right_eye_top, right_eye_bottom) < 0.01
                ):
                    if not timer.is_started:
                        timer.start()
                    elif timer.get_time_elapsed() > 3:
                        print("Asleep")
                    else:
                        print()
                else:
                    print()
                    timer.stop()

        cv.imshow("MediaPipe Face Mesh", image)

        if cv.waitKey(17) & 0xFF == ord("q"):
            break
cap.release()
