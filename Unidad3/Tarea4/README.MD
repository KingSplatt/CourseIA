# Sistema Experto para Diagnostico de Enfermedades 

Este proyecto consiste en un sistema experto diseñado para asistir en el diagnóstico preliminar de enfermedades comunes. El sistema interactúa con el usuario a través de preguntas sobre síntomas y, mediante una máquina de inferencia basada en reglas, determina el diagnóstico más probable según las respuestas proporcionadas.

### Tecnologias usadas

- lenguaje: Prolog
- Motor de inferencia: SWI-Prolog (SWISH)
- Base de conocimientos: Reglas y hechos extraidos del Manual Merck
- Archivo fuente: diagnosticoMedj.pl

### Estructura del sistema
El sistema se compone de tres elementos fundamentales, como lo suelen hacer los sistemas expertos:
- Base de conocimiento : La base de conocimientos son las reglas en la cual el sistema se fundamenta. Cada instrucción tiene de forma aislada su propio concepto. Generalmente, estos conocimientos son de carácter declarativo, lo que indica que la base de conocimientos es una definición de sus propias características, y para la resolución de problemas, es necesario la intervención de un nuevo mecanismo. En este caso son las enfermedades, que se definen como hipotesis, y cada una depende de una combinacion de sintomas (hechos)


- Motor de inferencias: El motor de inferencias es el responsable de seguir determinadas reglas (seleccionar las que considere oportunas) y ejecutarlas, con el objetivo de resolver un problema. El programa ejecuta el predicado evaluar/0, que inicia la consulta al usuario, analiza los síntomas afirmados y determina las enfermedades compatibles.

- Base de Hechos: La base de hechos es la que almacena la información de las distintas fases de un sistema experto: datos de partida, criterios de parada, y la actualización de información conforme se ejecuta el sistema. La base de hechos es también denominada base de datos global o memoria de trabajo.

### Enfermedades Incluidas
- Gripe
- Gastritis
- Faringitis
- Migraña
- Dermatitis
- Resfriado
- Cistitis
- Lumbalgia
- Conjuntivitis

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



