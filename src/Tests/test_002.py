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


class Test_002(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Abrir Chrome
        self.action = ActionChains(self.driver)
        # Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()  # Maximizamos la ventana
        # Ingresamos a la página web
        self.driver.get("https://shop.samsung.com/ar/")
        time.sleep(2)
        self.driver.implicitly_wait(5)
        global options
        options = webdriver.ChromeOptions()
        # Se utiliza para desactivar la funcion predeterminada de chrome que se cierra sola al no detectar actividad
        options.add_argument('--disable-infobars')
        global wait
        wait = WebDriverWait(self.driver, 10)

    def testcase_03(self):

        self.driver.find_element(By.XPATH, login.btn_login_xpath).click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, login.txt_email_xpath).send_keys(
            "cocarochagonzalo@gmail.com")

        time.sleep(1)

        self.driver.find_element(
            By.XPATH, login.btn_password_xpath).send_keys("Gonzalococa01")

        time.sleep(3)

        self.driver.implicitly_wait(5)
        #Se valida que el botón "Entrar" se encuentre listo para ser clickeable
        btn_enter_wait = wait.until(EC.element_to_be_clickable((By.XPATH, login.btn_enter_xpath)))

        self.driver.find_element(By.XPATH, login.btn_enter_xpath).click()

        time.sleep(5)

        self.driver.implicitly_wait(5)

        btn_home = self.driver.find_element(By.XPATH, menu.btn_home_xpath)

        btn_home.click()

        time.sleep(5)

        self.driver.implicitly_wait(5)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
