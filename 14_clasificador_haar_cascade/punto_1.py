import cv2 as cv


def main() -> None:
    cap = cv.VideoCapture("VID_20221030_234551_min.mp4")
    cv.namedWindow("video", cv.WINDOW_NORMAL)
    cascade_object: cv.CascadeClassifier = cv.CascadeClassifier(
        "classifier/cascade.xml"
    )

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image_gray: cv.Mat = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        ironman_positions = cascade_object.detectMultiScale(
            image_gray, scaleFactor=1.05, minSize=(50, 50), minNeighbors=0
        )

        print(len(ironman_positions))

        for (x, y, w, h) in ironman_positions:
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv.imshow("video", image)

        if cv.waitKey(int(1000 / 60)) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
