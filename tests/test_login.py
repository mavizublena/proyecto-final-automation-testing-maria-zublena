import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.reader import read_users_csv


@pytest.mark.parametrize("data", read_users_csv())
def test_login(driver, data):

    login_page = LoginPage(driver)
    login_page.abrir_pagina()

    login_page.login(data["usuario"], data["password"])

    if data["tipo_usuario"] == "True":

        assert "/inventory.html" in driver.current_url

        inventory_page = InventoryPage(driver)

        assert inventory_page.obtener_logo() == "Swag Labs"
        assert inventory_page.obtener_titulo() == "Products"

    elif data["tipo_usuario"] == "False":

        error = login_page.obtener_mensaje_error()

        assert error == data["mensaje_error"]

    else:
        pytest.fail("Tipo de usuario no válido en el CSV")
