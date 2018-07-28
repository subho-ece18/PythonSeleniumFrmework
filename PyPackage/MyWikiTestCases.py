'''
Created on Jul 28, 2018

@author: SUBHODEEP
'''
__author__ = 'Subhodeep'
 
import unittest
import os
from selenium import webdriver
 
class MyWikiTestCase(unittest.TestCase):
 
    def setUp(self):
        chromeDriverPath = "D:/chrome_driver/chromedriver"
        os.environ["webdriver.chrome.driver"]=chromeDriverPath
        self.driver=webdriver.Chrome(chromeDriverPath)
        #self.driver = webdriver.Firefox()
    def test_Wiki(self):
        #driver = self.driver
        self.driver.maximize_window()
        self.driver.get('http://en.wikipedia.org')
 
        self.driver.find_element_by_id('searchInput').clear()
        self.driver.find_element_by_id('searchInput').send_keys('Sachin Tendulkar')
        self.driver.find_element_by_id('searchButton').click()
 
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main()