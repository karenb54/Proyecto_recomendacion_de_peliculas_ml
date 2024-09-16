Proyecto Individual #1 Machine Learning

Descripcion:
  Este proyecto tiene como objetivo presentar un acercamiento al machine learning aprendido a travez de SoyHenry, para esto se realizo un sistema de recomendacion de peliculas.
  He desarrollado una api que permite hacer consultas sobre los datasets cargados, donde se podra obtener detalles acerca de las pelculas, directores, actores ademas de obtener
  una recomendacion de peliculas basada en diversos criterios como el genero, la popularidad, los actores, el resumen de la pelicula, entre otros.
  El modelo utiliza filtrado que esta basado en el contenido tanto numerico como categorico usando TfidfVectorizer para vectorizar el texto y StandardScaler para escalar las 
  variables numericas
  El proyecto cuenta con diferentes consultas que pueden ser realizadas por el usuario de manera simple
  Este proyecto me ha permitido llevar los conocimientos teoricos adquiridos a travez del curso y usarlos en un ambiente de desarrollo real, ademas de encontrar aprender sobre
  nuevas librerias como FastApi, Uvicorn, scikit-learn, entre otras y nuevas herramientas como render donde se podra visualizar mi proyecto de una mejor manera

Tabla de contenido

1. Instalacion y requisitos
2. Estructura del proyecto
3. Metodologia del proyecto
4. Datos y fuentes
5. Deployment de la api
6. Resultados

Instalacion

* Pasos

  1. Clonar el repositorio: git clone https://github.com/karenb54/Proyecto_recomendacion_de_peliculas_ml.git
  2. Crear un entorno virtual: python -m venv entorno_virtual
  3. Activar el entorno virtual:
     * Windows: entorno_virtual\Scripts\activate 
     * macOS/Linux: source venv/bin/activate
  6. Instalar las dependencias: pip install -r requirements.txt

2. Estructura del proyecto
* Datasets: Una carpeta que contiene todos los archivos que se usaron para realizar el proyecto
* Notebooks: Una carpeta que incluye los notebooks de Jupyter con las transformaciones, los analisis y el modelos.
* Extras visuales: Una carpeta que incluye un archivo en power bi donde estan cargados los archivos que se usaron para una mejor visualizacion tabular de los datos.
* .gitignore: Un archivo donde se encuentras las cosas que se crearon de manera local que no son necesarias subir.
* api.py: La api donde estan las consultas paso a paso, este archivo se encuentra deployado en render
* README.md: Archivo de documentación del proyecto.

3. Metodologia

Para realizar este proyecto utilice las siguientes Herramientas

Visual Studio Code : Se uso este editor de codigo para observar y modificar el proyecto que cree un entorno virtual de manera local.
Github: Se uso para almacenar el proyecto de manera global
Render : Se uso para deployar la api alojada en el Github
Gitbash: Se uso para crear el entorno virtual, para crear el repositorio, y para subir los cambios realizados de manera local al global.
PowerBi: Se uso para visualizar los datos de manera tabular dando un acceso mas profundo


4. Datos
Los datos utilizados en este proyecto provienen de un proyecto de Soy Henry, incialmente eran 2 archivos que contenian informacion total sobre las peliculas
(popularidad, prespuesto, ganancias, fecha de lanzamiento, desripcion, entre otros datos) y sobre las personas que trabajaron dentro de dichas peliculas
(nombres de actores, Directores, personaje interpretado, rol, entre otros datos) en formato CSV para la optimizacion y el manejo de los datos se decidio
pasarlos a parquet siendo un formato menos pesado, ademas despues del analisis exploratorio se decidio unir los los datasets por medio del id para una
mayor comodidad ya que se eliminaron distintas columnas que no eran utiles al momento del analisis o de la creacion del modelo.

5. Deployement de la api

Por medio de render se deployo la api creada para este proyecto los endpoints creados fueron:
  * @aplicacion.get("/") : siendo el endpoint raiz dando la bienvenida a la api
  * @aplicacion.get("/cantidad_peliculas_mes/{mes}") : Creando una consulta de la cantidad de peliculas que se estrenaron en determinado mes
  * @aplicacion.get("/cantidad_peliculas_dia/{dia}") : Creando una consulta de la cantidad de peliculas que se estrenaron en determinado dia de la semana
  * @aplicacion.get("/cantidad_peliculas_fecha/{dia}/{mes}/{anio}") : Creando una consulta de la cantidad de peliculas que se estrenaron en una fecha especifica
  * @aplicacion.get("/puntaje_pelicula/{nombre}") : Creando una consulta de la popularidad de una pelicula especifica
  * @aplicacion.get("/votos_pelicula/{nombre}") : Creando una consulta de la cantidad de votos de una pelicula especifica
  * @aplicacion.get("/obtener_exito_actor/{nombre_actor}") : Creando una consulta donde expondremos el exito de un actor basado en la cantidad de peliculas que realizo,
    las ganacias de las peliculas y el retorno generado de dichas peliculas.
  * @aplicacion.get("/obtener_exito_director/{nombre_director}") :Creando una consulta donde expondremos el exito de un Director basado en la cantidad de peliculas que Dirigio,
    El prespuesto de la pelicula,las ganacias de las peliculas y el retorno generado de dichas peliculas.
  * @aplicacion.get("/recomendacion/{title}") : Creando una consulta de recomendacion de peliculas basado en un modelo de similitud del coseno (peliculas mas similares
    a la consultada segun las siguientes caracteristicas: la popularidad, el genero, el presupuesto, las ganancias, la cantidad de votos, los actores y directores que participaron,
    y la descripcion de las peliculas)

    Proyecto Individual #1 - Sistema de Recomendación de Películas
Descripción
Este proyecto implementa un sistema de recomendación de películas utilizando machine learning, desarrollado como parte de mi formación en SoyHenry. El sistema permite realizar consultas sobre detalles de películas, directores, y actores, así como obtener recomendaciones basadas en criterios como el género, popularidad, actores, directores, y sinopsis.

He desarrollado una API que interactúa con los datasets cargados, permitiendo a los usuarios obtener información detallada y recomendaciones personalizadas. El modelo de recomendación emplea técnicas de filtrado basadas en el contenido, combinando variables numéricas y categóricas mediante TfidfVectorizer para vectorizar el texto y StandardScaler para escalar las variables numéricas.

Este proyecto me permitió poner en práctica conocimientos teóricos adquiridos en el curso y profundizar en nuevas herramientas como FastAPI y Render para la implementación y despliegue de la API, además de trabajar con librerías como scikit-learn, FastAPI, Uvicorn, y PowerBI para la visualización de datos.

Tabla de Contenidos
Instalación y Requisitos
Estructura del Proyecto
Metodología del Proyecto
Datos y Fuentes
Despliegue de la API
Resultados
Instalación y Requisitos
Pasos para instalar el proyecto:
Clonar el repositorio:

bash
Copy code
git clone https://github.com/karenb54/Proyecto_recomendacion_de_peliculas_ml.git
Crear un entorno virtual:

bash
Copy code
python -m venv entorno_virtual
Activar el entorno virtual:

Windows: entorno_virtual\Scripts\activate
macOS/Linux: source entorno_virtual/bin/activate
Instalar las dependencias necesarias:

bash
Copy code
pip install -r requirements.txt
Estructura del Proyecto
Datasets: Carpeta que contiene los archivos utilizados para el proyecto en formato Parquet.
Notebooks: Incluye los Jupyter notebooks donde se realizaron las transformaciones, análisis y modelado.
Extras Visuales: Carpeta con un archivo Power BI que ofrece una mejor visualización tabular de los datos.
api.py: Archivo donde se define la API con los endpoints.
README.md: Documentación del proyecto.
.gitignore: Para evitar subir archivos innecesarios al repositorio.
Metodología del Proyecto
Herramientas Utilizadas:
Visual Studio Code: Editor de código para desarrollar y modificar el proyecto en un entorno virtual local.
GitHub: Plataforma para almacenar el proyecto de forma global.
Render: Servicio de despliegue en la nube para la API.
Git Bash: Utilizado para crear el entorno virtual, configurar el repositorio y subir cambios locales a GitHub.
PowerBI: Herramienta utilizada para visualizar datos de manera más accesible y detallada.
Proceso de Desarrollo:
Carga y Procesamiento de Datos: Se comenzó con dos datasets en formato CSV que contienen información sobre películas y los actores y directores que participaron en ellas. Después de un análisis exploratorio de datos (EDA), se optó por unir los datasets mediante el ID de las películas.
Optimización del Dataset: Se decidió convertir los archivos a formato Parquet para mejorar el rendimiento.
Creación del Modelo de Recomendación: Se construyó un modelo de recomendación basado en la similitud del coseno, utilizando características tanto numéricas como categóricas, incluyendo presupuesto, popularidad, actores, y género de la película.
Despliegue de la API: Se utilizó FastAPI para crear y desplegar la API en Render, permitiendo consultas de recomendaciones y detalles sobre películas, actores, y directores.
Datos y Fuentes
Los datos provienen de un proyecto de SoyHenry. Se utilizaron dos archivos CSV que contenían información sobre películas y personas involucradas en ellas. Se unieron los datasets por el ID de las películas para facilitar el análisis y eliminar columnas no relevantes. Posteriormente, los archivos fueron convertidos a formato Parquet para mejorar el manejo y el rendimiento en el procesamiento de datos.

Despliegue de la API
La API fue desplegada en Render y cuenta con los siguientes endpoints:

GET /: Endpoint raíz que muestra un mensaje de bienvenida.
GET /cantidad_peliculas_mes/{mes}: Devuelve la cantidad de películas estrenadas en un mes específico.
GET /cantidad_peliculas_dia/{dia}: Devuelve la cantidad de películas estrenadas en un día específico de la semana.
GET /cantidad_peliculas_fecha/{dia}/{mes}/{anio}: Devuelve la cantidad de películas estrenadas en una fecha específica.
GET /puntaje_pelicula/{nombre}: Devuelve la popularidad de una película específica.
GET /votos_pelicula/{nombre}: Devuelve la cantidad de votos de una película específica.
GET /obtener_exito_actor/{nombre_actor}: Devuelve el éxito de un actor basado en la cantidad de películas, ganancias y retorno generado.
GET /obtener_exito_director/{nombre_director}: Devuelve el éxito de un director en base a las películas dirigidas, presupuesto, ganancias y retorno generado.
GET /recomendacion/{title}: Devuelve una lista de películas recomendadas basadas en la similitud de características como popularidad, género, actores, directores, y descripción.
Resultados
El modelo de recomendación ha demostrado ser eficaz al generar recomendaciones de películas basadas en diversas características relevantes. Los resultados muestran que el enfoque basado en la similitud del coseno permite recomendaciones personalizadas y coherentes. La API desplegada ofrece una forma sencilla de interactuar con el modelo, permitiendo consultas rápidas y efectivas.


  



