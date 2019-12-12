import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ims_Test2(unittest.TestCase):

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
        elem.send_keys("sales")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("sinventory")
        elem = driver.find_element_by_xpath(" /html/body/div/form/p[3]/input")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/a")
        elem.click()
        elem = driver.find_element_by_xpath(" /html/body/div/div/div/div/div/p[2]/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/a[2]/div/div/div/div[1]/div")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[9]/div/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_ship_date")
        elem.send_keys("2019-12-15")
        elem = driver.find_element_by_id("id_emp_init")
        elem.send_keys("JT")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[11]/button")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/a")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_id("id_fill")
        elem.send_keys("3 Mill")
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/form/div/div[3]/div/button")
        elem.click()
        time.sleep(3)
        driver.execute_script("window.history.go(-1)")
        driver.refresh()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/a")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/div[2]/div[4]/a")
        elem.click()
        time.sleep(3)




def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
