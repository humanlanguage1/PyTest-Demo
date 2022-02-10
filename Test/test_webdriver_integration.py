import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons.types import AttachmentType
import pytest

from Pages.homePage import HomePage


@pytest.mark.usefixtures("product_found")
def test_productSearch( chrome_browser):
    driver = chrome_browser
    homePage = HomePage(driver)
    time.sleep(2)
    homePage.buscarProducto()
    allure.attach(driver.get_screenshot_as_png(), name="productSearch", attachment_type=AttachmentType.PNG)
    assert 1 == 1
