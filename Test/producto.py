import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import unittest

from webdriver_manager.chrome import ChromeDriverManager

from Pages.homePage import HomePage
from Pages.productoPage import ProductoPage

class Producto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver  = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_agregarCarrito(self):
        driver = self.driver
        driver.get("https://www.linio.com.pe/")

        homePage = HomePage(driver)
        productoPage = ProductoPage(driver)

        homePage.buscarProducto()
        productoPage.clickProduct()
        productoPage.clickAddToCart()
        productoPage.clickAddToCartConfirmation()

    def test_validarProducto(self):
        driver = self.driver
        driver.get("https://www.linio.com.pe/")

        homePage = HomePage(driver)
        productoPage = ProductoPage(driver)

        homePage.buscarProducto()
        productoPage.clickProduct()
        productoPage.clickAddToCart()
        productoPage.clickAddToCartConfirmation()
        assert productoPage.checkProductValidation().strip().lower() == ('IPhone 12 64GB -Negro-').strip().lower()

    def test_eliminarProductoCarrito(self):
        driver = self.driver
        driver.get("https://www.linio.com.pe/")

        homePage = HomePage(driver)
        productoPage = ProductoPage(driver)

        homePage.buscarProducto()
        productoPage.clickProduct()
        productoPage.clickAddToCart()
        productoPage.clickAddToCartConfirmation()
        productoPage.eliminarProdcutoCarrito()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


