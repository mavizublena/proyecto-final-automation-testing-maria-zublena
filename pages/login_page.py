from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Localizadores
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error > h3")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")

    def ingresar_usuario(self, usuario):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(usuario)

    def ingresar_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

    def hacer_click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def obtener_mensaje_error(self):
        texto_error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return texto_error.text

    def login(self, usuario, password):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_click_login()