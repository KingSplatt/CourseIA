# Sistema Experto - Diagnostico Médico

Los sistemas expertos (SE) son programas informáticos que tienen el objetivo de solucionar un problema concreto y utilizan la Inteligencia Artificial (IA) para simular el razonamiento de un ser humano. Se denominan sistemas expertos porque estos programas imitan la toma de decisiones de un profesionista en la materia.

### Tipos de sistemas expertos

- RBO (Basado en reglas de sistemas experos)
- CBR (Basado en reglas de razonamiento)
- Basado en reglas de Bayes

### Partes de un sistema expertos
- Base de conocimiento : La base de conocimientos son las reglas en la cual el sistema se fundamenta. Cada instrucción tiene de forma aislada su propio concepto. Generalmente, estos conocimientos son de carácter declarativo, lo que indica que la base de conocimientos es una definición de sus propias características, y para la resolución de problemas, es necesario la intervención de un nuevo mecanismo.

- Motor de inferencias: El motor de inferencias es el responsable de seguir determinadas reglas (seleccionar las que considere oportunas) y ejecutarlas, con el objetivo de resolver un problema.

- Base de Hechos: La base de hechos es la que almacena la información de las distintas fases de un sistema experto: datos de partida, criterios de parada, y la actualización de información conforme se ejecuta el sistema. La base de hechos es también denominada base de datos global o memoria de trabajo.

### ¿Donde se usan los sistemas expertos?
Una de las principales funciones de estos sistemas es la relacionada con la salud. Sus aplicaciones en medicina son muy variadas y desde hace décadas se utilizan como sistemas de diagnóstico de enfermedades.

Sus usos varían enormemente en función del campo para el que estén diseñados y, por ejemplo, en la industria y los negocios empresariales pueden realizar tareas de análisis de préstamos, optimización de almacenes logísticos, toma de decisiones financieras, gestión de datos, evaluación, control de procesos, etc.

### Descripción del problema y objetivo

Se busca resolver la dificultad de obtener un diagnóstico médico rápido y accesible, especialmente para aquellos usuarios con recursos médicos limitados. Es por esto que se requiere un sistema experto que permita recibir un diagnóstico de enfermedades basado en los síntomas que reporta el usuario. Para ello se debe realizar una serie de preguntas sobre los síntomas posibles y a partir de ellos sugerir las enfermedades posibles, además de orientación sobre su condición, posibles causas y tratamientos.

### Como se llevo a cabo
Para recopilar informacion necesirtamos de una base de conocimiento, consultar aquella informacion necesaria para llevar la informacion de un experto, para ello consultamos un libro ('Manual Merck de Signos y sintomas del paciente - Diagnostico y tratamiento'),
dentro de estos decidimos obtener todas aquellos signos y sintomas acerca de causas de enfermedades para la medicina. Toda la informacion recabada la fuimos adjuntando a un JSON donde podriamos clasificarla e identificarla de manera sencilla

Un motor de inferencias, Para nuestro caso decidimos usar el lenguaje de programacion funcional PROLOG con SWISH, ahi mismo estableceremos las reglas y hechos que capturamos de nuestro base de conocimiento.



## Autores

- [@Peña Lopez Miguel Angel](https://github.com/KingSplatt)

- [@Robles Rios Jacquelin](https://github.com/jacq1813)
## Documentation

De Redacción de la Universidad Internacional de la Rioja, E. (2024, 9 agosto). ¿Qué es un sistema experto? Usos y aplicaciones en Inteligencia Artificial. UNIR México. https://mexico.unir.net/noticias/ingenieria/sistema-experto/

Porter, R. S., Kaplan, J. L., & Homeier, B. P. (Eds.). (2010). Manual Merck de signos y síntomas del paciente: Diagnóstico y tratamiento (1.ª ed., traducción de la Editorial Médica Panamericana S.A.). Editorial Médica Panamericana. (Obra original publicada en inglés en 2008 como The Merck Manual of Patient Symptoms). ISBN: 978-607-7743-09-5



