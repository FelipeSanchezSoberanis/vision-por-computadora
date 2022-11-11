---
title: Reconocimiento de Rostros
author: Felipe Sánchez Soberanis
date: 10 de noviembre de 2022

toc: true
geometry: margin=1in
lang: es
---

\newpage
# Resultados

Video: [https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EdwmtwwcOiBBs0MW7MINjfYBn74ZN9oG1_GpRoXtMk2vEA?e=dbn952](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EdwmtwwcOiBBs0MW7MINjfYBn74ZN9oG1_GpRoXtMk2vEA?e=dbn952)

Fisher XML: [https://alumnosuady-my.sharepoint.com/:u:/g/personal/a18214854_alumnos_uady_mx/EW_WjYfLgHBLhIGUlNaBa5gBa1Sg4V4T8YP-P4SruDHzYA?e=fNwrWn](https://alumnosuady-my.sharepoint.com/:u:/g/personal/a18214854_alumnos_uady_mx/EW_WjYfLgHBLhIGUlNaBa5gBa1Sg4V4T8YP-P4SruDHzYA?e=fNwrWn)

Eigen XML: [https://alumnosuady-my.sharepoint.com/:u:/g/personal/a18214854_alumnos_uady_mx/EYVZkgvO6jVBgA84EkVx_JkBCZNMmRZMwPSWyJRXrH6isw?e=kQgfmp](https://alumnosuady-my.sharepoint.com/:u:/g/personal/a18214854_alumnos_uady_mx/EYVZkgvO6jVBgA84EkVx_JkBCZNMmRZMwPSWyJRXrH6isw?e=kQgfmp)

LBPH XML: [https://alumnosuady-my.sharepoint.com/:u:/g/personal/a18214854_alumnos_uady_mx/EZ_-d9hUgR9DpvnJ09H3uDwBUxGMfVuKxE2J21FEr360Pg?e=8Q0JE8](https://alumnosuady-my.sharepoint.com/:u:/g/personal/a18214854_alumnos_uady_mx/EZ_-d9hUgR9DpvnJ09H3uDwBUxGMfVuKxE2J21FEr360Pg?e=8Q0JE8)

Como se puede observar en el video, el mejor método es el LBPH, el segundo es el de Fisher y, por último, el de Eigen. El de LBPH es el más robusto, soportando incluso el movimiento de la cara mientras se realiza la detección. En el caso de Fisher, la detección, si la cara se encuentra estática, es bastante buena, pero el movimiento del sujeto provoca que se presentan fallos. Finalmente, el método Eigen, no realiza ni siquiera la detección de caras, ni mucho menos, la detección de mascarilla. Ver la sección de problemas para posibles motivos.

# Bibliografía

[https://docs.opencv.org/4.6.0/d4/d48/namespacecv_1_1face.html](https://docs.opencv.org/4.6.0/d4/d48/namespacecv_1_1face.html)

[https://docs.opencv.org/4.6.0/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html](https://docs.opencv.org/4.6.0/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html)

[https://docs.opencv.org/4.6.0/d2/de9/classcv_1_1face_1_1FisherFaceRecognizer.html](https://docs.opencv.org/4.6.0/d2/de9/classcv_1_1face_1_1FisherFaceRecognizer.html)

[https://docs.opencv.org/4.6.0/dd/d7c/classcv_1_1face_1_1EigenFaceRecognizer.html](https://docs.opencv.org/4.6.0/dd/d7c/classcv_1_1face_1_1EigenFaceRecognizer.html)

# Librerías

Para entrenar el modelo:
```python
from typing import Any
import cv2 as cv
import os
import numpy as np
```

Para probar el modelo:
```python
import cv2 as cv
import mediapipe as mp
from train_model import FaceRecognitionModel, models
```

# Algoritmos propios

N/A.

# Problemas

El modelo que utiliza el algoritmo de Eigen no presenta ni siquiera el reconocimiento de las caras. Esto puede ser por diversos motivos, pero, después de un poco de lectura, puede que el más probable sea la diferencia de tamaño en las imágenes de entrenamiento y el video que se utiliza, ya que este algoritmo espera que el tamaño sea igual durante todo el proceso.

# Repositorio

[https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/15_reconocimiento_rostros](https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/15_reconocimiento_rostros)

