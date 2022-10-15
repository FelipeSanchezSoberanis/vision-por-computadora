---
title: Histogram Backprojection, MeanShift y CamShift
author: Felipe Sánchez Soberanis
date: 13 de octubre de 2022

toc: true
geometry: margin=1in
lang: es
---

\newpage
# Punto 1
## Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EWCqJUaSkJxAn1P5_WiSh3IBO9NPLgHKG3S-aTHjIy5qZw?e=ArnDLI](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EWCqJUaSkJxAn1P5_WiSh3IBO9NPLgHKG3S-aTHjIy5qZw?e=ArnDLI)

Como se puede observar, este método ofrece un muy buen seguimiento del objeto, pero, debido a que no cambia de tamaño, el ajuste al objeto no es tan bueno, especialmente cuando se aleja o acerca a la cámara, cambiando su tamaño dentro del cuadro de la imagen.

## Bibliografía

[https://elec-club-iitb.github.io/blog/2016/03/meanshift-algorithm-for-image-processing/](https://elec-club-iitb.github.io/blog/2016/03/meanshift-algorithm-for-image-processing/)

## Librerías

```python
import cv2 as cv
import numpy as np
```

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 2
## Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EbXc0wNLubtEknwF6Gx-CvUBui1TmWM4I-v4NpAvtJFXjQ?e=Z3vf9W](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EbXc0wNLubtEknwF6Gx-CvUBui1TmWM4I-v4NpAvtJFXjQ?e=Z3vf9W)

Como se puede observar, el método tiene un ajuste al objeto muy bueno, comparado al anterior. Pero, a pesar de esto, tiene una mayor sensibilidad al movimiento perpendicular del objeto respecto a la cámara, es decir, de adelante hacia atrás, ya que es cuando se presenta este tipo de movimiento cuando el seguimiento del objeto presenta los mayores errores.

## Bibliografía

[https://www.researchgate.net/figure/CAMshift-image-processing-for-region-of-interest_fig3_264174083](https://www.researchgate.net/figure/CAMshift-image-processing-for-region-of-interest_fig3_264174083)

## Librerías

```python
import cv2 as cv
import numpy as np
```

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 3
## Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EQKBMlwRnZ1KplwJeeUtsjQBGqcs-YRhURIFLusjkqw7Ng?e=P9T4XE](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EQKBMlwRnZ1KplwJeeUtsjQBGqcs-YRhURIFLusjkqw7Ng?e=P9T4XE)

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/ETpQAc2wMoFFok3NgCMjDi8BHPThF6qBh-wqwVf9YvgbYg?e=Q8zhDx](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/ETpQAc2wMoFFok3NgCMjDi8BHPThF6qBh-wqwVf9YvgbYg?e=Q8zhDx)

## Bibliografía
## Librerías

```python
import cv2 as cv
import argparse
import numpy as np
```

## Algoritmos propios

N/A.

## Problemas

N/A.

# Conclusión

A pesar de que, para la mayoría de los casos, camshift ofrecía y generaba un mejor ajuste al objeto que se deseaba buscar, parece que es demasiado sensible a ls distancia a la que se encuentra el objeto respecto a la cámara, ya que alejando el objeto provoca que este algoritmo se pierda y deje de marcar el objeto de manera correcta. Por el otro lado, meanshift tiene un peor ajuste al objeto, ya que no cambia de tamaño, pero el seguimiento del objeto es mucho mejor, comparado al anterior.

# Repositorio

[https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/08_histogram_backproject_meanshift_camshift](https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/08_histogram_backproject_meanshift_camshift)

