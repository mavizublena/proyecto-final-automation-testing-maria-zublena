import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    navegador = webdriver.Chrome(options=options)
    navegador.implicitly_wait(10)

    yield navegador

    navegador.quit()