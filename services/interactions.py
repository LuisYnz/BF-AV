from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import logging
import time

class services:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.warnings_list = []

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def capture_screenshot(self, filename):
        ruta = os.path.join("screenshots", filename)
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        self.driver.save_screenshot(ruta)
    
    def capture_error(self, mensaje, ruta_error):
        self.warnings_list.append(mensaje)
        logging.warning(mensaje)
        os.makedirs(os.path.dirname(ruta_error), exist_ok=True)
        self.save_screenshot(ruta_error)

    def continue_button(self):
        try:
            continue_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='maincontent']/div/div[6]/div/div/button-container/div/div/button")))
            
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_button)
            time.sleep(2)
            
            continue_button.click() 
            self.capture_screenshot("services_page.png")
            logging.info("✅ Continua a seat page correctamente..")
            return True
        except Exception as e: #Controla los errores del bloque try con exception.
            self.capture_error(f"⚠️ no fue posible continuar a seat page{e}", "screenshots/error_service_page.png")
            return False
