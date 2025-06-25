#   home_page/test_suite.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import logging
from select_flight.interactions import select_flight1 as Component
from core import execute_test_step

#   --- Definiciones de las Suites ---

def select_flight_suite(driver):
    suite_result = True
    select_flight_component = Component(driver)

    try:
        execute_test_step(
            driver,
            select_flight_component,
            "Test Step 007: Seleccionar vuelo",
            lambda: select_flight_component.select_flight()
        )
    except Exception as e:
        logging.error(f"Error en Test Step 007: {e}")
        suite_result = False

    if suite_result:
        logging.info("La suite de pruebas 'select_flight_suite' se ejecutó con éxito.")
    else:
        logging.error("La suite de pruebas 'select_flight_suite' tuvo al menos un fallo.")

def run_suite(driver):
    """ Función para ejecutar la suite de pruebas de Select Flight """
    select_flight_suite(driver)

#   --- Ejemplo de cómo ejecutar la suite directamente (opcional) ---
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://nuxqa4.avtest.ink/es/")  # Reemplaza con tu URL base
    run_suite(driver)
    driver.quit()