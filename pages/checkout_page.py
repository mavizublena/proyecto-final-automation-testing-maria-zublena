from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    TITULO = (By.CSS_SELECTOR, "[data-test='title']")
    NOMBRE = (By.ID, "first-name")
    APELLIDO = (By.ID, "last-name")
    CODIGO_POSTAL = (By.ID, "postal-code")
    BOTON_CONTINUE = (By.ID, "continue")
    
    NOMBRE_PRODUCTO = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    PRECIO_PRODUCTO = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    SUBTOTAL = (By.CSS_SELECTOR, "[data-test='subtotal-label']")
    IMPUESTO = (By.CSS_SELECTOR, "[data-test='tax-label']")
    TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")
    BOTON_FINISH = (By.CSS_SELECTOR, "[data-test='finish']")
    
    MENSAJE_CONFIRMACION = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def completar_formulario(self, nombre, apellido, codigo_postal):
        self.wait.until(
            EC.visibility_of_element_located(self.NOMBRE)
        ).send_keys(nombre)
        self.wait.until(
            EC.visibility_of_element_located(self.APELLIDO)
        ).send_keys(apellido)
        self.wait.until(
            EC.visibility_of_element_located(self.CODIGO_POSTAL)
        ).send_keys(codigo_postal)
        
        
    def obtener_titulo(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TITULO)
        ).text
        
    def hacer_click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BOTON_CONTINUE)
        ).click()   
        
    def obtener_nombre_producto(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.NOMBRE_PRODUCTO)
        ).text    

    def obtener_precio_producto(self):
        precio = self.wait.until(
            EC.visibility_of_element_located(self.PRECIO_PRODUCTO)
        ).text
        return float(precio.replace("$", ""))
    
    def obtener_subtotal(self):
        subtotal = self.wait.until(
            EC.visibility_of_element_located(self.SUBTOTAL)
        ).text
        return float(subtotal.replace("Item total: $", ""))
    
    def obtener_impuesto(self):
        impuesto = self.wait.until(
            EC.visibility_of_element_located(self.IMPUESTO)
        ).text
        return float(impuesto.replace("Tax: $", ""))

    def obtener_total(self):
        total = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL)
        ).text
        return float(total.replace("Total: $", ""))
    
    def hacer_click_finish(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BOTON_FINISH)
        ).click()
        
    def obtener_mensaje_confirmacion(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MENSAJE_CONFIRMACION)
        ).text