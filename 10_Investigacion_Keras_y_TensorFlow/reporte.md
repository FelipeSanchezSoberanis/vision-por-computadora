---
title: Investigacion Keras y TensorFlow
author: Felipe Sánchez Soberanis
date: 20 de octubre de 2022

toc: true
geometry: margin=1in
lang: es
---

# Keras

## Sobre Keras

Keras es una API de aprendizaje profundo escrita en Python, que se ejecuta sobre la plataforma de aprendizaje automático TensorFlow. Se desarrolló con el objetivo de permitir una experimentación rápida. Poder pasar de la idea al resultado lo más rápido posible es clave para hacer una buena investigación.

Keras es:

- Simple - pero no simplista. Keras reduce la carga cognitiva del desarrollador para que pueda centrarse en las partes del problema que realmente importan.
- Flexible -- Keras adopta el principio de divulgación progresiva de la complejidad: los flujos de trabajo simples deben ser rápidos y fáciles, mientras que los flujos de trabajo arbitrariamente avanzados deben ser posibles a través de un camino claro que se basa en lo que ya has aprendido.
- Potente -- Keras proporciona un rendimiento y una escalabilidad de nivel industrial: lo utilizan organizaciones y empresas como la NASA, YouTube o Waymo.

## Keras y TensorFlow 2

TensorFlow 2 es una plataforma de aprendizaje automático de extremo a extremo y de código abierto. Puedes pensar en ella como una capa de infraestructura para la programación diferenciable. Combina cuatro habilidades clave:

- Ejecución eficiente de operaciones tensoriales de bajo nivel en la CPU, GPU o TPU.
- Calcular el gradiente de expresiones diferenciables arbitrarias.
- Escalar el cálculo a muchos dispositivos, como clusters de cientos de GPUs.
- Exportación de programas ("gráficos") a tiempos de ejecución externos, como servidores, navegadores y dispositivos móviles e integrados.

Keras es la API de alto nivel de TensorFlow 2: una interfaz accesible y altamente productiva para resolver problemas de aprendizaje automático, con un enfoque en el aprendizaje profundo moderno. Proporciona abstracciones esenciales y bloques de construcción para desarrollar y enviar soluciones de aprendizaje automático con una alta velocidad de iteración.

Keras permite a los ingenieros e investigadores aprovechar al máximo la escalabilidad y las capacidades multiplataforma de TensorFlow 2: puede ejecutar Keras en TPU o en grandes clusters de GPU, y puede exportar sus modelos Keras para ejecutarlos en el navegador o en un dispositivo móvil.

## Características

Keras contiene numerosas implementaciones de bloques de construcción de redes neuronales de uso común, como capas, objetivos, funciones de activación, optimizadores y una serie de herramientas que facilitan el trabajo con datos de imagen y texto para simplificar la codificación necesaria para escribir código de redes neuronales profundas. El código está alojado en GitHub, y los foros de apoyo de la comunidad incluyen la página de problemas de GitHub y un canal de Slack.

Además de las redes neuronales estándar, Keras es compatible con las redes neuronales convolucionales y recurrentes. Soporta otras capas de utilidad común como el abandono, la normalización por lotes y la agrupación.

Keras permite a los usuarios producir modelos profundos en smartphones (iOS y Android), en la web o en la máquina virtual de Java. También permite el uso de entrenamiento distribuido de modelos de aprendizaje profundo en clusters de unidades de procesamiento gráfico (GPU) y unidades de procesamiento tensorial (TPU).

# Tensorflow

## Sobre Tensorflow

TensorFlow es una biblioteca de software libre y de código abierto para el aprendizaje automático y la inteligencia artificial. Puede utilizarse en una amplia gama de tareas, pero se centra especialmente en el entrenamiento y la inferencia de redes neuronales profundas.

TensorFlow fue desarrollado por el equipo de Google Brain para el uso interno de Google en la investigación y la producción La versión inicial fue lanzada bajo la licencia Apache 2.0 en 2015 Google lanzó la versión actualizada de TensorFlow, llamada TensorFlow 2.0, en septiembre de 2019.

TensorFlow se puede utilizar en una amplia variedad de lenguajes de programación, como Python, JavaScript, C++ y Java Esta flexibilidad se presta a una serie de aplicaciones en muchos sectores diferentes.

## Características

- AutoDiferenciación: La AutoDiferenciación es el proceso de calcular automáticamente el vector gradiente de un modelo con respecto a cada uno de sus parámetros. Con esta función, TensorFlow puede calcular automáticamente los gradientes de los parámetros de un modelo, lo que resulta útil para algoritmos como la retropropagación, que requieren gradientes para optimizar el rendimiento. Para ello, el marco debe hacer un seguimiento del orden de las operaciones realizadas a los Tensores de entrada en un modelo, y luego calcular los gradientes con respecto a los parámetros apropiados.

- Ejecución ansiosa - TensorFlow incluye un modo de "ejecución ansiosa", lo que significa que las operaciones son evaluadas inmediatamente en lugar de ser añadidas a un gráfico computacional que se ejecuta más tarde El código ejecutado de forma ansiosa puede ser examinado paso a paso a través de un depurador, ya que los datos se aumentan en cada línea de código en lugar de más tarde en un gráfico computacional Este paradigma de ejecución se considera más fácil de depurar debido a su transparencia paso a paso.

- Distribuir - Tanto en las ejecuciones eager como en las ejecuciones graph, TensorFlow proporciona una API para distribuir la computación a través de múltiples dispositivos con varias estrategias de distribución Esta computación distribuida puede a menudo acelerar la ejecución del entrenamiento y la evaluación de los modelos TensorFlow y es una práctica común en el campo de la IA.

- Pérdidas - Para entrenar y evaluar los modelos, TensorFlow proporciona un conjunto de funciones de pérdida (también conocidas como funciones de coste) Algunos ejemplos populares incluyen el error cuadrático medio (MSE) y la entropía cruzada binaria (BCE) Estas funciones de pérdida calculan el "error" o la "diferencia" entre la salida de un modelo y la salida esperada (más ampliamente, la diferencia entre dos tensores). Para diferentes conjuntos de datos y modelos, se utilizan diferentes pérdidas para priorizar ciertos aspectos del rendimiento.

- Métrica - Para evaluar el rendimiento de los modelos de aprendizaje automático, TensorFlow da acceso a la API a las métricas más utilizadas. Los ejemplos incluyen varias métricas de precisión (binaria, categórica, categórica dispersa) junto con otras métricas como Precisión, Recall e Intersección sobre la Unión (IoU).

- TF.nn - TensorFlow.nn es un módulo para ejecutar operaciones primitivas de redes neuronales en los modelos Algunas de estas operaciones incluyen variaciones de convoluciones (1/2/3D, Atrous, depthwise), funciones de activación (Softmax, RELU, GELU, Sigmoid, etc.) y sus variaciones, y otras operaciones de Tensor (max-pooling, bias-add, etc.).

- Optimizadores - TensorFlow ofrece un conjunto de optimizadores para el entrenamiento de redes neuronales, incluyendo ADAM, ADAGRAD, y Stochastic Gradient Descent (SGD) Cuando se entrena un modelo, los diferentes optimizadores ofrecen diferentes modos de ajuste de parámetros, que a menudo afectan a la convergencia y el rendimiento de un modelo.

## Aplicaciones

- Medicina: GE Healthcare utilizó TensorFlow para aumentar la velocidad y la precisión de las resonancias magnéticas en la identificación de partes específicas del cuerpo. Google utilizó TensorFlow para crear DermAssist, una aplicación móvil gratuita que permite a los usuarios tomar fotos de su piel e identificar posibles complicaciones de salud. Sinovation Ventures utilizó TensorFlow para identificar y clasificar enfermedades oculares a partir de escaneos de tomografía de coherencia óptica (OCT).

- Redes sociales: Twitter implementó TensorFlow para clasificar los tuits según su importancia para un determinado usuario, y cambió su plataforma para mostrar los tuits en orden de esta clasificación. Anteriormente, los tuits se mostraban simplemente en orden cronológico inverso. La aplicación para compartir fotos VSCO utilizó TensorFlow para ayudar a sugerir filtros personalizados para las fotos.

- Motor de búsqueda: Google lanzó oficialmente RankBrain el 26 de octubre de 2015, respaldado por TensorFlow.

- Educación: InSpace, una plataforma de aprendizaje virtual, utilizó TensorFlow para filtrar los mensajes de chat tóxicos en las aulas. Liulishuo, una plataforma de aprendizaje de inglés en línea, utilizó TensorFlow para crear un plan de estudios adaptativo para cada estudiante. TensorFlow se utilizó para evaluar con precisión las capacidades actuales de un estudiante, y también ayudó a decidir el mejor contenido futuro para mostrar en función de esas capacidades.

- Venta al por menor: La plataforma de comercio electrónico Carousell utilizó TensorFlow para ofrecer recomendaciones personalizadas a los clientes. La empresa de cosméticos ModiFace utilizó TensorFlow para crear una experiencia de realidad aumentada para que los clientes pudieran probar varios tonos de maquillaje en su rostro.

