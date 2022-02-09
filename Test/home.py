import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import unittest

from webdriver_manager.chrome import ChromeDriverManager

from Pages.homePage import HomePage

class Home(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver  = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_productSearch(self):
        driver = self.driver
        driver.get("https://www.linio.com.pe/")

        homePage = HomePage(driver)
        time.sleep(2)
        homePage.buscarProducto()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()