import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ims_Test9(unittest.TestCase):

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
        elem.send_keys("warehouse")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("winventory")
        elem = driver.find_element_by_xpath(" /html/body/div/form/p[3]/input")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath(" /html/body/div[2]/div/div[3]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/p[3]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/p[2]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/a[1]/div/div/div/div[1]/div/p")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[8]/div[4]/a")
        elem.click()
        time.sleep(5)
        driver.get("https://maverickims.herokuapp.com/warehouse/orders/")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/p[1]/a")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_order_number")
        elem.send_keys("3")
        elem.send_keys(Keys.ENTER)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div/button")
        elem.click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/p[2]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/a[1]/div/div/div/div[1]/div/p")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[8]/div[4]/a")
        elem.click()
        time.sleep(5)




def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
