# seatmap/test_suite.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import logging
from seatmap.interactions import seleccion_asientos as component  # Importa tu clase de interacciones
from core import execute_test_step  # Asegúrate de que la ruta sea correcta

# --- Definiciones de las Suites ---

def seleccionar_asiento_suite(driver):
    suite_result = True  # Asumimos que la suite comienza con éxito
    seleccion_asientos_component = component(driver)

    try:
        execute_test_step(
            driver,
            seleccion_asientos_component,
            "Test Step 015: Seleccionar asientos",
            lambda: seleccion_asientos_component.selected_seat()
        )
    except Exception:
        suite_result = False

    try:
        execute_test_step(
            driver,
            seleccion_asientos_component,
            "Test Step 016: Clic en botón Continuar",
            lambda: seleccion_asientos_component.continue_button()
        )
    except Exception:
        suite_result = False

    if suite_result:
        logging.info("La suite de pruebas 'seleccionar_asiento_suite' se ejecutó con éxito.")
    else:
        logging.error("La suite de pruebas 'seleccionar_asiento_suite' tuvo al menos un fallo.")

def run_suite(driver):
    """ Función para ejecutar la suite de pruebas de selección de asientos """
    seleccionar_asiento_suite(driver)

# --- Ejemplo de cómo ejecutar la suite directamente (opcional) ---
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    driver = webdriver.Chrome()  # Asegúrate de tener ChromeDriver en tu PATH
    try:
        driver.get("https://tu-pagina-de-seleccion-de-asientos.com")  # Reemplaza con la URL correcta
        # Es posible que necesites navegar a la página de selección de asientos
        # desde otra suite o directamente aquí para probar esta suite.
        run_suite(driver)
    finally:
        driver.quit()