from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def test_login_exitoso(driver):

    # Crear el objeto LoginPage
    login_page = LoginPage(driver)

    # Abrir la página e iniciar sesión
    login_page.abrir_pagina()
    login_page.login("standard_user", "secret_sauce")

    # Validar el inicio de sesión
    assert "/inventory.html" in driver.current_url

    # Validar el logo
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == "Swag Labs"

    # Validar el título
    titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
    assert titulo.text == "Products"