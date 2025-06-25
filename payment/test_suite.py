# seatmap/test_suite.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import logging
from payment.interactions import payment as component  # Importa tu clase de interacciones
from core import execute_test_step  # Asegúrate de que la ruta sea correcta

# --- Definiciones de las Suites ---

def payment_suite(driver):
    suite_result = True
    payment_page = component(driver)  # Instancia la clase payment

    try:
        execute_test_step(
            driver,
            payment_page,
            "Test Step 017: Ingresar datos de tarjeta de crédito",
            lambda: payment_page.credit_card()  # Ejecuta la función de pago
        )
        logging.info("✅ Test Step 017: Ingreso de datos de tarjeta de crédito completado.")
    except Exception as e:
        logging.error(f"❌ Error en Test Step 017: Ingreso de datos de tarjeta de crédito: {e}")
        suite_result = False

    if suite_result:
        logging.info("La suite de pruebas 'payment_suite' se ejecutó con éxito.")
    else:
        logging.error("La suite de pruebas 'payment_suite' tuvo al menos un fallo.")

def run_suite(driver):
    """ Función para ejecutar la suite de pruebas de la página de pago """
    payment_suite(driver)

# --- Ejemplo de cómo ejecutar la suite directamente (opcional) ---
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    driver = webdriver.Chrome()
    try:
        driver.get("TU_URL_AQUI")  # Reemplaza con la URL de la página de pago
        run_suite(driver)
    finally:
        driver.quit()