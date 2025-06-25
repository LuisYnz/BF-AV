#   home_page/test_suite.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import logging
from home_page.interactions import Home_Page1 as component 
from core import execute_test_step

#   --- Definiciones de las Suites ---

import logging
from selenium import webdriver

#   --- Definiciones de las Suites ---

def vuelo_basico_suite(driver):
    suite_result = True  # Asumimos que la suite comienza con éxito
    home_page_component = component(driver)

    #try:
        #execute_test_step(
            #driver,
            #home_page_component,
            #"Test Step 001: Seleccionar idioma",
            #lambda: home_page_component.select_idioma()
        #)
    #except Exception:
        #suite_result = False
    #try:
        #execute_test_step(
            #driver,
            #home_page_component,
            #"Test Step 002: Seleccionar punto de venta",
            #lambda: home_page_component.select_pos()
        #)
    #except Exception:
        #suite_result = False

    try:
        execute_test_step(
            driver,
            home_page_component,
            "Test Step 003: Seleccionar vuelo de solo ida",
            lambda: home_page_component.vuelo_ow()
        )
    except Exception:
        suite_result = False

    try:
        execute_test_step(
            driver,
            home_page_component,
            "Test Step 004: Ingresar origen y destino",
            lambda: home_page_component.estacion("Bogota", "Cali")
        )
    except Exception:
        suite_result = False

    try:
        execute_test_step(
            driver,
            home_page_component,
            "Test Step 005: Seleccionar fechas de salida",
            lambda: home_page_component.select_fechas()
        )
    except Exception:
        suite_result = False

    try:
        execute_test_step(
            driver,
            home_page_component,
            "Test Step 006: Seleccionar número de pasajeros y buscar vuelos",
            lambda: home_page_component.passenger(1, 1, 1)
        )
    except Exception:
        suite_result = False

    if suite_result:
        logging.info("La suite de pruebas 'vuelo_basico_suite' se ejecutó con éxito.")
    else:
        logging.error("La suite de pruebas 'vuelo_basico_suite' tuvo al menos un fallo.")

def run_suite(driver):
    """ Función para ejecutar la suite de pruebas de Home Page """
    vuelo_basico_suite(driver)

#   --- Ejemplo de cómo ejecutar la suite directamente (opcional) ---
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://nuxqa4.avtest.ink/es/") 
    run_suite(driver)
    driver.quit()