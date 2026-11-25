
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso(driver):

    # Crear el objeto LoginPage
    login_page = LoginPage(driver)

    # Abrir la página e iniciar sesión
    login_page.abrir_pagina()
    login_page.login("standard_user", "secret_sauce")

    # Validar el inicio de sesión
    assert "/inventory.html" in driver.current_url
    
    # Crear el objeto InventoryPage
    inventory_page = InventoryPage(driver)

    # Validar el logo
    assert inventory_page.obtener_logo() == "Swag Labs"

    # Validar el título
    assert inventory_page.obtener_titulo() == "Products"