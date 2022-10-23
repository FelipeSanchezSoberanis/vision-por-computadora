import cv2 as cv
import mediapipe as mp
import numpy as np


def distance_between_points(point_1, point_2):
    return np.sqrt(np.square(point_2.x - point_1.x) + np.square(point_2.y - point_1.y))


def main() -> None:
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    cv.namedWindow("MediaPipe Hands", cv.WINDOW_NORMAL)

    cap = cv.VideoCapture("rock_paper_scissors_input_720.mp4")
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
        max_num_hands=1,
    ) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            image.flags.writeable = False
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            results = hands.process(image)

            image.flags.writeable = True
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style(),
                    )

                    thumb_finger = hand_landmarks.landmark[4]
                    index_finger = hand_landmarks.landmark[8]
                    middle_finger = hand_landmarks.landmark[12]
                    ring_finger = hand_landmarks.landmark[16]
                    ring_finger_base = hand_landmarks.landmark[13]
                    pinky_finger = hand_landmarks.landmark[20]
                    pinky_finger_base = hand_landmarks.landmark[17]

            cv.imshow("MediaPipe Hands", image)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()


if __name__ == "__main__":
    main()
