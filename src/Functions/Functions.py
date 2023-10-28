from Functions.Inicializar import Inicializar
#Importamos del archivo Inicializar, a la clase Inicializar

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import string
import pytest
import unittest
import json
from test.test_tomllib.test_data import json_path

from selenium import webdriver

class Functions(Inicializar): #Le pasamos como parámetro la clase Inicializar
    def __init__(self): #traemos los valores del json, almacenandolos en variables globales vacías para luego usarlas en las funciones
        self.json_GetFieldBy = None
        self.json_ValueToFind = None
        
    def get_json_file(self, file):
        """para abrir el archivo"""
        json_path = Inicializar.Json + "/" + file + '.json'
        #para traenos el archivo
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_file: " + json_path)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            Functions.tearDown(self)
            pytest.skip("get_json_file: No se encontro el Archivo " + file)
            #para no iniciar la prueba si el archivo no se encuentra
            
    def get_entity(self, entity): #Traemos la entity que queremos leer
            if self.json_strings is False:
                print("Define el DOM para este TC")
            else:
                try:
                    self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                    self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                    return True
                except KeyError: #Si no existe la entity, se cancela la prueba
                        self.msj = "get_entity: No se encontro la key a la cual se hace referencia: " + entity
                        Functions.tearDown(self, "fail")
                        pytest.skip(self.msj) #se      

    def tearDown(self): #Pasamos a este archivo, el tearDown de los TCs
        self.driver.quit()
