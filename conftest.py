import pytest
from selenium import webdriver
import pytest_html
import pathlib
import base64
from datetime import datetime
import os


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    navegador = webdriver.Chrome(options=options)

    yield navegador

    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver is not None:

            carpeta = pathlib.Path("reports/screenshots")
            carpeta.mkdir(parents=True, exist_ok=True)

            fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            archivo = carpeta / f"{item.name}_{fecha_hora}.png"

            driver.save_screenshot(str(archivo))

            imagen = base64.b64encode(
                archivo.read_bytes()
            ).decode("utf-8")

            report.extras = [
                pytest_html.extras.png(imagen, name="Screenshot")
            ]
            
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {"x-api-key": os.environ["REQRES_API_KEY"]}