import numpy as np
import pandas as pd
from fastapi import FastAPI
from scipy.sparse import hstack, csr_matrix
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Crear una instancia para definir las rutas y funciones que se van a tomar como endpoints
aplicacion = FastAPI()

# Extraer los datos de los dataframe
credits_df_parquet = pd.read_parquet('Datasets/credits_dataset_parquet')
movies_df_parquet = pd.read_parquet('Datasets/movies_dataset_parquet')
dataframe_unido_modelo = pd.read_parquet('Datasets/dataset_unido_EDA')

# Crear un decorador para la ruta principal que va a definir el endpoint raíz
@aplicacion.get("/")
def inicio():
    return {"mensaje": "Esta es una API para realizar consultas sobre películas"}

# Consultas sobre la cantidad de películas en un mes dado
@aplicacion.get("/cantidad_peliculas_mes/{mes}")
def cantidad_peliculas_mes(mes: str):
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5,
        "junio": 6, "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10,
        "noviembre": 11, "diciembre": 12
    }
    numero_del_mes = meses.get(mes.lower())
    if numero_del_mes:
        cantidad = movies_df_parquet[movies_df_parquet['release_date'].dt.month == numero_del_mes].shape[0]
        return {"mensaje": f"En el mes de {mes}, se estrenaron {cantidad} películas."}
    else:
        return {"error": "El mes consultado no es válido. Por favor ingrese un mes válido en español."}

# Consultas sobre la cantidad de películas en un día dado
@aplicacion.get("/cantidad_peliculas_dia/{dia}")
def cantidad_peliculas_dia(dia: str):
    dias = {
        "lunes": 1, "martes": 2, "miércoles": 3, "jueves": 4,
        "viernes": 5, "sábado": 6, "domingo": 7
    }
    numero_de_dia = dias.get(dia.lower())
    if numero_de_dia is not None:
        cantidad_de_peliculas = movies_df_parquet[movies_df_parquet['release_date'].dt.weekday == numero_de_dia].shape[0]
        return {"mensaje": f"La cantidad de películas estrenadas en los días {dia} fueron {cantidad_de_peliculas}"}
    else:
        return {"error": "El día consultado no es válido. Por favor ingrese un día de la semana en español."}

# Consultas sobre la cantidad de películas en una fecha específica
@aplicacion.get("/cantidad_peliculas_fecha/{dia}/{mes}/{anio}")
def cantidad_filmaciones_fecha(dia: int, mes: int, anio: int):
    try:
        fecha_especifica = pd.Timestamp(year=anio, month=mes, day=dia)
        cantidad_de_peliculas = movies_df_parquet[movies_df_parquet['release_date'] == fecha_especifica].shape[0]
        return {"mensaje": f"{cantidad_de_peliculas} películas fueron estrenadas el {dia}/{mes}/{anio}"}
    except ValueError:
        return {"error": "La fecha consultada no es válida. Por favor ingrese una fecha válida en formato numérico dd/mm/YYYY."}

# Consultas sobre el puntaje de una película
@aplicacion.get("/puntaje_pelicula/{nombre}")
def puntaje_pelicula(nombre: str):
    pelicula = movies_df_parquet[movies_df_parquet['title'].str.lower() == nombre.lower()]
    if not pelicula.empty:
        nombre = pelicula['title'].values[0]
        anio = int(pelicula['release_year'].values[0])
        puntaje = pelicula['popularity'].values[0]
        return {"mensaje": f"La película {nombre} fue estrenada en el año {anio} con un puntaje de {puntaje}"}
    else:
        return {"error": "La película consultada no fue encontrada en la base de datos."}

# Consultas sobre la cantidad de votos de una película
@aplicacion.get("/votos_pelicula/{nombre}")
def votos_pelicula(nombre: str):
    pelicula = movies_df_parquet[movies_df_parquet['title'].str.lower() == nombre.lower()]
    if not pelicula.empty:
        nombre = pelicula['title'].values[0]
        anio = int(pelicula['release_year'].values[0])
        votos = int(pelicula['vote_count'].values[0])
        promedio_votos = pelicula['vote_average'].values[0]
        if votos >= 2000:
            return {"mensaje": f"La película {nombre} fue estrenada en el año {anio}. Tiene un total de {votos} votos, con un promedio de {promedio_votos}"}
        else:
            return {"mensaje": f"La película {nombre} no cumple con los 2000 votos requeridos. Tiene solo {votos} votos."}
    else:
        return {"error": "El nombre de la película consultada no fue encontrado."}

# Consultas sobre el éxito de un actor
@aplicacion.get("/obtener_exito_actor/{nombre_actor}")
def obtener_exito_actor(nombre_actor: str):
    nombre_actor_limpio = nombre_actor.lower().strip()
    peliculas_por_actor = credits_df_parquet[credits_df_parquet['cast_name_actor'].str.lower().str.strip() == nombre_actor_limpio]
    if not peliculas_por_actor.empty:
        peliculas_ids_columna = 'id_credits'
        peliculas_ids = peliculas_por_actor[[peliculas_ids_columna]].drop_duplicates()
        peliculas_actor_df = pd.merge(peliculas_ids, movies_df_parquet, left_on=peliculas_ids_columna, right_on='id_movies', how='inner')
        total_retorno = peliculas_actor_df['return'].sum()
        total_ganancia = peliculas_actor_df['revenue'].sum()
        num_peliculas = len(peliculas_actor_df)
        retorno_promedio = total_retorno / num_peliculas if num_peliculas > 0 else 0
        return {
            "mensaje": f"El actor {nombre_actor} ha participado en {num_peliculas} películas, con un retorno total de {total_retorno} y un retorno promedio de {retorno_promedio} por película con una ganancia total de ${total_ganancia}."
        }
    else:
        return {"error": f"El nombre {nombre_actor} no tiene películas registradas en la base de datos de actores."}

# Consultas sobre el éxito de un director
@aplicacion.get("/obtener_exito_director/{nombre_director}")
def obtener_exito_director(nombre_director: str):
    nombre_director_limpio = nombre_director.lower().strip()
    peliculas_por_director = credits_df_parquet[
        (credits_df_parquet['crew_name_member'].str.lower().str.strip() == nombre_director_limpio)
    ]
    if not peliculas_por_director.empty:
        peliculas_director = peliculas_por_director[peliculas_por_director['crew_job'] == 'Director']
        if not peliculas_director.empty:
            peliculas_ids_columna = 'id_credits'
            peliculas_ids = peliculas_director[[peliculas_ids_columna]].drop_duplicates()
            peliculas_director_df = pd.merge(peliculas_ids, movies_df_parquet, left_on=peliculas_ids_columna, right_on='id_movies', how='inner')
            total_retorno = peliculas_director_df['return'].sum()
            total_ganancia = peliculas_director_df['revenue'].sum()
            num_peliculas = len(peliculas_director_df)
            retorno_promedio = total_retorno / num_peliculas if num_peliculas > 0 else 0
            peliculas_detalles = peliculas_director_df[['title', 'release_date', 'return', 'budget', 'revenue']].to_dict(orient='records')
            return {
                "mensaje": f"El director {nombre_director} ha dirigido {num_peliculas} películas con un retorno total de {total_retorno} y un promedio de retorno de {retorno_promedio} por película con una ganancia total de ${total_ganancia}.",
                "Las peliculas dirigidas son": peliculas_detalles
            }
        else:
            return {"mensaje": f"El nombre {nombre_director} se encuentra en la base de datos, pero no tiene el rol de director en las películas registradas."}
    else:
        return {"error": f"El nombre {nombre_director} no se encuentra en la base de datos de directores."}

# Procesar datos y calcular la similitud del coseno
def procesar_datos():
    # Reemplazar los valores nulos
    dataframe_unido_modelo.fillna({'name_genre': '', 'cast_name_actor': '', 'crew_name_member': '', 'overview': ''}, inplace=True)

    # Normalizar características numéricas
    caracteristicas_numericas = ['budget', 'revenue', 'vote_count', 'popularity']
    scaler = StandardScaler()
    dataframe_unido_modelo[caracteristicas_numericas] = scaler.fit_transform(dataframe_unido_modelo[caracteristicas_numericas])

    # Vectorización de características categóricas
    vectorizador_generos = TfidfVectorizer()
    tfidf_generos = vectorizador_generos.fit_transform(dataframe_unido_modelo['name_genre'])

    vectorizador_cast = TfidfVectorizer()
    tfidf_cast = vectorizador_cast.fit_transform(dataframe_unido_modelo['cast_name_actor'])

    vectorizador_directores = TfidfVectorizer()
    tfidf_directores = vectorizador_directores.fit_transform(dataframe_unido_modelo['crew_name_member'])

    # Unir todas las matrices
    datos_vectorizados = hstack([
        csr_matrix(dataframe_unido_modelo[caracteristicas_numericas]),
        tfidf_generos,
        tfidf_cast,
        tfidf_directores
    ])

    # Reducir dimensionalidad
    svd = TruncatedSVD(n_components=100)
    datos_reducidos = svd.fit_transform(datos_vectorizados)

    # Calcular la similitud del coseno
    similitud = cosine_similarity(datos_reducidos)

    return similitud

# Consultar películas similares
@aplicacion.get("/recomendar_peliculas/{nombre_pelicula}")
def recomendar_peliculas(nombre_pelicula: str):
    similitud = procesar_datos()

    pelicula = dataframe_unido_modelo[dataframe_unido_modelo['title'].str.lower() == nombre_pelicula.lower()]
    if pelicula.empty:
        return {"error": "La película consultada no se encuentra en el dataset."}
    
    idx_pelicula = pelicula.index[0]
    puntuaciones_similitud = list(enumerate(similitud[idx_pelicula]))
    puntuaciones_similitud = sorted(puntuaciones_similitud, key=lambda x: x[1], reverse=True)
    peliculas_similares = puntuaciones_similitud[1:11]

    peliculas_ids = [i[0] for i in peliculas_similares]
    recomendaciones = dataframe_unido_modelo.iloc[peliculas_ids][['title', 'overview', 'popularity']]

    return recomendaciones.to_dict(orient='records')