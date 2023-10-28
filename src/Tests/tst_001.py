from Functions.Functions import Functions as Selenium #Importamos la función Functions y le ponemos el alias Selenium
from Pages.Samsung_carrito import Carrito as Samsung
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

options = webdriver.ChromeOptions()
#Templates
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
        self.driver = webdriver.Chrome()  #Abrir Chrome
        self.driver.implicitly_wait(10)  #Esperamos 10 segundos para continuar (para que se cargue por completo)
        self.driver.maximize_window()  #Maximizamos la ventana
        
        #Ingresamos a la página web
        self.driver.get("https://shop.samsung.com/ar/")
        
        options.add_argument('--disable-infobars')
        

    def test_product_page(self):
        btn_login = self.driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/div/div/div[2]/ul[2]/li[1]/a')

        btn_login.click()

        time.sleep(3)
        
        self.driver.implicitly_wait(5)
        
        txt_email = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div/form/div[1]/label/div/input')
        
        txt_email.click() 
        
        txt_email.clear()
        
        txt_email.send_keys("cocarochagonzalo@gmail.com")
        
        time.sleep(1)
        
        self.driver.implicitly_wait(5)
        
        btn_password = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input')
        
        btn_password.click()
        
        btn_password.clear()
        
        btn_password.send_keys("Gonzalococa01")
        
        time.sleep(1)
        
        self.driver.implicitly_wait(5)
        
        btn_enter = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div/form/div[4]/div/button')
        
        btn_enter.click()
        
        time.sleep(3)
        
        self.driver.implicitly_wait(5)
        
        wait = WebDriverWait(self.driver, 10)
        
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/section/header/div[2]/div/div/div[1]')))
        
        time.sleep(5)
        
        self.driver.implicitly_wait(5)
        
        btn_home = self.driver.find_element(By.XPATH, '//*[@id="headerSamsung"]/div[2]/div/div/a')
        
        btn_home.click()
        
        time.sleep(5)
        
        self.driver.implicitly_wait(5)
        
        btn_search = self.driver.find_element(By.XPATH, '//*[@id="search-bold"]') 
        
        btn_search.click()
        
        time.sleep(3)
        
        self.driver.implicitly_wait(5)
        
        txt_search = self.driver.find_element(By.XPATH, '//*[@id="downshift-0-input"]')
        
        txt_search.click()  
        
        txt_search.clear()
        
        txt_search.send_keys('55" Crystal UHD 4K CU7000')
        
        time.sleep(2)
        
        self.driver.implicitly_wait(5)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="hyper-modal-wrapper_component_id"]/div[2]/div[1]/div[1]/div/div/div[3]/section/section/ul/li[1]/div/a/article')))
        
        time.sleep(3)
        
        article = self.driver.find_element(By.XPATH, '//*[@id="hyper-modal-wrapper_component_id"]/div[2]/div[1]/div[1]/div/div/div[3]/section/section/ul/li[1]/div/a/article') 
        
        article.click()
        
        time.sleep(2)
        
        self.driver.implicitly_wait(5)
        
        btn_purchase = self.driver.find_element(By.XPATH, '//*[@id="product-button-add-to-cart"]/button/div')
        
        btn_purchase.click()
        
        time.sleep(2)
        
        self.driver.implicitly_wait(5)
    
        btn_increment = self.driver.find_element(By.XPATH, '//*[@id="item-quantity-change-increment-137629"]') 
        
        btn_increment.click()
        
        btn_increment.click()
        
        time.sleep(1)
        
        self.driver.implicitly_wait(5)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkoutMainContainer"]/div[5]/div[3]/div[1]/div[2]/div/div[4]/div[2]/div/div[2]/div/table/tfoot/tr/td[3]')))

        time.sleep(3)
        
        btn_choose_more_products = self.driver.find_element(By.XPATH, '//*[@id="cart-choose-more-products"]')  
        
        btn_choose_more_products.click()
        
        time.sleep(5)
         
        self.driver.implicitly_wait(5)
        
        btn_search2 = self.driver.find_element(By.XPATH, '//*[@id="search-bold"]') 
        
        btn_search2.click()
        
        time.sleep(3)
        
        self.driver.implicitly_wait(5)
        
        txt_search2 = self.driver.find_element(By.XPATH, '//*[@id="downshift-0-input"]') 
        
        txt_search2.click()  
        
        txt_search2.clear()
        
        txt_search2.send_keys('Galaxy Z Fold5')
        
        time.sleep(2)
        
        self.driver.implicitly_wait(5)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="hyper-modal-wrapper_component_id"]/div[2]/div[1]/div[1]/div/div/div[3]/section/section/ul/li/div/a/article/div[2]/div[1]/span')))
        
        time.sleep(3)
        
        article_2 = self.driver.find_element(By.XPATH, '//*[@id="hyper-modal-wrapper_component_id"]/div[2]/div[1]/div[1]/div/div/div[3]/section/section/ul/li/div/a/article/div[2]/div[1]/span') 
        
        article_2.click()
        
        time.sleep(5)
        
        self.driver.implicitly_wait(5)
        
        btn_add_to_cart2 = self.driver.find_element(By.XPATH, '//*[@id="product-button-add-to-cart"]/button/div') 
        
        btn_add_to_cart2.click()
        
        time.sleep(3)
        
        self.driver.implicitly_wait(5)
        
        btn_increment2 = self.driver.find_element(By.XPATH, '//*[@id="item-quantity-change-increment-137415"]')
        
        btn_increment2.click()
        
        btn_increment2.click()
        
        time.sleep(1)
        
        self.driver.implicitly_wait(5)
        
        btn_orderform = self.driver.find_element(By.XPATH, '//*[@id="cart-to-orderform"]') 
        
        btn_orderform.click()
        
        time.sleep(5)
        
        self.driver.implicitly_wait(5)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()