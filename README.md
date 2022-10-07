# Detector de Anomalias en Motores Industriales
Los motores eléctricos industriales son la base para que las máquinas industriales efectúen sus operaciones, por lo que, es necesario darle el respectivo mantenimiento y cuidado posible a tiempo. Por ello, la detección temprana de fallas o comportamientos atípicos en motores permite un ahorro económico sustancial, ya sea, por paradas en líneas de producción, pérdidas de rendimiento y seguridad. Este proyecto se desarrolló con un modelo de TinyML, usando Edge Impulse para el entrenamiento del modelo, junto a un kit de Arduino con sensor de sonido para la recolección de datos de un motor eléctrico. Mediante este proceso se obtuvo un dataset de sonidos con fallas, sin fallas y sonidos atípicos fondo. Posteriormente, se generaron espectrogramas para su análisis. Este estudio permitió diseñar un modelo fiable, económico y eficiente de detección temprana de fallas en motores eléctricos industriales con el uso de TinyML. Lo que permitió reducir las tasas de fallas y los tiempos de inactividad no programados.

Mediante el análisis de los espectrogramas se pueden obtener datos como la frecuencia, periodo, picos y dominio, gracias a ello se puede llegar a una conclusión sobre el estado del motor ya sea la proporción de tiempo de inactividad, variación de rotación, desequilibrio, problemas de soporte o problemas con el cojinete entre otros.

### Procedimiento
- Configurar el TinyMl kit de arduino y el software requerido.
- Recoleccion de datos.
- Limpieza de datos.
- Modelado en Edge Impulse
- Pruebas
- Creación de gráficos

Para la implementación de gráficos se usó el lenguaje de programación Python usando un archivo IPYNB que es un documento de cuaderno utilizado por Jupyter Notebook, que incluye las entradas y salidas de imágenes o audios, además se usaron las librerías mostradas en la Tabla 1. Librerías usadas para la elaboración de las gráficas con su respecta funcionalidad.

|                Librerías usadas             |                     |
| :----------------------------------------:  | :------------------ | 
| Librería                                    | Uso                 |
| Numpy                                       |	Manejo de Arreglo   |
| Matplotlib                                  | realizar gráficos   |
| wavfile                                     | leer y grabar audios|
| fft                                         | calcular la transformada de Fourier|
| Plotly                                      | realizar gráficos interactivo|

_Tabla1. Librerías usadas para la elaboración de las gráficas_

Dicho esto, el proceso comienza con la importación de datos ubicados en el dataset del EdgeImpulse recopilando todos los datos (75 audios) en un formato wav (Waveform Audio Format) con 1 segundo de duración cada uno, con esto se generan 2 carpetas “testing” y “training” ambos contienen archivos wav, Edge Impulse recomienda usar las de testing dado que estas son generalmente usadas para medir la precisión del modelo luego del entrenamiento.

Ahora se importan los datos al proyecto de Jupyter Notebook usando la librería de wavfile, con esto se crean vectores (fallas_signals, sinfallas_signals, atípicos_signals) para los audios de motor con fallas, sin fallas y los atípicos, el filtro se logró debido a que el nombre de todos los audios comenzaba con su categoría correspondiente como se ve en la _Figura 1_. facilitando así su categorización.

![image](https://user-images.githubusercontent.com/74307558/194596695-234a2fba-94b9-4b74-8e2a-31b27b4b5d0a.png)
_Figura1. Nombre de Audios_

Para la ilustración de las gráficas se utiliza la librería Matplotlib y la de Plotly. Se empezó con la creación de los espectrogramas cada uno con su vector correspondiente generando 3 gráficas distintas _Figura 2._ Sin embargo, para apreciar mejor los resultados se decidió crear otra función en la cual se ilustren los 3 resultados en una misma gráfica _Figura3_.

![image](https://user-images.githubusercontent.com/74307558/194596762-b47d0c32-b7fa-4a98-a48b-9ca5c13c09ff.png)
_Figura2. Proceso realizado para generar espectrogramas con su vector correspondiente_

![image](https://user-images.githubusercontent.com/74307558/194596830-873204f1-37c7-4ee4-96fa-3b3ee7d60a60.png)
_Figura3. Proceso para realizar espectrograma con los 3 vectores juntos_

Al notar las frecuencias ilustradas con las funciones anteriores y no notar cambios significativos se optó por crear otra función llamada dominioTiempo(), la cual representa la señal(audio) en función de Tiempo(ms) vs. Amplitud(V) ilustrando de esta forma la señal de su vector correspondiente de manera más precisa, en la _Figura 4._ se ilustra su proceso.

![image](https://user-images.githubusercontent.com/74307558/194596887-7b881726-82c5-4724-aa4f-8d91c1de7e91.png)
_Figura4. Proceso de creación del gráfico de la señal en dominio del Tiempo(ms)_

Y por último se crearon gráficas FFT(Transformada Rápida de Fourier) usando la librería de fft, creando gráficas con otros detalles en función de Amplitud vs Frecuencia con sus vectores correspondientes _Figura 5._

![image](https://user-images.githubusercontent.com/74307558/194597002-b77d531c-0542-487d-b7e3-392815fdba20.png)
_Figura5. Proceso de creación de gráfico FFT_


### Recomendaciones
- Descargar el proyecto, debido a que se usaron muchos gráficos además de gráficos iteractivos provocando que GitHub presente problemas en ilustrarlos.
- Se sugiere aumentar el número de muestras del dataset con diversos ruidos de motores y ruidos de fondo, para tener una mayor validez al ser entrenados.
