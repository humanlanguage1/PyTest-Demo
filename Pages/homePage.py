from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators

class HomePage:
    def __init__(self, driver):
        self.driver= driver

    def buscarProducto(self):
        self.driver.find_element(By.XPATH, Locators.homePage_SearchBar_XPATH).send_keys('iphone')
        self.driver.find_element(By.XPATH, Locators.homePage_searchButton_XPATH).click()

    def verCarrito(self):
        self.driver.find_element(By.XPATH, Locators.homePage_Cart_XPATH).click()

    def eliminarProducto(self):
        self.driver.find_element(By.XPATH, Locators.cart_eliminarProducto_XPATH).click()


