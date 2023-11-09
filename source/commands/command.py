from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class CommandBot:
    def clickButton(type, element):
        if type == 'xpath':
            element = driver.find_element(By.XPATH, element)