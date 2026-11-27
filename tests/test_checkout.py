import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_exitoso(driver):

    # Iniciar sesión
    login_page = LoginPage(driver)
    login_page.abrir_pagina()
    login_page.login("standard_user", "secret_sauce")

    # Agregar un producto al carrito
    inventory_page = InventoryPage(driver)
    inventory_page.agregar_producto("Sauce Labs Backpack")

    assert inventory_page.obtener_contador_carrito() == "1"

    # Navegar al carrito
    inventory_page.ir_al_carrito()

    cart_page = CartPage(driver)

    assert cart_page.obtener_titulo() == "Your Cart"
    assert cart_page.obtener_nombre_producto() == "Sauce Labs Backpack"
    assert cart_page.obtener_precio_producto() == 29.99

    # Iniciar el checkout
    cart_page.hacer_click_checkout()

    checkout_page = CheckoutPage(driver)

    assert checkout_page.obtener_titulo() == "Checkout: Your Information"
    
    # Completar la información del checkout    
    checkout_page.completar_formulario("Juan", "Pérez", "12345")
    checkout_page.hacer_click_continue()
    
    # Verificar que se haya navegado a la página de resumen
    assert checkout_page.obtener_titulo() == "Checkout: Overview"
    
    # Verificar el nombre y precio del producto en la página de resumen
    assert checkout_page.obtener_nombre_producto() == "Sauce Labs Backpack"
    assert checkout_page.obtener_precio_producto() == 29.99
    
    # Verificar el subtotal, impuestos y total
    assert checkout_page.obtener_subtotal() == 29.99
    assert checkout_page.obtener_impuesto() == 2.40
    assert checkout_page.obtener_total() == 32.39
    
    # Completar el checkout
    checkout_page.hacer_click_finish()
    
    # Verificar que se haya navegado a la página de confirmación
    assert checkout_page.obtener_titulo() == "Checkout: Complete!"
    
    # Verificar el mensaje de confirmación
    assert checkout_page.obtener_mensaje_confirmacion() == "Thank you for your order!"
   # assert checkout_page.obtener_mensaje_confirmacion() == "Compra exitosa"