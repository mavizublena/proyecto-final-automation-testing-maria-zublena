
from pages.login_page import LoginPage 
from pages.inventory_page import InventoryPage


def test_inventory_page(driver):

    # Iniciar sesión
    login_page = LoginPage(driver)
    login_page.abrir_pagina()
    login_page.login("standard_user", "secret_sauce")
    
    # Verificar que el título sea correcto
    inventory_page = InventoryPage(driver)
    assert inventory_page.obtener_titulo() == "Products"

    # Verificar que haya productos   
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0
    
    # Listar nombre y precio del primer producto
    nombre_producto = inventory_page.obtener_nombre_primer_producto()
    precio_producto = inventory_page.obtener_precio_primer_producto()

    print(f"Nombre: {nombre_producto}, Precio: {precio_producto}")

    assert nombre_producto == "Sauce Labs Backpack"
    assert precio_producto == "$29.99"

    # Verificar la existencia del menú hamburguesa
    assert inventory_page.menu_visible()

    # Verificar la existencia del filtro de ordenamiento
    assert inventory_page.filtro_visible()