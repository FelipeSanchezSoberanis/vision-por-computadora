---
title: Clasificador Haar Cascade
author: Felipe Sánchez Soberanis
date: 7 de noviembre de 2022

toc: true
geometry: margin=1in
lang: es
---

\newpage
# Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EVmE5hFs7Z1LmXUvu7Z4Ih4BrUMXFCiEjLhfj5J8QsESAg?e=d6ExoO](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/EVmE5hFs7Z1LmXUvu7Z4Ih4BrUMXFCiEjLhfj5J8QsESAg?e=d6ExoO)

Como se puede observar en el video, el entrenamiento que se realizó no otorgó un resultado satisfactorio al nivel esperado. El reconocimiento del objeto se logra apreciar hasta el final del video y ni siquiera en el lugar correcto.

# Bibliografía

[https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d](https://medium.com/analytics-vidhya/haar-cascades-explained-38210e57970d)

[https://www.educba.com/opencv-haar-cascade/](https://www.educba.com/opencv-haar-cascade/)

[https://www.geeksforgeeks.org/python-haar-cascades-for-object-detection/](https://www.geeksforgeeks.org/python-haar-cascades-for-object-detection/)

# Librerías

```python
import cv2 as cv
```

# Algoritmos propios

N/A.

# Problemas

Como se mencionó en la sección de resultados, el reconocimiento del objeto no fue satisfactorio. Esto es, a mi parecer, debido a varios posibles problemas:

1. La cantidad de imágenes que usé para el entramiento no son suficientes.
2. El ángulo de las imágenes no es el correcto o la iluminación no es la adecuada.
3. El tamaño de las imagenes no cuadra con el tamaño de la ventada utilizada para realizar el entrenamiento.

Cualquier de los 3 puntos anteriores o, la combinación de estos, pueden llevar a la conclusión que se puede observar en el video.

# Repositorio

[https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/14_clasificador_haar_cascade](https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/14_clasificador_haar_cascade)

