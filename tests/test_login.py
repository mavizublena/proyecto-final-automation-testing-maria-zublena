from selenium.webdriver.common.by import By


def test_login_exitoso(driver):

    # Abrir la página de inicio de sesión
    driver.get("https://www.saucedemo.com/")

    # Ingresar credenciales válidas
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Validar el inicio de sesión
    assert "/inventory.html" in driver.current_url

    # Validar el logo
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == "Swag Labs"

    # Validar el título
    titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
    assert titulo.text == "Products"
    