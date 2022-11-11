import cv2 as cv
import mediapipe as mp
from train_model import FaceRecognitionModel, models


#  SELECTED_MODEL: FaceRecognitionModel = models["Eigen"]
#  SELECTED_MODEL: FaceRecognitionModel = models["Fisher"]
SELECTED_MODEL: FaceRecognitionModel = models["LBPH"]


def main() -> None:
    mp_face_detection = mp.solutions.face_detection

    labels: list[str] = ["mask", "no_mask"]

    face_mask = SELECTED_MODEL.face_recognizer_method
    face_mask.read(SELECTED_MODEL.xml_name)

    cap = cv.VideoCapture(0)

    with mp_face_detection.FaceDetection(
        min_detection_confidence=0.5
    ) as face_detection:
        while True:
            ret: bool = cap.read()[0]
            frame: cv.Mat = cap.read()[1]

            if not ret:
                break

            frame: cv.Mat = cv.flip(frame, 1)

            height: int = frame.shape[0]
            width: int = frame.shape[1]

            frame_rgb: cv.Mat = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            results = face_detection.process(frame_rgb)

            if results.detections is None:
                continue

            for detection in results.detections:
                xmin: int = int(
                    detection.location_data.relative_bounding_box.xmin * width
                )
                ymin: int = int(
                    detection.location_data.relative_bounding_box.ymin * height
                )
                w: int = int(
                    detection.location_data.relative_bounding_box.width * width
                )
                h: int = int(
                    detection.location_data.relative_bounding_box.height * height
                )

                if xmin < 0 and ymin < 0:
                    continue

                face_image: cv.Mat = frame[ymin : ymin + h, xmin : xmin + w]
                face_image = cv.cvtColor(face_image, cv.COLOR_BGR2GRAY)
                face_image = cv.resize(
                    face_image, (72, 72), interpolation=cv.INTER_CUBIC
                )

                result = face_mask.predict(face_image)

                if result[1] >= 150:
                    continue

                color: tuple[int, int, int] = (
                    (0, 255, 0) if labels[result[0]] == "mask" else (0, 0, 255)
                )

                cv.putText(
                    frame,
                    "{}".format(labels[result[0]]),
                    (xmin, ymin - 15),
                    2,
                    1,
                    color,
                    1,
                    cv.LINE_AA,
                )

                cv.rectangle(frame, (xmin, ymin), (xmin + w, ymin + h), color, 2)

            cv.imshow("video", frame)

            if cv.waitKey(33) & 0xFF == ord("q"):
                break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
