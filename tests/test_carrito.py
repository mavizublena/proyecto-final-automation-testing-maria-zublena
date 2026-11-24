from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def test_carrito(driver):

    # Iniciar sesión
    login_page = LoginPage(driver)
    login_page.abrir_pagina()
    login_page.login("standard_user", "secret_sauce")

    # Agregar un producto al carrito
    boton_agregar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    boton_agregar.click()

    # Verificar que el carrito tenga un producto
    cantidad_carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cantidad_carrito.text == "1"

    # Navegar al carrito
    carrito = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )
    carrito.click()

    # Esperar hasta que navegue al carrito
    WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

    # Verificar que se haya navegado al carrito
    assert "/cart.html" in driver.current_url