# Automatización QA - SauceDemo y ReqRes

## Descripción del proyecto

Proyecto final de automatización de pruebas funcionales de UI y API realizado con Python para el curso de Talento Tech.

El objetivo es validar las principales funcionalidades del sitio web SauceDemo y los servicios REST de la API pública ReqRes, aplicando buenas prácticas de automatización de pruebas.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Requests
- Pytest HTML
- Page Object Model (POM)
- Logging
- CSV
- Git y GitHub

## Estructura del proyecto

- `pages/`: clases, localizadores y métodos de interacción con las páginas.
- `tests/`: pruebas automatizadas de UI y API.
- `data/`: archivo CSV con los datos para las pruebas parametrizadas.
- `utils/`: funciones de lectura de datos y configuración del logging.
- `reports/`: reporte HTML y capturas de pantalla.
- `logs/`: registros generados durante cada ejecución.
- `conftest.py`: configuración de fixtures y capturas automáticas.
- `pytest.ini`: configuración de Pytest y generación de reportes.
- `requirements.txt`: dependencias del proyecto.
- `.gitignore`: archivos y carpetas excluidos del control de versiones.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/mavizublena/proyecto-final-automation-testing-maria-zublena.git
```

Ingresar a la carpeta del proyecto:

```bash
cd proyecto-final-automation-testing-maria-zublena
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows desde PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

Para ejecutar las pruebas de UI es necesario tener Google Chrome instalado.

## Ejecutar las pruebas

Ejecutar todas las pruebas:

```bash
python -m pytest tests/ -v
```

Ejecutar únicamente las pruebas de login:

```bash
python -m pytest tests/test_login.py -v
```

Ejecutar únicamente las pruebas de API:

```bash
python -m pytest tests/test_api.py -v
```

## Casos de prueba de UI

Sitio web: [SauceDemo](https://www.saucedemo.com/)

- Login exitoso.
- Login con usuario incorrecto.
- Login con contraseña incorrecta.
- Login con usuario vacío.
- Login con contraseña vacía.
- Login con usuario bloqueado.
- Validación de la página de inventario.
- Agregar y verificar un producto en el carrito.
- Validación del flujo completo de compra (checkout).

Las pruebas son independientes y se implementan utilizando el patrón de diseño Page Object Model (POM).

Los escenarios de login se encuentran parametrizados mediante un archivo CSV.

## Casos de prueba de API

API pública: [ReqRes](https://reqres.in/)

| Método | Caso de prueba | Código esperado |
|---|---|---|
| GET | Obtener un usuario | 200 |
| POST | Crear un usuario | 201 |
| DELETE | Eliminar un usuario | 204 |

Se validan los códigos de estado HTTP, los encabezados, la estructura y el contenido de las respuestas.

También se registran los tiempos de respuesta con fines informativos.

## Capturas de pantalla

Cuando falla una prueba de UI, se genera automáticamente una captura de pantalla que incluye el nombre del test, la fecha y la hora.

Las capturas se almacenan en `reports/screenshots/` y se incorporan al reporte HTML.

## Logging

Se generan archivos de logs que registran las acciones principales, las validaciones realizadas, los tiempos de respuesta de la API y las excepciones.

Los archivos se almacenan en la carpeta `logs/` y se identifican mediante la fecha y hora de ejecución.

## Reportes

El reporte HTML se genera automáticamente después de cada ejecución y se encuentra en:

`reports/report.html`

Permite visualizar los resultados de las pruebas, su duración, los errores y las capturas de pantalla correspondientes a los fallos de UI.

## Resumen de pruebas

| Tipo de prueba | Cantidad |
|---|---:|
| UI | 9 |
| API | 3 |
| **Total** | **12** |

## Control de versiones

El proyecto se desarrolló utilizando Git y GitHub, mediante ramas independientes para cada etapa y su posterior integración a la rama principal mediante Pull Requests.

## Autora

María Victoria Zublena

Proyecto final - Automation Testing - Talento Tech.