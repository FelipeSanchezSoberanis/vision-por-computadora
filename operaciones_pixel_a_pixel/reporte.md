---
title: Operaciones pixel a pixel
author: Felipe Sánchez Soberanis
date: 5 de septiembre de 2022

toc: true
geometry: margin=1in
---

\newpage
# Punto 1

## Resultados

![Resultados punto 1.](reporte-media/resultados-punto-1.png)

Aquí se pueden observar las 12 posibles combinaciones (4 resoluciones y 3 diferentes métodos de interpolación).
Comparando visualmente los resultados obtenidos, el método de vecino más cercano tiende a dar resultados menos suaves que los otros métodos, ya que el método lineal y cúbico dan resultados más parecidos entre sí. Esto se hace más obvio cuando se aumenta la resolución de la imagen, ya que cuando se disminuye, los resultados no son obvios, debido a los poco pixeles de la imagen.

## Bibliografía

![Documentación de la función resize ([click aquí para ir](https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d)).](reporte-media/cv-resize.png)

## Librerías

- opencv-contrib-python
- numpy

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 2

## Resultados

![Resultados punto 2.](reporte-media/resultados-punto-2.png)

Aquí se puede observar del lado izquierdo la diferencia entre el frame actual y el frame pasado del video captado con la cámara de video de mi celular.

## Bibliografía

![Documentación de la función absdiff ([click aquí para ir](https://docs.opencv.org/4.x/d2/de8/group__core__array.html#ga6fef31bc8c4071cbc114a758a2b79c14)).](reporte-media/cv-absdiff.png)

## Librerías

- opencv-contrib-python

## Algoritmos propios

N/A.

## Problemas

La cámara de mi computadora no funciona, pero usé la aplicación DroidCam para poder obtener el video de mi celular y usarlo dentro de mi computadora.

\newpage
# Punto 3

## Resultados

![Resultados punto 3.](reporte-media/resultados-punto-3.png)

Aquí se pueden observar las 3 imágenes y cómo se ven afectadas con el cambio de gamma. El valor nuevo de la gamma se define por medio del slider de la imagen de arriba a la izquierda. A pesar de que visualmente tiene un rango de 0 a 1000, hay una función que normaliza el rango al requerido de 0.01 a 4 para cumplir con los requerimientos.

## Bibliografía

![Documentación de la función LUT ([click para ir](https://docs.opencv.org/4.x/d2/de8/group__core__array.html#gab55b8d062b7f5587720ede032d34156f)).](reporte-media/cv-lut.png)

![Documentación de la función interp ([click para ir](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy-interp)).](reporte-media/np-interp.png)

![Documentación de la función createTrackbar ([click para ir](https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#gaf78d2155d30b728fc413803745b67a9b)).](reporte-media/cv-createTrackbar.png)

\newpage

## Librerías

- opencv-contrib-python
- numpy

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 4

## Resultados

![Resultados punto 3 (histograma).](reporte-media/resultados-punto-4-histograma.png)

![Resultados punto 3 (binarización).](reporte-media/resultados-punto-4.png)

Aquí se puede observar el histrograma generado, el cual indica que el valor más brillante de la imagen es entre 100 y 130, lo quiere decir que ese rango de valores es el que se tiene que pasar a la función de binarización para poder separar el objeto más brillante de la imagen. El resultado de esta binarización se puede observar en la siguiente imagen.

\newpage
## Bibliografía

![Documentación de la función calcHist ([click para ir](https://docs.opencv.org/4.x/d6/dc7/group__imgproc__hist.html#ga4b2b5fd75503ff9e6844cc4dcdaed35d)).](reporte-media/cv-calcHist.png)

![Documentación de la función threshold ([click para ir](https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57)).](reporte-media/cv-threshold.png)

## Librerías

- opencv-contrib-python
- numpy
- matplotlib

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Conclusiones

A pesar de que los algoritmos de esta tarea se centran totalmente en el procesamiento de imágenes, son de suma utilidad para poder preparar la información que estas contienen y poder pasar propiamente a algoritmos de visión por computadora y lograr que estos funcionen de manera óptima o, aunque sea, de manera más eficiente. Esto debido a que el pre procesamiento de las imagenes que estos algoritmos van a utilizar logra que funcionen más pegados a su rendimiento teórico, lo que quiere decir que pueden proveer mejores resultados, que, al final de cuentas, es lo que a las personas que los utilizan les interesa.

# Código

[Repositorio de Github.](https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/operaciones_pixel_a_pixel)

