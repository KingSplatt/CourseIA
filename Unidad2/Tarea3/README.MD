## Tarea 3 - unidad2

Clasificador de correos, en esta tarea se busca identificar aquellos correos cuales tienen ciertas peculiaridades que lo hacen notarse como un correo de SPAM, para ello hay que saber unas cuantas caracteristicas acerca de cuando un correo se hace notar por uno de estos tipos:

- Solicitudes urgenes o amanezanates
- Enlaces sospechosos o acortados
- Archivos adjuntos inesperados
- Encabezados o saludos genericos ("Querido usuario","Estimado cliente")
- Oferas demasiadas buenas para ser verdad

### Teoria de la probabilidad. ¿Nos sirve para estos casos?

La teoría de probabilidades se ocupa de asignar un cierto número a cada posible resultado que pueda ocurrir en un experimento aleatorio, con el fin de cuantificar dichos resultados y saber si un suceso es más probable que otro.

### Teorema de Bayes

El teorema de Bayes establece una forma de calcular la probabilidad de un evento, teniendo en cuenta la probabilidad de eventos relacionados previamente observados. En otras palabras, nos permite actualizar nuestras creencias sobre la probabilidad de un evento a medida que obtenemos nueva información.

El Teorema de Bayes es una herramienta fundamental en el análisis estadístico y la toma de decisiones. Fue desarrollado por el matemático inglés Thomas Bayes en el siglo XVIII y desde entonces ha sido aplicado en diversas disciplinas como la medicina, la inteligencia artificial y la economía.

Ejemplos donde se usa:

- Diagnóstico médico
- Filtros de spam (caso actual)
- Sistemas de recomendación
- Predicción de eventos
- Meteorología
- Reconocimiento de voz

### Palabras clave:

- Probabilidad condicional: se refiere a la probabilidad de que un evento ocurra dado que otro evento ya ha ocurrido. Por ejemplo, la probabilidad de que llueva dado que hay nubes en el cielo.
- Probabilidad mutua: establece que la probabilidad de que dos eventos ocurran juntos es igual a la probabilidad de que ocurra el primer evento multiplicada por la probabilidad de que ocurra el segundo evento dado que el primer evento ya ha ocurrido.

## Funcionalidad

El teorema de Bayes establece que la probabilidad de un evento A dado un evento B es igual a la probabilidad del evento B dado A multiplicado por la probabilidad de A dividido por la probabilidad de B. Es decir:

```bash
                            P(A|B) = P(B|A) * P(A) / P(B)
Donde:

    P(A|B) es la probabilidad de A dado B.

    P(B|A) es la probabilidad de B dado A.

    P(A) es la probabilidad de A.

    P(B) es la probabilidad de B.


```

## En nuestro caso:

- Calculamos la proporcion de correos spam: la cantidad de correos que son spam segun el dataset y se divide entre el total de correos

- Calculamos la proporcion de correos : 1 - Probabilidad spam

- Calcular la probabilidad de que un correo sea spam:

Como estamos utilizando un dataset con el mensaje y el su clasificacion, debemos de calcular en este caso lo siguiente:

```bash
                            P(spam|mensaje) = P(mensaje|spam) * P(spam) / P(mensaje)
Donde:

    P(spam) es la proporción de correos spam en el dataset.

    P(mensaje) es la probabilidad total de que un mensaje ocurra spam o no spam.

    P(mensaje|spam) es la probabilidad de que el mensaje sea spam.

    Lo que queremos calcular:
    P(spam|mensaje)


```

## Autores

- [@Peña Lopez Miguel Angel](https://github.com/KingSplatt)

- [@Robles Rios Jacquelin](https://github.com/jacq1813)

## Documentation

Blanca, A. C. (2024, 14 noviembre). Explicación del Teorema de Bayes: fórmula y ejemplos. Academia Carta Blanca. https://academiacartablanca.es/blog/teorema-de-bayes-probabilidad/
