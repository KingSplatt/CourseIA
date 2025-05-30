## Reconocimiento de Emociones Faciales con Deep Learning

Este proyecto implementa un sistema de reconocimiento de emociones faciales utilizando redes neuronales convolucionales (CNN) en Python, con TensorFlow/Keras y OpenCV. El flujo abarca desde la recopilación y preprocesamiento de datos hasta la implementación de un sistema en tiempo real para la detección de emociones a través de la cámara web.

### Recopilación de datos
- **Fuente:** El dataset se obtuvo desde Roboflow, una plataforma que facilita la descarga de conjuntos de datos para visión computacional.
- **Descarga:** Se utilizó la API de Roboflow para descargar el dataset de clasificación de emociones faciales.
- **Estructura:** El dataset descargado contiene imágenes organizadas en carpetas por clase (emociones como angry, happy, sad, etc.) y separadas en conjuntos de entrenamiento, validación y test.

### Preprocesamiento de imagenes
- **Aumentos de datos:** Se aplicaron técnicas de data augmentation para mejorar la robustez del modelo **Brillo, Rotacion, Escalado**
- **Escalado:** Cambios aleatorios en el tamaño de la imagen.
- **Herramientas:** Se usaron **OpenCV y Numpy** para manipular las imágenes y guardar las aumentadas en una carpeta preprocesado.
- **ImageDataGenerator:** Además, se utilizó ImageDataGenerator de Keras para aplicar normalizacion de las imagenes en el entrenamiento, lo que ayuda a la generalización del modelo.



### Organizacion del Dataset
Organización del Dataset
El dataset final se organizó en tres carpetas principales:
- train/: Imágenes para entrenamiento.
- valid/: Imágenes para validación.
- test/: Imágenes para prueba.
Dentro de cada carpeta, las imágenes están clasificadas en subcarpetas por emoción.
### Construccion y Entrenamiento del Modelo
- **Arquitectura:** Se diseñó una **red neuronal convolucional** profunda con varios bloques de capas Conv2D, MaxPooling2D, BatchNormalization y Dropout para evitar el sobreajuste.
- **Entrenamiento:** El modelo se entrenó usando los datos preprocesados, con callbacks como EarlyStopping, ReduceLROnPlateau y ModelCheckpoint para optimizar el proceso.
- **Evaluación:** Se evaluó el modelo en el conjunto de test y se generaron métricas como accuracy, loss y matriz de confusión.

### Implementacion en Tiempo Real

- **Carga del modelo:** Se utilizó keras.models.load_model para cargar el modelo entrenado.
- **Procesamiento de video:** Con OpenCV (cv2), se accedió a la cámara web y se detectaron rostros en tiempo real usando un clasificador Haar Cascade.
- **Preprocesamiento de rostros:** Los rostros detectados se recortan, redimensionan y normalizan antes de ser pasados al modelo para la predicción.
- **Suavizado de predicciones:** Se implementó un historial de predicciones para suavizar la salida y evitar fluctuaciones.
- **Visualización:** El resultado de la emoción detectada se muestra en pantalla junto con el porcentaje de confianza.
### Librerias Utilizadas
- **tensorflow y keras** para la construcción y entrenamiento del modelo.
- **opencv-python (cv2)** para procesamiento de imágenes y video.
- **numpy** para operaciones numéricas.
- **matplotlib y seaborn** para visualización de resultados.
- **scikit-learn** para métricas y matriz de confusión.
- **roboflow** para la descarga del dataset.
## Autores

- [@Peña Lopez Miguel Angel](https://github.com/KingSplatt)

- [@Robles Rios Jacquelin](https://github.com/jacq1813)
## Video de la implementacion
- [Pruebas al "Sistema de reconocimiento facial de emociones"](https://youtu.be/8kCoOt-08Is)



