
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger


def test_inventory_page(driver):
    try:
        logger.info("Iniciando prueba de la página de inventario")

        # Iniciar sesión
        login_page = LoginPage(driver)
        login_page.abrir_pagina()
        login_page.login("standard_user", "secret_sauce")
        logger.info("Login exitoso")

        # Verificar que el título sea correcto
        inventory_page = InventoryPage(driver)
        assert inventory_page.obtener_titulo() == "Products"
        logger.info("Título verificado correctamente")

        # Verificar que haya productos
        productos = inventory_page.obtener_productos()
        assert len(productos) > 0
        logger.info(f"Se encontraron {len(productos)} productos en la página de inventario")

        # Listar nombre y precio del primer producto
        nombre_producto = inventory_page.obtener_nombre_primer_producto()
        precio_producto = inventory_page.obtener_precio_primer_producto()

        logger.info(f"Nombre: {nombre_producto}, Precio: {precio_producto}")

        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"
        logger.info("Nombre y precio del primer producto verificados correctamente")

        # Verificar la existencia del menú hamburguesa
        assert inventory_page.menu_visible()
        logger.info("Menú hamburguesa verificado correctamente")

        # Verificar la existencia del filtro de ordenamiento
        assert inventory_page.filtro_visible()
        logger.info("Filtro de ordenamiento verificado correctamente")

    except Exception:
        logger.exception("Error durante la prueba de inventario")
        raise
