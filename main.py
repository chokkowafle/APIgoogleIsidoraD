import requests 
# Importa la biblioteca requests para realizar solicitudes HTTP

from dotenv import load_dotenv 
# Importa funcion Load_dovent para cargar variables de entorno de un archivo .env

import os
# Importa el modulo os que proporciona funcions para interactuar con el sist. operativo, asi se logra acceder a las variables de entorno

def load_environment_variables(): 
    """Carga las variables de entorno necesarias.""" 
#Define una funcion para cargar y validar las variables
    
    load_dotenv() 
# Carga las variables de entorno desde el archivo .env

    api_key = os.getenv("API_KEY_SEARCH_GOOGLE") 
    search_engine_id = os.getenv("SEARCH_ENGINE_ID") 
# Desde aquí, se obtienen las variables de entorno "API_KEY..." y "SEARCH_ENG..." usando ost.getenv

    if not api_key or not search_engine_id:
        raise ValueError("Las variables de entorno API_KEY_SEARCH_GOOGLE o SEARCH_ENGINE_ID no están configuradas.")
# En el caso de que alguna de las variables no esté configurada, se arroja un mensaje de error

    return api_key, search_engine_id
# Devuelve las variables de entorno necesarias para la búsqueda


def build_search_url(api_key, search_engine_id, query, page, lang):
    """Construye la URL para la API de Google Custom Search."""
# Define una función para construir la URL de búsqueda personalizada de Google

    return (
        f"https://www.googleapis.com/customsearch/v1?"
        f"key={api_key}&cx={search_engine_id}&q={query}&start={page}&lr={lang}"
    )
# Devuelve la URL de busqueda con los parametros necesarios para la API


def fetch_search_results(url):
    """Realiza la solicitud a la API y devuelve los resultados en formato JSON."""
# Se define la funcion para solicitar la API y devolver los resultados en formato JSON

    response = requests.get(url)
# Solicitud HTTP GET a la URL

    if response.status_code != 200:
        raise Exception(f"Error en la solicitud: {response.status_code} - {response.text}")
# Si la respuesta no es ecitosa (code diferente a 200) se arroja un mensaje de error

    return response.json()
# Devuelve la respuesta en formato JSON

def display_results(results):
    """Muestra los resultados de la búsqueda en la consola."""
#Define la funcion para mostrar los resultados de la busqueda en la consola

    if not results:
        print("No se encontraron resultados.")
        return
# Si no hay resultados, se imprime un mensaje y se sale de la funcion

    for item in results:
        title = item.get('title')
        link = item.get('link')
        snippet = item.get('snippet')
# Itera sobre los resultados, se extrae el titulo, enlace y snippet(fragmento) de cada elemento

        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Snippet: {snippet}")
        print("-" * 80)
# se imprime (print) los detalles de cada resultado en un formato legible y ordenado



def main():
    """Función principal del programa."""
# Define la funcion principal del programa 

    try:
        api_key, search_engine_id = load_environment_variables()
# Se cargan las variables de entorno necesarias

        query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
        page = 1
        lang = "lang_es"
# Configuración de la consulta y los parámetros de búsqueda

        url = build_search_url(api_key, search_engine_id, query, page, lang)
        data = fetch_search_results(url)
# Construcción de la URL y obtención de resultados

        results = data.get('items', [])
        display_results(results)
 # Procesamiento y visualización de resultados

    except Exception as e:
        print(f"Error: {e}")
# Manejo de excepciones para capturar errores durante la ejecución del programa


if __name__ == "__main__":
    main()
# Verifica si el script se está ejecutando directamente y llama a la función principal