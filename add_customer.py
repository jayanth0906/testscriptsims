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
        elem.send_keys("sales")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("sinventory")
        elem = driver.find_element_by_xpath(" /html/body/div/form/p[3]/input")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/a")
        elem.click()
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/p[2]/a")
        elem.click()
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/a")
        elem.click()
        elem = driver.find_element_by_id("id_company")
        elem.send_keys("core drilling")
        elem = driver.find_element_by_id("id_contact_name")
        elem.send_keys("Jim")
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("4028965786")
        elem = driver.find_element_by_id("id_street_address")
        elem.send_keys("maple street")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("omaha")
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("nebraska")
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("98124")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[8]/button")
        elem.click()
        time.sleep(3)





def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
