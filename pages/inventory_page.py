from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    # Localizadores
    PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
    PRECIO_PRODUCTO = (By.CLASS_NAME, "inventory_item_price")
    MENU = (By.ID, "react-burger-menu-btn")
    FILTRO = (By.CLASS_NAME, "product_sort_container")
    BOTON_AGREGAR = (By.CSS_SELECTOR, "button[id^='add-to-cart-']")
    CONTADOR_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    LOGO = (By.CLASS_NAME, "app_logo")
    TITULO = (By.CSS_SELECTOR, "[data-test='title']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_productos(self):
        return self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCTOS)
        )

    def obtener_nombre_primer_producto(self):
        productos = self.obtener_productos()
        return productos[0].find_element(*self.NOMBRE_PRODUCTO).text

    def obtener_precio_primer_producto(self):
        productos = self.obtener_productos()
        return productos[0].find_element(*self.PRECIO_PRODUCTO).text

    def menu_visible(self):
        menu = self.wait.until(
            EC.visibility_of_element_located(self.MENU)
        )
        return menu.is_displayed()

    def filtro_visible(self):
        filtro = self.wait.until(
            EC.visibility_of_element_located(self.FILTRO)
        )
        return filtro.is_displayed()

    def agregar_producto(self, nombre):
        productos = self.obtener_productos()

        for producto in productos:
            nombre_producto = producto.find_element(
                *self.NOMBRE_PRODUCTO
            ).text

            if nombre_producto == nombre:
                producto.find_element(*self.BOTON_AGREGAR).click()
                return

        raise AssertionError(f"No se encontró el producto: {nombre}")

    def obtener_contador_carrito(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CONTADOR_CARRITO)
        ).text

    def ir_al_carrito(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CARRITO)
        ).click()

    def obtener_logo(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGO)
        ).text

    def obtener_titulo(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TITULO)
        ).text

    