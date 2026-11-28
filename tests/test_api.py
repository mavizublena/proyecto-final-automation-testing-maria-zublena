import requests
from utils.logger import logger


def test_obtener_usuario(base_url):
    try:
        logger.info("Iniciando prueba GET de usuario")

        url = f"{base_url}/users/2"
        response = requests.get(url, timeout=10)

        # NIVEL 1: STATUS CODE
        assert response.status_code == 200
        logger.info("Código de estado 200 verificado correctamente")

        # NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Tipo de contenido JSON verificado correctamente")

        # NIVEL 3: ESTRUCTURA
        data = response.json()

        assert isinstance(data, dict)
        assert "data" in data
        assert isinstance(data["data"], dict)

        assert "id" in data["data"]
        assert "email" in data["data"]
        assert "first_name" in data["data"]
        assert "last_name" in data["data"]

        logger.info("Estructura de la respuesta verificada correctamente")

        # NIVEL 4: CONTENIDO
        assert data["data"]["id"] == 2
        assert data["data"]["email"] == "janet.weaver@reqres.in"

        logger.info("Datos del usuario verificados correctamente")

        # NIVEL 5: TIEMPO DE RESPUESTA
        tiempo = response.elapsed.total_seconds()
        

        logger.info(f"Tiempo de respuesta: {tiempo:.3f} segundos")

    except Exception:
        logger.exception("Error durante la prueba GET de usuario")
        raise
    
def test_crear_usuario(base_url):
    try:
        logger.info("Iniciando prueba POST de creación de usuario")

        url = f"{base_url}/users"
        payload = {"name": "maria", "job": "QA tester"}
        response = requests.post(url, json=payload, timeout=10)

        # NIVEL 1: STATUS CODE
        assert response.status_code == 201
        logger.info("Código de estado 201 verificado correctamente")

        # NIVEL 2: HEADERS
        assert "application/json" in response.headers["Content-Type"]
        logger.info("Tipo de contenido JSON verificado correctamente")

        # NIVEL 3: ESTRUCTURA
        data = response.json()

        assert isinstance(data, dict)
        assert "name" in data
        assert "job" in data
        assert "id" in data
        assert "createdAt" in data

        logger.info("Estructura de la respuesta verificada correctamente")

        # NIVEL 4: CONTENIDO
        assert data["name"] == payload["name"]
        assert data["job"] == payload["job"]
        assert data["id"]
        assert data["createdAt"]

        logger.info("Datos del usuario creados verificados correctamente")
        
       
    except Exception:
        logger.exception("Error durante la prueba POST de creación de usuario")
        raise  
    
def test_eliminar_usuario(base_url):
    try:
        logger.info("Iniciando prueba DELETE de usuario")

        url = f"{base_url}/users/2"
        response = requests.delete(url, timeout=10)

        # NIVEL 1: STATUS CODE
        assert response.status_code == 204
        logger.info("Código de estado 204 verificado correctamente")

        # NIVEL 2: HEADERS
        assert "Content-Type" not in response.headers
        logger.info("Tipo de contenido JSON verificado correctamente")

        # NIVEL 3 4: ESTRUCTURA y contenido
        assert response.text == ""
        logger.info("Cuerpo de la respuesta vacío verificado correctamente")
        
         # NIVEL 5: REGISTRO DEL TIEMPO DE RESPUESTA
        tiempo = response.elapsed.total_seconds()
        logger.info(f"Tiempo de respuesta: {tiempo:.3f} segundos")

    except Exception:
        logger.exception("Error durante la prueba DELETE de usuario")
        raise
      