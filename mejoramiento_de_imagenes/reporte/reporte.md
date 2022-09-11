---
title: "Mejoramiento de imágenes"
author: "Felipe Sánchez Soberanis"
date: "12 de septiembre de 2022"

lang: es
toc: true
geometry: margin=1in
---

\newpage

# Punto 1

## Resultados

![Resultado de la ecualización del histograma en la imagen.](reporte/media/punto_1_resultados_1.png){width=50%}

![Resultado de la ecualización del histograma.](reporte/media/punto_1_resultados_2.png){width=50%}

Como se puede observar, el resultado de ecualizar el histograma es que la imagen modificada tiene un mejor contraste, comparada la imagen original. Esto es debido a que, como se puede observar en el segundo histograma, los valores de brillo son mejor distribuidos a lo largo del rango 0 a 255.

## Bibliografía

N/A.

## Librerías

- opencv-contrib-python
- numpy
- matplotlib

## Algoritmos propios

**Calcular histograma de una imagen**:
```
imagen = ingresar imagen

ancho = imagen.ancho
alto = imagen.alto

x = 0 a 255, de 1 en 1
y = 256 0s

por cada w en ancho:
    por cada a en alto:
        v = imagen[w][a].intensidad_del_pixel
        y[v] += 1

regresar x, y
```

**Ecualizar histograma**:
```
imagen = ingresar imagen

ancho = imagen.ancho
alto = imagen.alto

y = calcular_histograma(imagen)

k = 255 / (ancho * alto)
suma = 0

imagen_ecualizada = zeros, ancho y alto igual al de imagen

por cada w en ancho:
    por cada a en alto:
        por cada s en intensidad_pixel(imagen[w][a]):
            suma += y[s]
        imagen_ecualizada[w][a] = k * suma
        suma = 0

regresar imagen_ecualizada
```

## Problemas

N/A.

\newpage
# Punto 2

## Resultados

![Comparación de la ecualización hecha por mi contra la ecualización de la librería OpenCV.](reporte/media/punto_2_resultados_1.png)

Visualmente, los resultados obtenidos por el algoritmo hecho desde 0 contra el algoritmo implementado en la librería de OpenCV, no es aparente. La mayor diferencia se encuentra en la velocidad con la que ambos algoritmos se llevan a cabo, ya que el propio, al estar hecho en Python, es mucho más lento que el de OpenCV, que se encuentra escrito en C y C++.

## Bibliografía

![Documentación de la función equalizeHist ([click aquí para ir](https://docs.opencv.org/4.x/d6/dc7/group__imgproc__hist.html#ga7e54091f0c937d49bf84152a16f76d6e)).](reporte/media/lib_opencv_equalizeHist.png)

## Librerías

- opencv-contrib-python
- matplotlib

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 3

## Resultados
## Bibliografía
## Librerías
## Algoritmos propios
## Problemas

\newpage
# Punto 4

## Resultados
## Bibliografía
## Librerías
## Algoritmos propios
## Problemas

\newpage
# Punto 5

## Resultados
## Bibliografía
## Librerías
## Algoritmos propios
## Problemas


