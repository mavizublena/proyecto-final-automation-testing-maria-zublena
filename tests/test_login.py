import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.reader import read_users_csv
from utils.logger import logger


@pytest.mark.parametrize("data", read_users_csv())
def test_login(driver, data):

    try:
        logger.info("Iniciando prueba de login")

        login_page = LoginPage(driver)
        login_page.abrir_pagina()
        logger.info("Pagina abierta correctamente")

        login_page.login(data["usuario"], data["password"])
        logger.info(f"Credenciales ingresadas para: {data['usuario']}")

        if data["tipo_usuario"] == "True":

            assert "/inventory.html" in driver.current_url

            inventory_page = InventoryPage(driver)

            assert inventory_page.obtener_logo() == "Swag Labs"
            assert inventory_page.obtener_titulo() == "Products"

            logger.info("Login exitoso. Logo y titulo verificados")

        elif data["tipo_usuario"] == "False":

            error = login_page.obtener_mensaje_error()

            assert error == data["mensaje_error"]

            logger.info(f"Mensaje de error validado: {error}")

        else:
            pytest.fail("Tipo de usuario no valido en el CSV")

    except Exception:
        logger.exception("Error durante la prueba de login")
        raise
