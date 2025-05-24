# Preprocesamiento y Aumento de Imágenes para Visión por Computadora

El preprocesamiento de imágenes es una etapa fundamental en proyectos de visión por computadora. Consiste en aplicar técnicas que mejoran o modifican las imágenes antes de ser utilizadas por un modelo de aprendizaje automático o red neuronal. Esto ayuda a reducir ruido y normalizar condiciones de captura.

El **aumento de datos (data augmentation)** es una técnica que consiste en generar nuevas versiones de las imágenes de entrenamiento mediante transformaciones como rotaciones, cambios de brillo y escalado. Esto permite:

- Aumentar el tamaño efectivo del dataset.
- Introducir variabilidad que mejora la capacidad del modelo para generalizar.
- Prevenir el sobreajuste (overfitting), especialmente con datasets pequeños.

## 🔧 Transformaciones Aplicadas

Cada imagen es aumentada con una combinación aleatoria de las siguientes transformaciones:

- **Brillo** (`brightness`): Ajusta la intensidad de luz para simular diferentes condiciones de iluminación.
- **Rotación** (`rotation`): Simula distintas orientaciones de los rostros en la imagen.
- **Escalado** (`scale`): Cambia el tamaño para mejorar la capacidad del modelo de reconocer objetos en diferentes proporciones.

Las imágenes originales también se guardan para comparación.

## Autores

- [@Peña Lopez Miguel Angel](https://github.com/KingSplatt)

- [@Robles Rios Jacquelin](https://github.com/jacq1813)

## Documentation

El dataset fue recopilado desde:

https://universe.roboflow.com/my-workspace-2-9rl26/facial-emotion-detection-rijqy/dataset/2
