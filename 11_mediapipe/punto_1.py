import cv2 as cv
import mediapipe as mp
import numpy as np


class HandPartCoordinates:
    def __init__(self):
        pass

    x: float
    y: float
    z: float


class Hand:
    def __init__(self, landmarks):
        self.finger_thumb = [landmarks[1], landmarks[2], landmarks[3], landmarks[4]]
        self.finger_pointer = [landmarks[5], landmarks[6], landmarks[7], landmarks[8]]
        self.finger_middle = [landmarks[9], landmarks[10], landmarks[11], landmarks[12]]
        self.finger_ring = [landmarks[13], landmarks[14], landmarks[15], landmarks[16]]
        self.finger_pinky = [landmarks[17], landmarks[18], landmarks[19], landmarks[20]]
        self.hand_base = landmarks[0]

    finger_thumb: list[HandPartCoordinates]
    finger_pointer: list[HandPartCoordinates]
    finger_middle: list[HandPartCoordinates]
    finger_ring: list[HandPartCoordinates]
    finger_pinky: list[HandPartCoordinates]
    hand_base: HandPartCoordinates


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
                break

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

                    hand = Hand(hand_landmarks.landmark)

                    #  ================================================================================
                    #  Detect rock
                    #  ================================================================================
                    if (
                        distance_between_points(hand.hand_base, hand.finger_ring[2])
                        < distance_between_points(hand.hand_base, hand.finger_ring[1])
                        and distance_between_points(
                            hand.hand_base, hand.finger_pinky[2]
                        )
                        < distance_between_points(hand.hand_base, hand.finger_pinky[1])
                        and distance_between_points(
                            hand.hand_base, hand.finger_pointer[2]
                        )
                        < distance_between_points(
                            hand.hand_base, hand.finger_pointer[1]
                        )
                        and distance_between_points(
                            hand.hand_base, hand.finger_middle[2]
                        )
                        < distance_between_points(hand.hand_base, hand.finger_middle[1])
                    ):
                        print("Rock")

                    #  ================================================================================
                    #  Detect scissors
                    #  ================================================================================
                    elif distance_between_points(
                        hand.hand_base, hand.finger_ring[2]
                    ) < distance_between_points(
                        hand.hand_base, hand.finger_ring[1]
                    ) and distance_between_points(
                        hand.hand_base, hand.finger_pinky[2]
                    ) < distance_between_points(
                        hand.hand_base, hand.finger_pinky[1]
                    ):
                        print("Scissors")

                    #  ================================================================================
                    #  Detect paper
                    #  ================================================================================
                    elif (
                        distance_between_points(
                            hand.finger_thumb[3], hand.finger_pointer[0]
                        )
                        < 0.1
                    ):
                        print("Paper")
                    else:
                        print()

            cv.imshow("MediaPipe Hands", image)
            if cv.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()


if __name__ == "__main__":
    main()
