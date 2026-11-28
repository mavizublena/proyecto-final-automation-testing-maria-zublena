from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger

def test_carrito(driver):
    try:
        logger.info("Iniciando prueba del carrito de compras")

        # Iniciar sesión
        login_page = LoginPage(driver)
        login_page.abrir_pagina()
        login_page.login("standard_user", "secret_sauce")
        logger.info("Login exitoso")

        # Crear el objeto InventoryPage
        inventory_page = InventoryPage(driver)

        # Agregar un producto al carrito
        inventory_page.agregar_producto("Sauce Labs Backpack")
        logger.info("Producto agregado al carrito: Sauce Labs Backpack")

        # Verificar que el carrito tenga un producto
        assert inventory_page.obtener_contador_carrito() == "1"
        logger.info("Contador del carrito verificado correctamente")

        # Navegar al carrito
        inventory_page.ir_al_carrito()
        logger.info("Navegación al carrito exitosa")

        # Verificar que se haya navegado al carrito
        cart_page = CartPage(driver)
        assert cart_page.obtener_titulo() == "Your Cart"
        logger.info("Título del carrito verificado correctamente")

        # Verificar el nombre y precio del producto en el carrito
        nombre_producto = cart_page.obtener_nombre_producto()
        precio_producto = cart_page.obtener_precio_producto()
        

        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == 29.99
        
        logger.info("Nombre y precio del producto en el carrito verificados correctamente")
        logger.info(f"Producto verificado: {nombre_producto}, Precio: ${precio_producto}")
        
    except Exception:
        logger.exception("Error durante la prueba del carrito de compras")
        raise
    
