from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_carrito(driver):

    # Iniciar sesión
    login_page = LoginPage(driver)
    login_page.abrir_pagina()
    login_page.login("standard_user", "secret_sauce")

    # Crear el objeto InventoryPage
    inventory_page = InventoryPage(driver)

    # Agregar un producto al carrito
    inventory_page.agregar_producto("Sauce Labs Backpack")

    # Verificar que el carrito tenga un producto
    assert inventory_page.obtener_contador_carrito() == "1"

    # Navegar al carrito
    inventory_page.ir_al_carrito()

    # Verificar que se haya navegado al carrito
    cart_page = CartPage(driver)
    assert cart_page.obtener_titulo() == "Your Cart"
    
    # Verificar el nombre y precio del producto en el carrito
    nombre_producto = cart_page.obtener_nombre_producto()
    precio_producto = cart_page.obtener_precio_producto()
    
    assert nombre_producto == "Sauce Labs Backpack"
    assert precio_producto == 29.99
    
    
