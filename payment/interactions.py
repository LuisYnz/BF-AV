from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import logging

class payment:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.warnings_list = []

    def click_element(self, xpath): # Define el metodo para hacer clic en un elemento usando su XPath.
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera hasta que el elemento sea clickeable.
            element.click() #Realiza click en el elemento.
        except Exception as e: #Controla el error.
            self.capture_error(f"⚠️ Error al hacer clic en: {xpath} - {e}", f"{self.create_screenshot_path('error_click.png')}") #Captura y guarda el error con captura de pantalla en la ruta creada.

    def send_keys(self, xpath, keys): #Define un metodo para escribir texto en un input usando su XPath.
        try:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath))) #Espera que el input este presente en la página.
            element.send_keys(keys) #Ingrsa el texto en el input.
        except Exception as e: #Controla el error. 
            self.capture_error(f"⚠️ Error al enviar texto a: {xpath} - {e}", f"{self.create_screenshot_path('error_send_keys.png')}") #Captura y guarda el error con captura de pantalla en la ruta creada.

    def select_dropdown(self, xpath, value_xpath):
        self.click_element(xpath)
        self.click_element(value_xpath)

    def capture_screenshot(self, filename):
        ruta = os.path.join("screenshots", filename)
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        self.driver.save_screenshot(ruta)

    def capture_error(self, mensaje, filename):
        ruta_error = os.path.join("screenshots", filename)
        self.warnings_list.append(mensaje)
        logging.warning(mensaje)
        os.makedirs(os.path.dirname(ruta_error), exist_ok=True)
        self.driver.save_screenshot(ruta_error)

    def credit_card(self):  
        try:
            self.wait = WebDriverWait(self.driver, 30)
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
            self.click_element("//*[@id='onetrust-accept-btn-handler']")
            time.sleep(2)

            payment_iframe = self.wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class, 'payment-forms-layout_iframe')]")))
            self.driver.switch_to.frame(payment_iframe)

            self.send_keys("//*[@id='Holder']", "Luis Yanez")
            self.send_keys("//*[@id='Data']", "4111111111111111")
            self.select_dropdown("//*[@id='expirationMonth_ExpirationDate']", "//*[@id='expirationMonth_ExpirationDate-4']")
            self.select_dropdown("//*[@id='expirationYear_ExpirationDate']", "//*[@id='expirationYear_ExpirationDate-26']")
            self.send_keys("//*[@id='Cvv']", "123")
            self.capture_screenshot("credit_card.png")

            self.driver.switch_to.default_content()

            self.send_keys("//*[@id='email']", "luis@flyr.com")
            self.send_keys("//*[@id='address']", "KR 20 18 10")
            self.send_keys("//*[@id='city']", "Manizales")
            self.select_dropdown("//*[@id='country']", "//*[@id='country-0']")
            self.capture_screenshot("credit_info.png")

            self.click_element("//*[@id='terms']")
            self.click_element("/html/body/dcx-content-body/div/div/div[3]/div/div[1]/div/div[2]/dcx-component/div/div[2]/div/action-button/ds-button/button")

        except Exception as e:
            self.capture_error(
                f"⚠️ No fue posible diligenciar el formulario de pagos y realizar el pago: {e}",
                self.create_screenshot_path("error_continue_button.png")
            )
            return False #Retorna false si encuentra errores.
        return True #Retorna true si no encuentra errores.


