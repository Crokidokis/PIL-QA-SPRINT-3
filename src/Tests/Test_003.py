# IMPORTANTE: En caso de que al ejecutar el script aparezca el error "ModuleNotFoundError: No module named 'Pages'"
# Es porque el directorio no está incluido en la ruta de búsqueda de python
# Utilizar print(sys.path) para saber si está presente o no, en caso de no estarlo agregarlo con sys.path.append (al menos en mi caso se solucionó así)
import sys
sys.path.append("c:\\Users\\Gonzalo\\Desktop\\PIL-QA-SPRINT-3\\src")
from Pages.WebElements_Login import Login as login
from Pages.WebElements_Menu import Menu as menu
from Pages.WebElements_Cart import Cart as cart
import msvcrt
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import unittest
import selenium
# Templates
# Buscar un elemento por XPATH
# elemento = self.driver.find_element(By.XPATH, ' ')
# Esperar a la presencia de un elemento
# wait.until(EC.presence_of_element_located((By.XPATH, ' ')))
# Esperar a la visibilidad de un elemento
# wait.until(EC.visibility_of_element_located((By.XPATH, ' ')))
# Hacer scroll hasta un elemento específico en la página
# self.driver.execute_script("arguments[0].scrollIntoView();", elemento)


class Test_003(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Abrir Chrome
        self.action = ActionChains(self.driver)
        # Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()  # Maximizamos la ventana
        # Ingresamos a la página web
        self.driver.get("https://shop.samsung.com/ar/")
        time.sleep(5)
        self.driver.implicitly_wait(5)
        global options
        options = webdriver.ChromeOptions()
        # Se utiliza para desactivar la funcion predeterminada de chrome que se cierra sola al no detectar actividad
        options.add_argument('--disable-infobars')
        global wait
        wait = WebDriverWait(self.driver, 10)

    def testcase_03(self):

        try:
            self.driver.find_element(By.XPATH, login.btn_login_xpath).click()

            time.sleep(3)

            self.driver.find_element(By.XPATH, login.txt_email_xpath).send_keys(
                "cocarochagonzalo@gmail.com")

            time.sleep(1)

            txt_password = self.driver.find_element(By.XPATH, login.btn_password_xpath)

            txt_password.send_keys("Gonzalococa01")

            txt_password.send_keys(Keys.ENTER)

            time.sleep(5)   

            self.driver.implicitly_wait(5)

            btn_home = self.driver.find_element(By.XPATH, login.btn_home_xpath)

            btn_home.click()

            self.driver.implicitly_wait(8)

            time.sleep(5)
            
        except WebDriverException as e: #En caso de no poder logearse se notifica un except y se sigue con la ejecución del código
            print("Error al iniciar sesión")
            print(e)

        tvs_and_audio = self.driver.find_element(By.XPATH, menu.tv_and_audio_xpath)
    
        tvs_and_audio.click()

        time.sleep(5)

        self.driver.implicitly_wait(5)

        article_3 = self.driver.find_element(By.XPATH, menu.article_3_xpath)

        self.action.move_to_element(article_3).perform()

        article_3.click()

        time.sleep(5)

        btn_add_to_cart = self.driver.find_element(By.XPATH, cart.btn_add_to_cart_xpath)

        self.action.move_to_element(btn_add_to_cart).perform()

        btn_add_to_cart.click()

        time.sleep(5)

        self.driver.implicitly_wait(5)

        btn_delete = self.driver.find_element(By.XPATH, cart.btn_delete_xpath)

        btn_delete.click()

        time.sleep(3)

        self.driver.implicitly_wait(5)


    def tearDown(self):
        #msvcrt.getch()
        self.driver.close()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
