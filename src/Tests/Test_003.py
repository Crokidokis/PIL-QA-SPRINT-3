#IMPORTANTE: En caso de que al ejecutar el script aparezca el error "ModuleNotFoundError: No module named 'Pages'"
#Es porque el directorio no está incluido en la ruta de búsqueda de python
#Utilizar print(sys.path) para saber si está presente o no, en caso de no estarlo agregarlo con sys.path.append (al menos en mi caso se solucionó así)
import sys
sys.path.append("c:\\Users\\Gonzalo\\PIL-QA-SPRINT-3\\src")
import selenium
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import msvcrt
from Pages.WebElements_Menu import Shop as elements
#Templates
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
        self.driver = webdriver.Chrome()  #Abrir Chrome
        self.action = ActionChains(self.driver)
        self.driver.implicitly_wait(10)  #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window()  #Maximizamos la ventana
        
        #Ingresamos a la página web
        self.driver.get("https://shop.samsung.com/ar/")
        global options
        options = webdriver.ChromeOptions()
        
        options.add_argument('--disable-infobars') 

    def testcase_03(self):
        btn_login = self.driver.find_element(By.XPATH, elements.btn_login_xpath)

        btn_login.click()

        time.sleep(3)
        
        self.driver.implicitly_wait(5)
        
        txt_email = self.driver.find_element(By.XPATH, elements.txt_email_xpath)
        
        txt_email.click() 
        
        txt_email.clear()
        
        txt_email.send_keys("cocarochagonzalo@gmail.com")
        
        time.sleep(1)
        
        self.driver.implicitly_wait(5)
        
        btn_password = self.driver.find_element(By.XPATH, elements.btn_password_xpath)
        
        btn_password.click()
        
        btn_password.clear()
        
        btn_password.send_keys("Gonzalococa01")
        
        time.sleep(1)
        
        self.driver.implicitly_wait(5)
        
        btn_enter = self.driver.find_element(By.XPATH, elements.btn_enter_xpath)
        
        btn_enter.click()
        
        time.sleep(3)
        
        self.driver.implicitly_wait(5)
        
        wait = WebDriverWait(self.driver, 10)
        
        wait.until(EC.presence_of_element_located((By.XPATH, elements.profile_xpath)))
        
        time.sleep(5)
        
        self.driver.implicitly_wait(5)
        
        btn_home = self.driver.find_element(By.XPATH, elements.btn_home_xpath)
        
        btn_home.click()
        
        time.sleep(5)
        
        self.driver.implicitly_wait(5)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()