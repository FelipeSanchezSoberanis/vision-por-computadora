from typing import Any
import cv2 as cv
import os
import numpy as np


class FaceRecognitionModel:
    def __init__(self, method: Any, xml_name: str):
        self.face_recognizer_method = method
        self.xml_name = xml_name

    face_recognizer_method: Any
    xml_name: str


models: dict[str, FaceRecognitionModel] = {
    "LBPH": FaceRecognitionModel(
        cv.face.LBPHFaceRecognizer.create(), "mask_model_LBPH.xml"
    ),
    "Eigen": FaceRecognitionModel(
        cv.face.EigenFaceRecognizer.create(), "mask_model_eigen.xml"
    ),
    "Fisher": FaceRecognitionModel(
        cv.face.FisherFaceRecognizer.create(), "mask_model_fisher.xml"
    ),
}


def main() -> None:
    data_path: str = os.path.join("data")
    dir_list: list[str] = os.listdir(data_path)

    labels: list[int] = []
    faces_data: list[cv.Mat] = []
    label: int = 0

    for name_dir in dir_list:
        dir_path: str = os.path.join(data_path, name_dir)

        for file_name in os.listdir(dir_path):
            image_path: str = os.path.join(dir_path, file_name)
            image: cv.Mat = cv.imread(image_path, 0)

            faces_data.append(image)
            labels.append(label)

        label += 1

    for _, model in models.items():
        face_mask = model.face_recognizer_method
        face_mask.train(faces_data, np.array(labels))
        face_mask.write(model.xml_name)


if __name__ == "__main__":
    main()
