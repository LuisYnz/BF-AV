 # services/test_suite.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import logging
from services.interactions import services as component

from core import execute_test_step # Asegúrate de que la ruta sea correcta

def services_suite(driver):

    suite_result = True
    services_component = component(driver)

    try:
        execute_test_step(
        driver,
        services_component,
        "Test Step 014: Click Continue Button",
        lambda: services_component.continue_button()
        )
    except Exception as e:
        logging.error(f"Error en Test Step 014: {e}")
        suite_result = False

    if suite_result:
        logging.info("La suite de pruebas 'services_suite' se ejecutó con éxito.")
    else:
        logging.error("La suite de pruebas 'services_suite' tuvo al menos un fallo.")
        return suite_result

def run_suite(driver):
  """
  Función para ejecutar la suite de pruebas de la página de servicios.
  """
  services_suite(driver)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("TU_URL_AQUI")

    run_suite(driver)
    driver.quit()