import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    navegador = webdriver.Chrome(options=options)
    navegador.implicitly_wait(10)

    time.sleep(5)
    yield navegador

    navegador.quit()