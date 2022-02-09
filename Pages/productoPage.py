from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators

class ProductoPage:
    def __init__(self, driver):
        self.driver= driver

    def clickProduct(self):
        self.driver.find_element(By.XPATH, Locators.product_selectedProduct_XPATH).click()

    def clickAddToCart(self):
        self.driver.find_element(By.XPATH, Locators.product_addToCart_XPATH).click()

    def clickAddToCartConfirmation(self):
        self.driver.find_element(By.XPATH, Locators.product_addToCartConfirmation_XPATH).click()

    def checkProductValidation(self):
        self.driver.find_element(By.XPATH, Locators.cart_productoVerificado_XPATH).text

    def eliminarProdcutoCarrito(self):
        self.driver.find_element(By.XPATH, Locators.cart_eliminarProducto_XPATH).click()

