<h1 align="center"><strong>Proyecto Individual #1 - Sistema de Recomendación de Películas</strong></h1>

## Descripción

Este proyecto implementa un sistema de recomendación de películas utilizando machine learning, desarrollado como parte de mi formación en SoyHenry. El sistema permite realizar consultas sobre detalles de películas, directores, y actores, así como obtener recomendaciones basadas en criterios como el género, popularidad, actores, directores, y sinopsis.

He desarrollado una API que interactúa con los datasets cargados, permitiendo a los usuarios obtener información detallada y recomendaciones personalizadas. El modelo de recomendación emplea técnicas de filtrado basadas en el contenido, combinando variables numéricas y categóricas mediante `TfidfVectorizer` para vectorizar el texto y `StandardScaler` para escalar las variables numéricas.

Este proyecto me permitió poner en práctica conocimientos teóricos adquiridos en el curso y profundizar en nuevas herramientas como FastAPI y Render para la implementación y despliegue de la API, además de trabajar con librerías como `scikit-learn`, `FastAPI`, `Uvicorn`, y `PowerBI` para la visualización de datos.

## Tabla de Contenidos
✦  [Instalación y Requisitos](#instalación-y-requisitos)  
✦  [Estructura del Proyecto](#estructura-del-proyecto)  
✦  [Metodología del Proyecto](#metodología-del-proyecto)  
✦  [Datos y Fuentes](#datos-y-fuentes)  
✦  [Despliegue de la API](#despliegue-de-la-api)  
✦  [Análisis Teórico del Modelo](#análisis-teórico-del-modelo)  
✦  [Resultados](#resultados)  
✦  [Autor](#autor)  
✦  [Links](#links)  

---

## Instalación y Requisitos

### Pasos para instalar el proyecto:

1. Clonar el repositorio:

     ![image](https://github.com/user-attachments/assets/48635476-a253-484a-8710-8ad9657f863f)

  3. Crear un entorno virtual: python -m venv entorno_virtual

     ![image](https://github.com/user-attachments/assets/b3223ca8-8dba-49a9-970d-775d2a9da147)

  5. Activar el entorno virtual:
     * Windows: entorno_virtual\Scripts\activate 
     * macOS/Linux: source venv/bin/activate
  6. Instalar las dependencias: pip install -r requirements.txt

     ![image](https://github.com/user-attachments/assets/5846bbe4-1f82-42a6-b6f3-9b02cbd2bc82)


## Estructura del Proyecto
✦ Datasets: Carpeta que contiene los archivos utilizados para el proyecto en formato Parquet.

✦ Notebooks: Incluye los Jupyter notebooks donde se realizaron las transformaciones, análisis y modelado.

✦ Extras Visuales: Carpeta con un archivo Power BI que ofrece una mejor visualización tabular de los datos.

✦ api.py: Archivo donde se define la API con los endpoints.

✦ README.md: Documentación del proyecto.

✦ .gitignore: Para evitar subir archivos innecesarios al repositorio.
  
## Metodología del Proyecto
### Herramientas Utilizadas:
✦ Visual Studio Code: Editor de código para desarrollar y modificar el proyecto en un entorno virtual local.

✦ GitHub: Plataforma para almacenar el proyecto de forma global.

✦ Render: Servicio de despliegue en la nube para la API.

✦ Git Bash: Utilizado para crear el entorno virtual, configurar el repositorio y subir cambios locales a GitHub.

✦ PowerBI: Herramienta utilizada para visualizar datos de manera más accesible y detallada.

### Proceso de Desarrollo:
✦ Carga y Procesamiento de Datos: Se implementó un proceso de ETL (Extracción, Transformación y Carga) mediante un notebook. En esta fase, se examinaron los datos en profundidad, desanidando las columnas relevantes y aplicando una limpieza exhaustiva. Esto permitió obtener dos datasets optimizados, que fueron la base para el análisis exploratorio de datos.

✦ Primera Optimización del Dataset: Para realizar el análisis exploratorio de datos de manera más eficiente, se decidió filtrar las películas únicamente en los idiomas español e inglés, ya que estas representaban los mercados de mayor interés para el proyecto.

✦ Analisis exploratorio de datos (EDA) : Utilizando un notebook denominado "EDA", se analizaron gráficamente las características numéricas y categóricas del dataset. Esto incluyó histogramas, matrices de correlación, gráficos de barras, nubes de palabras y análisis de tendencias temporales. Durante este proceso, se resolvieron problemas de datos faltantes y outliers para garantizar la integridad del análisis.

✦ Segunda Optimizacion: Tras el análisis exploratorio, se creó un nuevo dataset más reducido. Este dataset unió los archivos originales y aplicó filtros clave, como limitar las películas a las que fueron lanzadas a partir de 1980 y cuya fecha de estreno indicaba un estatus de "released" (estrenada), ya que el sistema de recomendación está orientado a sugerir películas disponibles para ver. Además, solo se conservaron las columnas necesarias para la construcción del modelo de recomendación.

✦ Creación del Modelo de Recomendación: El modelo se construyó utilizando un enfoque de filtrado basado en contenido, empleando la similitud del coseno para medir la relación entre películas. Las características incluyeron tanto variables numéricas (presupuesto, ingresos, votos, popularidad) como categóricas (actores, directores, género y descripción de la película). Las variables categóricas se vectorizaron utilizando TfidfVectorizer, mientras que las numéricas se escalaron con StandardScaler. Finalmente, se combinaron las matrices resultantes para construir el modelo.

✦ Despliegue de la API: Para desplegar el sistema, se utilizó FastAPI, lo que permitió crear una API alojada en Render. Esta API permite consultas como recomendaciones basadas en contenido, además de detalles sobre películas, actores y directores. Debido a las limitaciones de memoria en Render, el sistema cuenta con una función de procesamiento de datos optimizada que realiza las vectorizaciones, escalado y ponderación en una fase previa, mejorando el rendimiento en tiempo real.

## Datos y Fuentes
Los datos utilizados para este proyecto se encuentran en la carpeta "Datasets". A continuación, se presentan los principales datasets optimizados utilizados para el análisis y el desarrollo del modelo de recomendación:
✦ Dataset optimizado de películas (movies):

Este dataset contiene información esencial sobre las películas, como el presupuesto, los ingresos, la popularidad, el género y las fechas de lanzamiento, entre otros.

![image](https://github.com/user-attachments/assets/7b05f327-195c-4e97-b3fe-eaeb5946c594)

✦ Dataset optimizado de créditos (credits):

En este dataset se almacena información clave sobre los actores, directores y demás miembros del equipo de producción de las películas.

![image](https://github.com/user-attachments/assets/bfce4ac0-3b6b-471d-9f28-f908c99e7655)

✦ Dataset final unido:

Este dataset combina los dos archivos anteriores (películas y créditos) para facilitar el análisis y la construcción del modelo. Contiene las columnas relevantes para la recomendación de películas.

![image](https://github.com/user-attachments/assets/6cdbb28b-c335-4aa4-8786-ff347fa3bfdb)

## Despliegue de la API
La API fue desplegada en Render y cuenta con los siguientes endpoints:

✦ GET /: Endpoint raíz que muestra un mensaje de bienvenida.

✦ GET /cantidad_peliculas_mes/{mes}: Devuelve la cantidad de películas estrenadas en un mes específico.

✦ GET /cantidad_peliculas_dia/{dia}: Devuelve la cantidad de películas estrenadas en un día específico de la semana.

✦ GET /cantidad_peliculas_fecha/{dia}/{mes}/{anio}: Devuelve la cantidad de películas estrenadas en una fecha específica.

✦ GET /puntaje_pelicula/{nombre}: Devuelve la popularidad de una película específica.

✦ GET /votos_pelicula/{nombre}: Devuelve la cantidad de votos de una película específica.

✦ GET /obtener_exito_actor/{nombre_actor}: Devuelve el éxito de un actor basado en la cantidad de películas, ganancias y retorno generado.

✦ GET /obtener_exito_director/{nombre_director}: Devuelve el éxito de un director en base a las películas dirigidas, presupuesto, ganancias y retorno generado.

✦ GET /recomendacion/{title}: Devuelve una lista de películas recomendadas basadas en la similitud de características como popularidad, género, actores, directores, y descripción.

## Análisis Teórico del Modelo

A lo largo del proyecto, se analizaron y procesaron diversas características de las películas para mejorar la calidad de las recomendaciones:

✦ Popularidad: Se observó que las películas con mayor popularidad tienden a recibir más recomendaciones debido a la relevancia de esta característica en el modelo. 

✦ Presupuesto y Ganancias: Aunque estas características son importantes, se identificó que no siempre correlacionan directamente con la calidad o éxito percibido de una película, por lo que se ajustaron sus pesos en el modelo. 

✦ Género: Uno de los factores más influyentes en el sistema de recomendación. Las películas que comparten géneros similares suelen ser altamente recomendadas entre sí. 

✦ Actores y Directores: Los actores y directores tienen un fuerte impacto en las recomendaciones, especialmente cuando son nombres conocidos o han trabajado en películas similares. 

✦ Descripción (sinopsis): Aunque no fue la característica más influyente, la similitud en la sinopsis contribuyó a mejorar la precisión en algunas recomendaciones.

Con estas observaciones, se realizaron ajustes en el modelo para lograr un equilibrio entre las diferentes características y optimizar la precisión de las recomendaciones finales.

## Resultados

El modelo de recomendación ha demostrado ser eficaz al generar recomendaciones de películas basadas en diversas características relevantes. Los resultados muestran que el enfoque basado en la similitud del coseno permite recomendaciones personalizadas y coherentes. La API desplegada ofrece una forma sencilla de interactuar con el modelo, permitiendo consultas rápidas y efectivas.

## Autor

✦ Este proyecto fue realizado por **Karen Lizeth Barbosa Rojas**.

## Links

✦ [Proyecto en Render](https://proyecto-recomendacion-de-peliculas-ml.onrender.com) → Enlace al endpoint principal de la API. Para ver todas las consultas disponibles, puedes ingresar a la ruta `/Docs` o consultar las rutas descritas en el archivo `api.txt`, ubicado en la carpeta "Extras visuales".  
> **Nota:** El tiempo de reactivación de la API en Render puede demorar hasta **10 minutos** debido a que entra en modo reposo cuando no está en uso. Por favor, ten paciencia mientras la aplicación se reactiva.

✦ [Video Explicativo](#) → Enlace al video explicativo y demostrativo del proyecto desplegado.
  



