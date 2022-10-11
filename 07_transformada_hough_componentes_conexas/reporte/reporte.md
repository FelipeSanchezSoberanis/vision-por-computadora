---
title: Transformada de Hough y Componentes Conexas
author: Felipe Sánchez Soberanis
date: 10 de octubre de 2022

toc: true
geometry: margin=1in
lang: es
---

\newpage
# Punto 1
## Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EdCwnP9HJpxDmZSY9fdFqfcB0mdG4ryDEmgcG3BTznDgHw?e=4hwgav](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EdCwnP9HJpxDmZSY9fdFqfcB0mdG4ryDEmgcG3BTznDgHw?e=4hwgav)

Como se puede observar, el mayor problema con este método es que es muy dependiente de la iluminación que tiene el cuadro, es decir, es de suma importancia no tener sombras que pasen encima de la imagen, ya que esto hace que la detección de círculos disminuya considerablemente.

## Bibliografía

[https://www.sciencedirect.com/topics/computer-science/hough-transforms](https://www.sciencedirect.com/topics/computer-science/hough-transforms)

## Librerías

```python
import cv2 as cv
import numpy as np
import os
```

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 2
## Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EbiV08cTT0VPusd-UVcmLSYBAPV8INEoJWEREkaQ2IwYKg?e=T0sQmH](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EbiV08cTT0VPusd-UVcmLSYBAPV8INEoJWEREkaQ2IwYKg?e=T0sQmH)

A pesar de funcionar mejor que el método anterior, es súper dependiente de la calidad de la imagen, ya que bordes borrosos de monedas que se encuentran en proximidad, hacen que el algoritmo tenga un error y piense que es una sola entidad. Igual es importante mencionar que las sombras pueden lograr que las monedas parezcan más grandes de lo que son en realidad.

## Bibliografía

[https://pyimagesearch.com/2021/02/22/opencv-connected-component-labeling-and-analysis/](https://pyimagesearch.com/2021/02/22/opencv-connected-component-labeling-and-analysis/)

## Librerías

```python
import cv2 as cv
import os
import numpy as np
```

## Algoritmos propios

N/A.

## Problemas

N/A.


# Repositorio

[https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/07_transformada_hough_componentes_conexas](https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/07_transformada_hough_componentes_conexas)
