---
title: Filtros en el Dominio de la Frecuencia
author: Felipe Sánchez Soberanis
date: 19 de septiembre de 2022

lang: es
toc: true
geometry: margin=1in
---

\newpage
# Punto 1

## Muestreo

**Definición técnica**: El muestreo es el proceso mediante el cual se selecciona un grupo de observaciones que pertenecen a una población. Esto, con el fin de realizar un estudio estadístico.

El muestreo, en otras palabras, es el procedimiento mediante el cual se toman a ciertos individuos que pertenecen a una población que está siendo sujeto de un análisis.

El muestreo es necesario por el hecho de que las poblaciones pueden ser demasiado grandes y no es factible (económica y materialmente hablando) tomar datos de todos los individuos.

El objetivo es que la muestra sea representativa. Es decir, que sus indicadores como la media de edad, el ingreso promedio, el porcentaje de hombres y de mujeres, entre otros, sea el mismo, o muy similar al de la población.

Los tipos de muestreo pueden distinguirse en función de distintos criterios. Así, según la técnica para seleccionar el subgrupo, se pueden diferenciar los siguientes:

**Muestreo probabilístico**: Las observaciones son seleccionadas en base a la aleatoriedad, es decir, al azar. En esta categoría podemos encontrar:

- **Muestreo aleatorio simple**: Todos los individuos de la población tienen la misma probabilidad de ser elegidos como parte de la muestra. Tiene ventajas, como el hecho de que es fácil de llevar a cabo a través de sistemas informáticos. Sin embargo, se requiere el listado completo de toda la población y, si la muestra es muy pequeña, la selección podría no ser representativa. Sistemático: Se elige una observación al azar y, para seleccionar el resto de la muestra, se utilizan intervalos numéricos regulares. Es decir, supongamos que tengo una población de 10.000 y, aleatoriamente, selecciono la observación 600, después de lo cual puedo considerar intervalos de 30 observaciones. En este caso, tomaría las observaciones 600, 630, 660, 690, 720, 750, 780, y así sucesivamente.
- **Aleatorio estratificado**: Se divide a la población en estratos, que son grupos que comparten características en común y son más homogéneos, inclusive, que la población en su conjunto. Entonces, se selecciona una muestra, ya sea de manera aleatoria o sistemática, dentro de cada estrato. El objetivo es lograr una representatividad de cada estrato.
- **Por conglomerados o clústeres**: Consiste en crear grupos más pequeños que la población, los cuales reflejen o compartan todas las características de esta. Luego, elegimos alguno de los conglomerados como muestra y lo analizamos de forma detallada.

**Muestreo no probabilístico**: La selección de la muestra no depende de la probabilidad, sino de la decisión de los investigadores. Podemos distinguir algunas subcategorías:

- **Por conveniencia**: Consiste en que el investigador captará a los sujetos que estén a su disponibilidad. Por ejemplo, por su proximidad o facilidad de acceso.
- **Método opinático o intencional**: El investigador utiliza su juicio o criterio para elegir a quienes van a participar como parte de la muestra.
- **Casual o accidental**: El investigador selecciona sin juicio previo a los individuos que van a formar parte de la muestra. Por ejemplo, esto suele suceder cuando se hacen encuestas en la calle.
- **Bola de nieve**: Consiste en que, después de encontrar al primer sujeto (o primeros sujetos) de la muestra, el investigador le pide ayuda a él (o ellos) para identificar a otros individuos con esas mismas características. Se trata de una técnica utilizada cuando es difícil localizar a un grupo específico por el manejo de datos sensibles, por ejemplo, emigrantes en situación de ilegalidad.
- **Por cuotas**: El investigador, tomando en cuenta la composición de la población, y dividiendo por grupos o estratos, hará una selección proporcional de la muestra. Por ejemplo, imaginemos que en la población hay un 40% de personas menores de 25 años, 35% de personas de entre 25 y 50 años, y 25% de individuos con más de 50 años. Entonces, una muestra de 4.000 personas tendría 1.600 sujetos menores de 25 años, 1.400 de entre 25 y 50 años, y 1.000 adultos mayores de 50 años o más. Cabe señalar que los individuos que cubrirán cada cuota serán seleccionados por algún método no probabilístico, es decir, cualquiera de las técnicas explicadas líneas arriba.

## Transformada de Fourier

Este concepto matemático fue presentado por Joseph B. Fourier en el año 1811 mientras desarrollaba un tratado referente a la propagación de calor. Rápidamente fue adoptado por diversas ramas de la ciencia e ingeniería.

Se estableció como principal herramienta de trabajo en el estudio de las ecuaciones con derivadas parciales, comparándose incluso con la relación de trabajo existente entre la transformada de Laplace y las ecuaciones diferenciales ordinarias.

¿Para qué sirve la transformada de Fourier?
Sirve principalmente para simplificar de manera notable las ecuaciones, mientras transforma expresiones derivadas en elementos de potencia, que denotan expresiones diferenciales en forma de polinomios integrables.

En la optimización, modulación y modelación de resultados actúa como expresión estandarizada, siendo un recurso frecuente para la ingeniería tras varias generaciones.

La serie de Fourier
Son series definidas en términos de Cosenos y Senos; sirven para facilitar el trabajo con funciones periódicas generales. Al aplicarse forman parte de las técnicas de resolución de ecuaciones diferenciales parciales y ordinarias.

Las series de Fourier son incluso más generales que las series de Taylor, debido a que desarrollan funciones discontinuas periódicas que no tienen representación en series de Taylor.

El motivo general de la aplicación de la transformada de Fourier en esta rama se debe mayormente a la descomposición característica de una señal como superposición infinita de señales más fácilmente tratables.

Puede tratarse de una onda de sonido o una onda electromagnética, la transformada de Fourier la expresa en una superposición de ondas simples. Esta representación es bastante frecuente en ingeniería eléctrica.

\newpage
# Punto 2

## Resultados

![Resultados del punto 2.](reporte/punto2_resultados_1.png)

Como se puede observar, los mejores resultados son dado por el método Gaussiano, ya que da resultados con menos artefactos, comparado con los demás, que tiene unas línas curvas alrededor de toda la imagen.

## Bibliografía

N/A.

## Librerías

- opencv-contrib-python
- matplotlib
- numpy

## Algoritmos propios

N/A.

## Problemas

\newpage
# Punto 3

## Resultados

![Resultados del punto 3.](reporte/punto3_resultados_1.png)

En las imágenes se puede observar que, nuevamente, el mejor resultado es dado por el método Gaussiano, ya que, a pesar de tener un valor menor de brillo en los bordes, es el que tiene una mejor separación entre bajas y altras frecuencias, permitiendo una mejor detección de bordes.

## Bibliografía

N/A.

## Librerías

- opencv-contrib-python
- matplotlib
- numpy

## Algoritmos propios

N/A.

## Problemas

\newpage
# Punto 4

## Resultados

![Resultados del punto 4.](reporte/punto4_resultados_1.png)

Nuevamente, el método Gaussiano da los mejores resultados, ya que es el que logra combinar de mejor manera, y más suave, la combinación de altas con bajas frecuencias, logrando generar una imagen más clara.

## Bibliografía

N/A.

## Librerías

- opencv-contrib-python
- matplotlib
- numpy

## Algoritmos propios

N/A.

## Problemas

\newpage
# Punto 5

## Resultados

![Resultados del punto 5.](reporte/punto5_resultados_1.png)

A pesar de, al parecer, usar el algoritmo correcto, parece que los métodos no alteran la imagen original.

## Bibliografía

N/A.

## Librerías

- opencv-contrib-python
- matplotlib
- numpy

## Algoritmos propios

N/A.

## Problemas

\newpage
# Conclusiones

Los filtros de frecuencias vistos en esta tarea son, a mi parecer, de los más importantes que se pueden realizar para pre procesar imágenes antes de pasarlas por un sistema de visión por computadora. Por ejemplo, los filtros pasa altas son súper útiles para la detección de bordes, lo cual es súper útil par apoder detectar el principio y fin de objetos en el espacio, permitiendo al algoritmo de visión por computadora realizar operaciones sobre esa información, como sería, por ejemplo, detectar el nivel de llenado de una botella de cristal en un sistema de producción refresquero.

# Repositorio

[https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/filtros_dominio_frecuencia](https://github.com/FelipeSanchezSoberanis/vision-por-computadora/tree/main/filtros_dominio_frecuencia)
