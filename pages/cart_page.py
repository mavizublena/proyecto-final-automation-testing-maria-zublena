from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    # Localizadores
    NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
    PRECIO_PRODUCTO = (By.CLASS_NAME, "inventory_item_price")
    TITULO = (By.CSS_SELECTOR, "[data-test='title']")
    BOTON_CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_nombre_producto(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.NOMBRE_PRODUCTO)
        ).text

    def obtener_precio_producto(self):
        precio = self.wait.until(
            EC.visibility_of_element_located(self.PRECIO_PRODUCTO)
        ).text
        return float(precio.replace("$", ""))

    def obtener_titulo(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TITULO)
        ).text
        
    def hacer_click_checkout(self):
       self.wait.until(
        EC.element_to_be_clickable(self.BOTON_CHECKOUT)
       ).click()   