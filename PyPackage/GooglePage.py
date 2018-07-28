'''
Created on Jul 24, 2018

@author: SUBHODEEP
'''
import unittest
import time
#from PyPackage import HTMLTestRunner
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MyGoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_GoogleTest(self):
        chromeDriverPath = "D:/chrome_driver/chromedriver"
        os.environ["webdriver.chrome.driver"]=chromeDriverPath
        self.driver=webdriver.Chrome(chromeDriverPath)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")
        time.sleep(2)
        self.driver.close()
        #driver = self.driver
        #driver.maximize_window()
        '''driver.get('https://www.youtube.com/')
        driver.find_element_by_id('masthead-search-term').clear()
        driver.find_element_by_id('masthead-search-term').send_keys('Metallica')
        driver.find_element_by_id('search-btn').click()
 
 
 
if __name__ == '__main__':
    unittest.main()
class LoginTest(unittest.TestCase):


    def testSetup(self):
        chromeDriverPath = "D:/chrome_driver/chromedriver"
        os.environ["webdriver.chrome.driver"]=chromeDriverPath
        self.driver=webdriver.Chrome(chromeDriverPath)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get("https://www.google.com")
        time.sleep(2)
        self.driver.close()'''
       

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
