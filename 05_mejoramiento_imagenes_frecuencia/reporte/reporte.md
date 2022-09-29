---
title: Mejoramiento y reconstrucción de imágenes en el dominio de la frecuencia
author: Felipe Sánchez Soberanis
date: 26 de septiembre de 2022

toc: true
geometry: margin=1in
---

\newpage
# Punto 1

## Resultados

![Resultados del punto 1.](reporte/punto_1_resultados_1.png)

Como se puede observar, el mejor resultado es obtenido en la imagen del paisaje, ya que es la que contiene más información, permitiendo que el algoritmo tenga más información con la que trabajar, contrario al meteorito, que tiene una gran parte de su información en un color sumamente oscuro.

## Bibliografía

N/A.

## Librerías

- opencv-contrib-python
- numpy
- matplotlib

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 2

## Resultados

![Resultados del punto 2.](reporte/punto_2_resultados_1.png)

Se puede observar claramente cómo el filtro logra que los contornos de la mujer, y del fondo, sean aumentados, permitiendo que las orillas y diferencias entre objetos sean más evidentes, logrando la meta del ejercicio.

## Bibliografía

N/A.

## Librerías

- opencv-contrib-python
- numpy
- matplotlib

## Algoritmos propios

N/A.

## Problemas

N/A.

\newpage
# Punto 3

![](reporte/punto_3_resultados_1.png)

![](reporte/punto_3_resultados_2.png)

![](reporte/punto_3_resultados_3.png)

![](reporte/punto_3_resultados_4.png)

\newpage
# Punto 4

## Resultados

![Resultados del punto 4.](reporte/punto_4_resultados_1.png)

Se puede observar que el filtro de movimiento es mejor combatido por el método de Wiener, mientras que, para el caso del filtro inverso, el resultado es peor que la entrada, indicando que es el menos indicado para este tipo de ruido o, al menos, para la magnitud del ruido.

## Bibliografía

N/A.

## Librerías

- opencv-contrib-python
- numpy
- matplotlib

## Algoritmos propios

N/A.

## Problemas

N/A.


\newpage
# Repositorio

[https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/mejoramiento_imagenes_frecuencia](https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/mejoramiento_imagenes_frecuencia)

# Conclusiones

Estos filtro, especialmente el de high boost para poder resaltar las orillas de las imágenes, son una gran herramiento para poder complementar los filtros visto con anterioridad que pueden combatir una gran cantidad de ruido, lo que quiere decir que estos ruidos logran que la información que se pasa a los algoritmos de visión por computadora sea lo más adecuada posible para cada aplicación que se necesite.

