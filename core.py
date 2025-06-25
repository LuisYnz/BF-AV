import logging
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from concurrent.futures import ThreadPoolExecutor

# Configuración básica de logging
def configure_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


def get_driver(browser_type):
    """ Función para obtener el driver adecuado según el tipo de navegador """
    if browser_type == 'chrome':
        chrome_options = Options()
        # Descomentar la siguiente línea para ejecutar en modo "headless" (sin interfaz gráfica)
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_type == 'edge':
        edge_options = EdgeOptions()
        # Descomentar la siguiente línea para ejecutar en modo "headless" (sin interfaz gráfica)
        # edge_options.add_argument("--headless")
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError(f"Navegador no soportado: {browser_type}")
    
    driver.maximize_window()
    return driver


def execute_test_step(driver, component_instance, step_description, step_action):
    try:
        logging.info(step_description)
        step_action()  # Ejecuta la acción
        logging.info(f"Paso '{step_description}' ejecutado con éxito.")
    except WebDriverException as e:  # Captura excepciones de Selenium
        logging.error(f"Error en el paso '{step_description}': {e}")
        driver.save_screenshot(f"error_{step_description.replace(' ', '_')}.png")
    except Exception as e:  # Captura otras excepciones
        logging.error(f"Error inesperado en el paso '{step_description}': {e}")
    # No se relanza la excepción, la ejecución continúa


def run_tests_for_url(url, browser_type, suite_functions):
    """ Función para ejecutar las pruebas en una URL específica con un navegador específico """
    driver = get_driver(browser_type)

    try:
        # Navegar a la página web que estás probando
        driver.get(url)

        # Ejecutar las suites de pruebas
        logging.info(f"Iniciando la ejecución de las pruebas para la URL: {url} en {browser_type}")
        for suite in suite_functions:
            suite(driver)

        logging.info(f"Finalizada la ejecución de las pruebas para la URL: {url} en {browser_type}")
    except Exception as e:
        logging.error(f"Ocurrió un error durante la ejecución de las pruebas para la URL {url} en {browser_type}: {e}")
    finally:
        driver.quit()  # Asegurar que el driver se cierre al finalizar, incluso si hay errores


def run_tests_parallel(urls, browsers, suite_functions):
    """ Función para ejecutar las pruebas de Selenium en paralelo en diferentes navegadores """
    # Usamos ThreadPoolExecutor para ejecutar pruebas en paralelo en diferentes hilos
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Creamos un iterable combinando las URLs con los navegadores, de forma que
        # una URL se ejecute en un navegador y la siguiente en otro
        tasks = [(url, browsers[i % len(browsers)], suite_functions) for i, url in enumerate(urls)]
        executor.map(lambda task: run_tests_for_url(task[0], task[1], task[2]), tasks)

