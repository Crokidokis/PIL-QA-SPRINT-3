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


class Test_001(unittest.TestCase):
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

    def testcase_01(self):

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

        btn_search = self.driver.find_element(By.XPATH, menu.btn_search_xpath)

        btn_search.click()

        time.sleep(3)

        self.driver.implicitly_wait(5)

        txt_search = self.driver.find_element(By.XPATH, menu.txt_search_xpath)

        txt_search.click()

        txt_search.clear()

        txt_search.send_keys('Monitor Gamer CRG5 24" FHD 144hz Curvo')

        txt_search.send_keys(Keys.ENTER)

        time.sleep(2)

        self.driver.implicitly_wait(5)

        article = wait.until(EC.visibility_of_element_located(
            (By.XPATH, menu.article_xpath)))

        article.click()

        time.sleep(2)
        # Validar redirección a la URL del producto 'Monitor Gamer CRG5 24" FHD 144hz Curvo'
        try:
            assert self.driver.current_url == cart.link_product1
        except WebDriverException as e:
            print("URL errónea")
            print(e)
            

        btn_purchase = self.driver.find_element(
            By.XPATH, cart.btn_purchase_xpath)

        self.action.move_to_element(btn_purchase).perform()

        btn_purchase.click()

        time.sleep(2)

        self.driver.implicitly_wait(5)

        btn_increment = self.driver.find_element(
            By.XPATH, cart.btn_increment_xpath)

        btn_increment.click()

        btn_increment.click()

        time.sleep(1)

        self.driver.implicitly_wait(5)
        # Se espera a que el precio cambie para recien darle al botón de elegir más productos
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, cart.cart_price_xpath)))

        time.sleep(3)

        btn_choose_more_products = self.driver.find_element(
            By.XPATH, cart.btn_choose_more_products_xpath)

        self.action.move_to_element(btn_choose_more_products).perform()

        btn_choose_more_products.click()

        time.sleep(5)

        self.driver.implicitly_wait(5)

        btn_search2 = self.driver.find_element(
            By.XPATH, menu.btn_search2_xpath)

        btn_search2.click()

        time.sleep(3)

        self.driver.implicitly_wait(5)

        txt_search2 = self.driver.find_element(
            By.XPATH, menu.txt_search2_xpath)

        txt_search2.click()

        txt_search2.clear()

        txt_search2.send_keys('Galaxy Z Fold5')

        time.sleep(2)

        self.driver.implicitly_wait(5)
        # Se espera a que se visualice el producto buscado en la barra de búsqueda
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, menu.article_2_xpath)))

        article_2 = self.driver.find_element(
            By.XPATH, menu.article_2_xpath).click()

        time.sleep(5)

        self.driver.implicitly_wait(5)

        btn_add_to_cart2 = self.driver.find_element(
            By.XPATH, cart.btn_add_to_cart2_xpath)

        self.action.move_to_element(btn_add_to_cart2).perform()

        btn_add_to_cart2.click()

        time.sleep(3)

        self.driver.implicitly_wait(5)

        btn_increment2 = self.driver.find_element(By.XPATH, cart.btn_increment2_xpath)

        btn_increment2.click()

        btn_increment2.click()

        time.sleep(3)

        self.driver.implicitly_wait(5)

        btn_orderform = self.driver.find_element(
            By.XPATH, cart.btn_orderform_xpath)

        self.action.move_to_element(btn_orderform).perform()

        btn_orderform.click()

        time.sleep(5)

        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
