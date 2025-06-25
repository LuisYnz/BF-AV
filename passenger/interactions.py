from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
import logging
import os

class passengers_list:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.warnings_list = []

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que el elemento sea interactivo antes de dar click.
        element.click() #Pulsa click en el elemento.

    def send_keys(self, xpath, keys):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath))) #Localiza el input y espera que sea visible.
        element.send_keys(keys) #Ingresa la informacion en el input.

    def select_dropdown(self, xpath, value_xpath):
        self.click_element(xpath) #Abre el dropdown
        self.click_element(value_xpath) #Selecciona la opcion del dropdown

    def capture_screenshot(self, filename): #Declara la función con los metodos a utilizar.
        ruta = os.path.join("screenshots", filename) #Crea la ruta del screenshot.
        os.makedirs(os.path.dirname(ruta), exist_ok=True) #Crea los directorios en caso de no existir.
        self.driver.save_screenshot(ruta) #Realiza la captura de pantalla en la ruta creada

    def capture_error(self, mensaje, ruta_error): #Declara la función con los metodos a utilizar.
        self.warnings_list.append(mensaje) #Agrega el mensaje de advertencia a la warning list.
        logging.warning(mensaje) #Agrega el mensaje de advertencia en los logz.
        os.makedirs(os.path.dirname(ruta_error), exist_ok=True) #Crea los directorios en caso de no existir.
        self.driver.save_screenshot(ruta_error) #Realiza la captura de pantalla en la ruta creada.    

    def passenger_adt(self): #Diligenciar form de pasajeros
        try:
            self.wait = WebDriverWait(self.driver, 30)
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
            self.select_dropdown("//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433323244343535383534']", "//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433323244343535383534-0']")
            self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[1]/div/div[2]/ibe-input/div/div/input", "Charizard")
            self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[2]/ibe-input/div/div/input", "Tetsa")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_-0']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/button", "//*[@id='dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_-2']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/button", "//*[@id='dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433323244343535383534_-2']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[1]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/button", "//*[@id='IdDocNationality_7E7E303030312D30312D30317E353334423438324433323244343535383534-1']")

            self.capture_screenshot("form_adt.png")
            logging.info("✅ Formulario de pasajero adulto diligenciado correctamente.")
            return True
        except Exception as e: #Controla los errores del bloque try con exception.
            self.capture_error(f"⚠️ no fue posible diligenciar form adt {e}", "screenshots/error_form_adt.png")
            return False

    def passenger_inf(self):   
        try: #Diligenciar form del pasajero INF.
            form_inf = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form_inf)

            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[1]/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433313244343535383534-1']")
            self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[1]/div/div[2]/ibe-input/div/div/input", "Tester")
            self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[2]/ibe-input/div/div/input", "Goku")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_-0']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/button", "//*[@id='dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_-0']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/button", "//*[@id='dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433313244343535383534_-0']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[2]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/button", "//*[@id='IdDocNationality_7E7E303030312D30312D30317E353334423438324433313244343535383534-1']")

            self.capture_screenshot("form_inf.png")
            logging.info("✅ Formulario de pasajero infante diligenciado correctamente.")
            return True
        except Exception as e:
            self.capture_error(f"⚠️ no fue posible diligenciar form infante {e}", "screenshots/error_form_inf.png")
            return False

    def passenger_youth(self):
        try: #Diligenciar form del pasajero joven.
            form_youth = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form")                                                 
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form_youth)

            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[1]/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433333244343535383534-0']")
            self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[1]/div/div[2]/ibe-input/div/div/input", "Vegueta")
            self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[2]/ibe-input/div/div/input", "Turs")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_-1']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/button", "//*[@id='dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_-2']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/button", "//*[@id='dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433333244343535383534_-1']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[3]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/button", "//*[@id='IdDocNationality_7E7E303030312D30312D30317E353334423438324433333244343535383534-1']")   

            self.capture_screenshot("form_yout.png")
            logging.info("✅ Formulario de pasajero joven diligenciado correctamente.")
            return True
        except Exception as e:
            self.capture_error(f"⚠️ no fue posible diligenciar form youth {e}", "screenshots/error_form_youth.png")
            return False

    def chd(self): #Diligenciar form del pasajero joven.
        try:
            form_chd = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form")                                                 
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form_chd)

            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[1]/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='IdPaxGender_7E7E303030312D30312D30317E353334423438324433343244343535383534-0']")
            self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[1]/div/div[2]/ibe-input/div/div/input", "Pedro")
            self.send_keys("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[2]/ibe-input/div/div/input", "Peresa")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[1]/ibe-select-custom/div/div[2]/button", "//*[@id='dateDayId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_-1']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[2]/ibe-select-custom/div/div[2]/button", "//*[@id='dateMonthId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_-0']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[3]/input-date-picker-custom/ibe-select-date-picker-custom/div/div/fieldset/div/div[3]/ibe-select-custom/div/div[2]/button", "//*[@id='dateYearId_IdDateOfBirthHidden_7E7E303030312D30312D30317E353334423438324433343244343535383534_-1']")
            self.select_dropdown("/html/body/div[1]/main/div/div[3]/div/div/passenger-details-container/personal-data-custom/div/div/div[4]/personal-data-form-custom/div/form/div/div[4]/ibe-select-custom/div/div[2]/button", "//*[@id='IdDocNationality_7E7E303030312D30312D30317E353334423438324433343244343535383534-1']")     

            self.capture_screenshot("form_chd.png")
            logging.info("✅ Formulario de pasajero niño diligenciado correctamente.")
            return True
        except Exception as e:
            self.capture_error(f"⚠️ no fue posible diligenciar form niño {e}", "screenshots/error_form_chd.png")
            return False

    def contact(self): #Diligencia la informacion de contact details
        try:
            form_contact = self.driver.find_element(By.XPATH, "//*[@id='maincontent']/div/div[3]/div/div/contact-container/booking-contact-custom")                                                 
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", form_contact)
            self.select_dropdown("//*[@id='phone_prefixPhoneId']", "//*[@id='phone_prefixPhoneId-1']")
            self.send_keys("//*[@id='phone_phoneNumberId']", "3231536789")
            self.send_keys("//*[@id='email']", "luis.yanez@flyr.com")

            self.capture_screenshot("form_contact.png")
            logging.info("✅ Formulario de contacto diligenciado correctamente.")
        except Exception as e:
            self.capture_error(f"⚠️ no fue posible diligenciar form contact {e}", "screenshots/error_form_contact.png")
            return False
        
        try:
            confirm_email_element = self.driver.find_element(By.XPATH, "//*[@id='confirmEmail']")
            confirm_email_element.send_keys("luis.yanez@flyr.com")
            print("Campo 'Confirmar Email' encontrado y diligenciado.")
            self.capture_screenshot("form_contact2.png")
        except NoSuchElementException:
            print("Campo 'Confirmar Email' no está presente. Continuando con el siguiente paso.")
     
    def continue_bton(self): #Localiza el boton continuar y sigue a la siguiente pagina.
        self.click_element("//*[@id='maincontent']/div/div[3]/div/div/contact-container/booking-contact-custom/form/div[2]/ibe-checkbox")
        time.sleep(2)
        self.click_element("//*[@id='maincontent']/div/div[3]/div/div/button-container/div/div/button")

        try:  
            self.wait = WebDriverWait(self.driver, 30)
            ok_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ngb-modal-window/div/div/div/div[3]/button")))
            ok_btn.click()
            logging.info("✅ Botón OK localizado y pulsado")
        
        #Volver a hacer clic en el botón continuar después de cerrar el modal
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='maincontent']/div/div[3]/div/div/button-container/div/div/button"))).click()
        except TimeoutException:
            logging.info("✅ No se encontró el botón OK, continuando con el siguiente paso.")
            return False