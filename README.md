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
✦ Carga y Procesamiento de Datos: Mediante un notebook de ETL (extraccion, transformacion y carga de datos) se observaron los datos, se desanidaron las columnas pertinentes y se hizo la respectiva limpieza de datos obteniendo dos nuevos datasets listos para realizar un analisis exploratorio

✦ Primera Optimización del Dataset: Se decidió tomar para el analisis exploratorio de datos unicamente las peliculas en idioma español o ingles.

✦ Analisis exploratorio de datos : Mediante un notebook llamado EDA se pudieron observar de forma grafica (histogramas, matrices de correlacion, barras de distribucion, nubes de palabras, Tendencias en el tiempo) las diferentes caracteristicas tanto numericas como categoricas a tener en cuenta, ademas se solcionaron problemas con datos faltantes, outliers pertinentes

✦ Segunda Optimizacion: dentro del notebook del analisis exploratorio se decidio guardar un dataset mas pequeño donde se unieron los datasets originales, se filtro la fecha de lanzamiento de las peliculas mayor a 1980 basandonos en las tendencias temporales graficadas, y donde el status de la pelicula sea 'released' ya que estamos recomendando peliculas para ver basadas en una pelicula dada, en este dataset se dejaron unicamente las columnas necesarias para la creacion del modelo 

✦ Creación del Modelo de Recomendación: Se construyó un modelo de recomendación basado en la similitud del coseno, utilizando características tanto numéricas como categóricas, incluyendo presupuesto, ganancias, cantidad de votos, popularidad, actores, directores, genero de la pelicula y descripcion de la película que fueron vectorizadas convirtiendose en matrices dispersas concatenadas.

✦ Despliegue de la API: Se utilizó FastAPI para crear y desplegar la API en Render, permitiendo consultas de recomendaciones y detalles sobre películas, actores, y directores; El modelo de similitud del coseno realizado en la api cuenta con dos funciones una donde se procesan los datos (vectorizaciones, escalado, ponderacion, entre otros procesos) para la optimizacion de la memoria dado que render tiene un limite reducido.
    
## Datos y Fuentes
Los datos necesarios para el despliegue del proyecto se pueden encontrar en la carpeta Datasets a continuacion observaremos las columnas y los tipos de datos que contienen.
✦ dataset optimizado de movies

![image](https://github.com/user-attachments/assets/7b05f327-195c-4e97-b3fe-eaeb5946c594)

✦dataset optimizado de credits

![image](https://github.com/user-attachments/assets/bfce4ac0-3b6b-471d-9f28-f908c99e7655)

✦dataset final unido

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

  
  



