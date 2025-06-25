from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import logging
from passenger.interactions import passengers_list as component
from core import execute_test_step

def formulario_pasajeros_suite(driver):
    suite_result = True
    passengers_page_component = component(driver)

    try:
        execute_test_step(
            driver,
            passengers_page_component,
            "Test Step 008: Diligenciar formulario de pasajero adulto",
            lambda: passengers_page_component.passenger_adt()
        )
    except Exception as e:
        logging.error(f"Error en Test Step 008: {e}")
        suite_result = False

    try:
        execute_test_step(
            driver,
            passengers_page_component,
            "Test Step 009: Diligenciar formulario de pasajero infante",
            lambda: passengers_page_component.passenger_inf()
        )
    except Exception as e:
        logging.error(f"Error en Test Step 009: {e}")
        suite_result = False

    try:
        execute_test_step(
            driver,
            passengers_page_component,
            "Test Step 010: Diligenciar formulario de pasajero joven",
            lambda: passengers_page_component.passenger_youth()
        )
    except Exception as e:
        logging.error(f"Error en Test Step 010: {e}")
        suite_result = False

    try:
        execute_test_step(
            driver,
            passengers_page_component,
            "Test Step 011: Diligenciar formulario de pasajero niño",
            lambda: passengers_page_component.chd()
        )
    except Exception as e:
        logging.error(f"Error en Test Step 011: {e}")
        suite_result = False

    try:
        execute_test_step(
            driver,
            passengers_page_component,
            "Test Step 012: Diligenciar información de contacto",
            lambda: passengers_page_component.contact()
        )
    except Exception as e:
        logging.error(f"Error en Test Step 012: {e}")
        suite_result = False

    try:
        execute_test_step(
            driver,
            passengers_page_component,
            "Test Step 013: Hacer clic en el botón Continuar",
            lambda: passengers_page_component.continue_bton()
        )
    except Exception as e:
        logging.error(f"Error en Test Step 013: {e}")
        suite_result = False

    if suite_result:
        logging.info("La suite de pruebas 'formulario_pasajeros_suite' se ejecutó con éxito.")
    else:
        logging.error("La suite de pruebas 'formulario_pasajeros_suite' tuvo al menos un fallo.")

def run_suite(driver):
    """ Función para ejecutar la suite de pruebas de la página de pasajeros """
    formulario_pasajeros_suite(driver)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("TU_URL_AQUI")  # Reemplaza con la URL donde se encuentra el formulario de pasajeros
    run_suite(driver)
    driver.quit()
