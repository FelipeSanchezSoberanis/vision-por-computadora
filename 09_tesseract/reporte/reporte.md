---
title: Tesseract
author: Felipe Sánchez Soberanis
date: 20 de octubre de 2022

toc: true
geometry: margin=1in
lang: es
---

\newpage
# Resultados

[https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/ETGRdOJU7ohBtjqZsmAut6gBp1pGCSQYGwylNRILPha1Yg?e=0r3UWX](https://alumnosuady-my.sharepoint.com/:v:/g/personal/a18214854_alumnos_uady_mx/ETGRdOJU7ohBtjqZsmAut6gBp1pGCSQYGwylNRILPha1Yg?e=0r3UWX)

Como se puede observar en el video, el funcionamiento de detectar la tarjeta que contiene la operación trabaja de la manera esperada. Lo que no se aprecia es la detección de la operación por medio de OCR. Esto puede ser, a mi parecer, debido a dos problemas principales: el grosor del plumón con el que puse los caracteres en las tarjetas, y/o el hecho de que las haya escrito a mano. Yo creo que es una combinación de ambos, ya que al final se puede apreciar como tesseract funciona de manera correcta cuando lo uso en la consola y le paso como argumento una imagen de una operación escrita a computadora que, de igual manera, tiene un mayor grosor.

# Bibliografía

[https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

[https://github.com/JaidedAI/EasyOCR](https://github.com/JaidedAI/EasyOCR)

# Librerías

```python
import cv2 as cv
import numpy as np
import pytesseract
```

# Algoritmos propios

N/A.

# Problemas

La detección de las operaciones escritas a mano y con un plumón no tan grueso es nula, es to se puede arreglar cambiando lo escrito en las tarjetas por impresiones de las operaciones que se desean detectar por medio del OCR, ya que este sí funciona de manera correcta en operaciones impresas.

# Repositorio

[https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/09_tesseract](https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/09_tesseract)

