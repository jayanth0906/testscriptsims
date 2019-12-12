import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ims_Test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://maverickims.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@ id = "navbarSupportedContent"] / ul[2] / li / a')
        elem.click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("swarehouse")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("sinventory")
        elem = driver.find_element_by_xpath(" /html/body/div/form/p[3]/input")
        elem.click()
        time.sleep(10)

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
