# Importar las librerias para crear la api
from fastapi import FastAPI
import pandas as pd


# crear una instancia para definir las rutas y funciones que se van a tomar como endpoints
aplicacion = FastAPI()

# Extraer los datos de los dataframe
credits_df_parquet = pd.read_parquet('Datasets/credits_dataset_parquet')
movies_df_parquet = pd.read_parquet('Datasets/movies_dataset_parquet')


# Crear un decorador para la ruta principal que va a definir el endpoint raiz
@aplicacion.get("/")

def inicio():
    """
    Ruta raíz de la API que retorna un mensaje de bienvenida.
    No recibe ningun parametro.
    
    """
    return {"mensaje": "Esta es una API para realizar consultas sobre películas"}

# Crear un ruta para hacer consultas sobre cantidad de peliculas en un mes dado

@aplicacion.get("/cantidad_peliculas_mes/{mes}")

def cantidad_peliculas_mes(mes: str):

    """
    Consulta la cantidad de películas estrenadas en un mes específico.

    Parámetros:
        mes: Nombre del mes consultado en español.
    Retorna:
        Si el mes es valido retorna la cantidad de peliculas que fueron estrenadas en un mes especifico.
        Si el mes no es valido retorna un mensaje de error. 
    """
    # crear un diccionario para traducir meses en español a números
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5,
        "junio": 6, "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10,
        "noviembre": 11, "diciembre": 12
    }
    
     # Verificar si el mes es válido es decir se encuentra dentro del diccionario meses

    numero_del_mes = meses.get(mes.lower())
    if numero_del_mes:

        # si es valido va a filtrar el archivo para contar las peliculas del mes dado
        cantidad = movies_df_parquet[movies_df_parquet['release_date'].dt.month == numero_del_mes].shape[0]
        
        return {"mensaje": f"En el mes de {mes}, se estrenaron {cantidad} películas."}
    else:
        return {"error": "El mes consultado es no es valido. Por favor ingrese un mes válido en español."}
    
    # Crear un ruta para hacer consultas sobre cantidad de peliculas en un dia dado

@aplicacion.get("/cantidad_peliculas_dia/{dia}")

def cantidad_peliculas_dia(dia: str):
    """
    Consulta la cantidad de películas que fueron estrenadas en un día específico de la semana.

    Parametros:
        dia: dia de la semana en español en formato string.
    Retorna:
        Si el dia es valido retorna un mensaje con la cantidad de películas que fueron estrenadas en un día especifico.
        Si el dia no es valido retorna un mensaje de error.
    """
    # Diccionario para traducir días de español a números
    dias = {
        "lunes": 1, "martes": 2, "miercoles": 3, "jueves": 4,
        "viernes": 5, "sabado": 6, "domingo": 7
    }
    
    # Obtener el número del dia correspondiente al nombre ingresado convirtiendolo en minusculas y buscandolo en el diccionario
    numero_de_dia = dias.get(dia.lower())

     # Verificar si el día ingresado es válido
    if numero_de_dia is not None:

        # Filtrar el DataFrame para contar las películas estrenadas en el día especificado
        cantidad_de_peliculas = movies_df_parquet[movies_df_parquet['release_date'].dt.weekday == numero_de_dia].shape[0]

        return {"mensaje": f"La cantidad de peliculas estrenadas en los dias {dia} fueron {cantidad_de_peliculas} "}
    else:
        return {"error": "El Dia consultado no es valido. Por favor ingrese un dia de la semana en español."}
    
    # Crear una ruta para hacer consultas sobre la cantidad de peliculas en una fecha especifica

@aplicacion.get("/cantidad_peliculas_fecha/{dia}/{mes}/{anio}")

def cantidad_filmaciones_fecha(dia: int, mes: int, anio: int):
    """
    Consulta la cantidad de películas que fueron estrenadas en una fecha específica (día, mes, año).

    Parametros:
        dia: El día consultado en formato numerico.
        mes: El mes consultado en formato numérico.
        anio: El año consultado en formato numerico.

    Retorna:
        Si el dia es valido retorna un mensaje indicando la cantidad de películas que fueron estrenadas en la fecha indicada.
        Si el dia no es valido o no es encontrado retorna un mensaje de error.
    """

    try:
        # Crear un objeto de fecha usando los parámetros de día, mes y año
        fecha_especifica = pd.Timestamp(year=anio, month=mes, day=dia)
        
        # Filtrar el DataFrame para contar las películas que coinciden con la fecha especificada
        cantidad_de_peliculas = movies_df_parquet[movies_df_parquet['release_date'] == fecha_especifica].shape[0]

        # Retornar un mensaje indicando la cantidad de películas estrenadas en la fecha específica
        return {"mensaje": f"{cantidad_de_peliculas} películas fueron estrenadas el {dia}/{mes}/{anio}"}
    
    except ValueError:
        # Si hay un error en la construcción de la fecha (por ejemplo, si la fecha no es válida), manejar el error
        return {"error": "La fecha consultada no es valida. Por favor ingrese una fecha válida en formato numérico dd/mm/YYYY."}
    
# Crear una ruta para hacer consultas sobre una película dado su título

@aplicacion.get("/puntaje_pelicula/{nombre}")

def puntaje_pelicula(nombre: str):
    """
    obtiene el nombre de la pelicula, el año de estreno y el puntaje de una película específica basada en el título dado.
    
    Parametros:
        nombre: Título de la película.
    Retorna:
        si el nombre de la pelicula es valido retorna un mensaje con el título, año de estreno y puntaje promedio de la película.
        si el titulo no es valido (pelicula no encontrada) retorna un mensaje de error.
    """
    # Filtrar el DataFrame para encontrar la película cuyo título coincida (ignorando mayúsculas/minúsculas)
    pelicula = movies_df_parquet[movies_df_parquet['title'].str.lower() == nombre.lower()]

    # Verificar si se encontró la película
    if not pelicula.empty:

        # Extraer los valores del nombre, año y puntaje de la primera coincidencia encontrada
        nombre = pelicula['title'].values[0]
        anio = int(pelicula['release_year'].values[0]) #convertir el año a un numero entero
        puntaje = pelicula['vote_average'].values[0]
        
        return {"mensaje": f"La película {nombre} fue estrenada en el año {anio} con un puntaje de {puntaje}"}
    else:
        return {"error": "La pelicula consultada no fue encontrada en la base de datos."}

# Crear una ruta para hacer consultas sobre la cantidad de votos que tuvo una película

@aplicacion.get("/votos_pelicula/{nombre}")

def votos_pelicula(nombre: str):
    """
    Obtiene el nombre, la cantidad de votos y el promedio de votaciones de una pelicula especifica.

    Parametros :
        nombre : el nombre de una película (no es sensible a mayúsculas/minúsculas).

    Retorna:
        Si el nombre de la pelicula es valido y cuenta con 2000 votos o mas retorna, Un mensaje con el nombre, año de estreno, cantidad de votos y promedio de votaciones de la película.
        Si el nombre de la pelicula es valido pero no cumple los 2000 votos retorna un mensaje indicando dicha condicion.
        Si el nombre de la pelicula no es valido (pelicula no encontrada) retorna un mensaje de error.
    """
    # Filtrar el DataFrame para encontrar la película cuyo nombre coincida (ignorando mayúsculas/minúsculas)
    pelicula = movies_df_parquet[movies_df_parquet['title'].str.lower() == nombre.lower()]

    # Verificar si se encontró la película
    if not pelicula.empty:

        # Extraer los valores del nombre, año, cantidad de votos y promedio de votaciones de la primera coincidencia encontrada
        nombre = pelicula['title'].values[0]
        anio = int(pelicula['release_year'].values[0]) #convertir el año a un numero entero
        votos = int(pelicula['vote_count'].values[0]) #convertir la cantidad de votos a un numero entero
        promedio_votos = pelicula['vote_average'].values[0]
        
        if votos >= 2000:
            return {"mensaje": f"La película {nombre} fue estrenada en el año {anio}. Tiene un total de {votos} votos, con un promedio de {promedio_votos}"}
        else:
            return {"mensaje": f"La película {nombre} no cumple con los 2000 votos requeridos. Tiene solo {votos} votos."}
    else:
        return {"error": "El nombre de la pelicula consultada no fue encontrado."}
    
# Crear una ruta para hacer consultas sobre el éxito de un actor

@aplicacion.get("/obtener_exito_actor/{nombre_actor}")

def obtener_exito_actor(nombre_actor: str):
    """
    Obtiene el éxito del actor medido a través del retorno generado, 
    la cantidad de películas en las que ha participado y calcula el promedio del retorno generado.

    Parámetro:
        nombre_actor: El nombre del actor (no es sensible a mayúsculas/minúsculas).

    Retorna:
        Si el nombre del actor es válido, retorna un mensaje con la cantidad de películas, el retorno total generado,
        el promedio de retorno generado por película del actor, y la ganancia total en las películas interpretadas.
        Si el nombre del actor no es válido, retorna un mensaje de error.
    """
    
    # Limpiar el nombre del actor antes de hacer el filtro
    nombre_actor_limpio = nombre_actor.lower().strip()

    # Filtrar el DataFrame de créditos para encontrar películas donde el actor haya participado
    peliculas_por_actor = credits_df_parquet[credits_df_parquet['cast_name_actor'].str.lower().str.strip() == nombre_actor_limpio]

    # Verificar si se encontraron películas
    if not peliculas_por_actor.empty:
        # Convertir la columna 'id_credits' a tipo int para asegurar la coincidencia de tipo de datos
        peliculas_por_actor['id_credits'] = pd.to_numeric(peliculas_por_actor['id_credits'], errors='coerce', downcast='integer')
        
        # Obtener los IDs de las películas en las que el actor ha participado
        peliculas_ids_columna = 'id_credits'  # Nombre de la columna en credits_df_parquet
        peliculas_ids = peliculas_por_actor[[peliculas_ids_columna]].drop_duplicates()

        # Convertir la columna 'id_movies' a tipo int para asegurar la coincidencia de tipo de datos
        movies_df_parquet['id_movies'] = pd.to_numeric(movies_df_parquet['id_movies'], errors='coerce', downcast='integer')

        # Unir los DataFrames de películas y créditos usando la columna 'id_movies' para el DataFrame de películas
        peliculas_actor_df = pd.merge(peliculas_ids, movies_df_parquet, left_on=peliculas_ids_columna, right_on='id_movies', how='inner')

        # Inicializar las variables de retorno, costo y ganancia
        total_retorno = 0
        total_ganancia = 0

        # Contar el número de películas
        num_peliculas = len(peliculas_actor_df)
        
        # Calcular las métricas
        for _, pelicula in peliculas_actor_df.iterrows():
            retorno_generado = pelicula['return']
            ganancia_generada = pelicula['revenue']

            # Acumular los totales
            total_retorno += retorno_generado
            total_ganancia += ganancia_generada

        # Calcular el retorno promedio
        retorno_promedio = total_retorno / num_peliculas if num_peliculas > 0 else 0

        # Retornar el resumen del éxito del actor
        return {
            "mensaje": f"El actor {nombre_actor} ha participado en {num_peliculas} peliculas, el mismo ha conseguido un retorno total de {total_retorno} con un retorno promedio de {retorno_promedio} por pelicula con una ganancia total de ${total_ganancia} en las películas interpretadas."
        }

    # Si no se encontraron películas, retornar un mensaje de error
    else:
        return {"error": f"El nombre {nombre_actor} no tiene películas registradas en la base de datos de actores."}



    
# Crear una ruta para hacer consultas sobre el éxito de un director

@aplicacion.get("/obtener_exito_director/{nombre_director}")

def obtener_exito_director(nombre_director: str):
    """
    Obtiene el éxito del director medido a través del retorno generado, 
    la cantidad de películas que ha dirigido y calcula el promedio del retorno generado.

    Parámetro:
        nombre_director: El nombre del director (no es sensible a mayúsculas/minúsculas).

    Retorna:
        Si el nombre del director es válido y se encuentra como director, retorna un mensaje con la cantidad de películas,
        el retorno total generado, el promedio de retorno generado por película del director, la ganancia total y una lista
        de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia.
        Si el nombre se encuentra pero no es un director, retorna un mensaje indicando que la persona no es director.
        Si el nombre no se encuentra, retorna un mensaje de error.
    """
    
    # Limpiar el nombre del director antes de hacer el filtro
    nombre_director_limpio = nombre_director.lower().strip()

    # Filtrar el DataFrame de créditos para encontrar todas las películas en las que la persona ha trabajado
    peliculas_por_director = credits_df_parquet[
        (credits_df_parquet['crew_name_member'].str.lower().str.strip() == nombre_director_limpio)
    ]

    # Verificar si se encontraron créditos para la persona
    if not peliculas_por_director.empty:
        # Filtrar para encontrar solo aquellos créditos donde el rol es 'Director'
        peliculas_director = peliculas_por_director[peliculas_por_director['crew_job'] == 'Director']
        
        # Verificar si se encontraron créditos con el rol de director
        if not peliculas_director.empty:
            # Convertir la columna 'id_credits' a tipo int para asegurar la coincidencia de tipo de datos
            peliculas_director['id_credits'] = pd.to_numeric(peliculas_director['id_credits'], errors='coerce', downcast='integer')
            
            # Obtener los IDs de las películas en las que el director ha trabajado
            peliculas_ids_columna = 'id_credits'  # Nombre de la columna en credits_df_parquet
            peliculas_ids = peliculas_director[[peliculas_ids_columna]].drop_duplicates()

            # Convertir la columna 'id_movies' a tipo int para asegurar la coincidencia de tipo de datos
            movies_df_parquet['id_movies'] = pd.to_numeric(movies_df_parquet['id_movies'], errors='coerce', downcast='integer')

            # Unir los DataFrames de películas y créditos usando la columna 'id_movies' para el DataFrame de películas
            peliculas_director_df = pd.merge(peliculas_ids, movies_df_parquet, left_on=peliculas_ids_columna, right_on='id_movies', how='inner')

            # Inicializar las variables de retorno, costo y ganancia
            total_retorno = 0
            total_ganancia = 0

            # Contar el número de películas
            num_peliculas = len(peliculas_director_df)
            
            # Calcular las métricas
            for _, pelicula in peliculas_director_df.iterrows():
                retorno_generado = pelicula['return']
                costo = pelicula['budget']
                ganancia_generada = pelicula['revenue']

                # Acumular los totales
                total_retorno += retorno_generado
                total_ganancia += ganancia_generada

            # Calcular el retorno promedio
            retorno_promedio = total_retorno / num_peliculas if num_peliculas > 0 else 0

            # Crear una lista de películas con sus detalles
            peliculas_detalles = [
                {
                    "titulo": pelicula['title'],
                    "fecha_estreno": pelicula['release_date'],
                    "retorno": pelicula['return'],
                    "costo": pelicula['budget'],
                    "ganancia": pelicula['revenue']
                }
                for _, pelicula in peliculas_director_df.iterrows()
            ]

            # Retornar el resumen del éxito del director
            return {
                "mensaje": f"El director {nombre_director} ha dirigido {num_peliculas} películas con un retorno total de {total_retorno} y un promedio de retorno de {retorno_promedio} por película con una ganancia total de ${total_ganancia}.",
                "Las peliculas dirigidas son": peliculas_detalles
            }
        else:
            # Retornar un mensaje indicando que la persona no es un director
            return {"mensaje": f"El nombre {nombre_director} se encuentra en la base de datos, pero no tiene el rol de director en las películas registradas."}
    
    # Si no se encontraron créditos para la persona, retornar un mensaje de error
    else:
        return {"error": f"El nombre {nombre_director} no se encuentra en la base de datos de directores."}