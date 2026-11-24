from selenium.webdriver.common.by import By


def test_inventory_page(driver):

    # Login
    driver.get("https://www.saucedemo.com/")

    # Ingresar credenciales válidas
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Verificar que el título sea correcto
    titulo = driver.title
    assert titulo == "Swag Labs"

    # Verificar que haya productos
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0

    # Listar nombre y precio del primer producto
    primer_producto = productos[0]
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    print(f"Nombre: {nombre_producto}, Precio: {precio_producto}")

    assert nombre_producto == "Sauce Labs Backpack"
    assert precio_producto == "$29.99"

    # Verificar la existencia del menú hamburguesa
    menu_hamburguesa = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_hamburguesa.is_displayed()

    # Verificar la existencia del filtro de ordenamiento
    filtro_ordenamiento = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro_ordenamiento.is_displayed()