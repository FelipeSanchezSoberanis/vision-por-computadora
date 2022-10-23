---
title: MediaPipe
author: Felipe Sánchez Soberanis
date: 26 de octubre de 2022

toc: true
geometry: margin=1in
lang: es
---

\newpage
# Punto 1
## Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/Ee78p1HPA7NMnMAqq-_MVdsBIPTl9pEk-VnJ7vKvYMmndA?e=AF6HfO](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/Ee78p1HPA7NMnMAqq-_MVdsBIPTl9pEk-VnJ7vKvYMmndA?e=AF6HfO)

Como se puede observar, la detección de la posición de los dedos de la mano para poder saber qué figura de piedra, papel y tijeras se está haciendo. La manera puede ser mucho más optimizada, ya que tiene muchos ifs repetidos, lo que afecta su rendimiento, como se puede observar cuando se detecta la piedra.

## Bibliografía

[https://google.github.io/mediapipe/solutions/hands.html](https://google.github.io/mediapipe/solutions/hands.html)

## Librerías

```python
import cv2 as cv
import mediapipe as mp
import numpy as np
```

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 2
## Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EUuo0_UJVW1EpA3gxx5cVwsBfVNRRfHMS9iXfbvdEL-Jkg?e=fCoysl](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EUuo0_UJVW1EpA3gxx5cVwsBfVNRRfHMS9iXfbvdEL-Jkg?e=fCoysl)

## Bibliografía

[https://google.github.io/mediapipe/solutions/pose.html](https://google.github.io/mediapipe/solutions/pose.html)

Como se puede observar, el conteo de abdominales funciona de la manera correcta, contando cuando la persona sobrepasa cierto ángulo y así se cuenta. Esto puede fallar si la persona no comienza acostada, pero puede ser resuelto con lógica adicional.

## Librerías

```python
import cv2 as cv
import mediapipe as mp
from punto_1 import LandMarkCoordinates
import numpy as np
```

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 3
## Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EaD3031FPzNOl7PQQBXUphYBCJxa65XZuLAOAkz8P6F4CQ?e=vldwiA](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EaD3031FPzNOl7PQQBXUphYBCJxa65XZuLAOAkz8P6F4CQ?e=vldwiA)

Se puede observar que todos los 300 puntos son reconocidos de manera correcta y, tomando en cuenta los puntos de arriba y abajo de los ojos, se puede obtener la distancia y saber si los ojos están cerrados. A esto se le suma un timer y se puede obtener cuando los ojos estén cerrados por más de 3 segundos.

## Bibliografía

[https://google.github.io/mediapipe/solutions/face_mesh.html](https://google.github.io/mediapipe/solutions/face_mesh.html)

## Librerías

```python
from time import time
import cv2 as cv
import mediapipe as mp
from punto_1 import LandMarkCoordinates, distance_between_points
```

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 4
## Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EbjBuZZnku1Kl0Q7qPg35dIB3ck7gS6GII0CmIKttTgfng?e=NWgIWJ](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EbjBuZZnku1Kl0Q7qPg35dIB3ck7gS6GII0CmIKttTgfng?e=NWgIWJ)

## Bibliografía

[https://google.github.io/mediapipe/solutions/selfie_segmentation.html](https://google.github.io/mediapipe/solutions/selfie_segmentation.html)

Se puede observar que el algoritmo funciona la mayoría del tiempo, cuando se pueden observar algunos fallos es cuando el fondo coincide el color con el de la camisa o de la cara de la persona en el frame.

## Librerías

```python
import cv2 as cv
import mediapipe as mp
import numpy as np
```

## Algoritmos propios

N/A.

## Problemas

N/A.

# Conclusiones

Esta librería es de suma utilidad para aplicaciones de algoritmos que trabajen con personas. A pesar de ser un proceso muy complejo, esta librería nos permite poder acceder a los resultados de un sistema ya entrenado, así permitiendo que nos centremos en la parte esencial de nuestro nuevo programa, ya sea contar las repeticiones de un ejercicio, detectar la posición de la mano para u njuego, o traducir de lenguaje de señar a algún idioma. Las aplicaciones que se pueden obtener de esta librería y sus componentenes son muy amplias.

# Repositorio

[https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/11_mediapipe](https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/11_mediapipe)

