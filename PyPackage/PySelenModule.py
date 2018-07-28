'''
Created on Jul 22, 2018

@author: SUBHODEEP
'''
#print("Hello World")
'''if __name__ == '__main__':
    pass'''
    
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#chromeDriverPath = "D:/chrome_driver"
chromeDriverPath = "D:\chrome_driver"
#os.environ["webdriver.chrome.driver"]=chromeDriverPath
#os.environ["webdriver.chrome.driver"]="D:/chrome_driver"
driver = webdriver.Chrome(chromeDriverPath)
#driver.get("http://gmail.com")
user = "subho_ece@yahoo.co.in"
pwd = "Subho_ece@hnj10"
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
driver.fullscreen_window()
driver.implicitly_wait(2)

driver.close()


'''user = ""
pwd = ""
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()'''