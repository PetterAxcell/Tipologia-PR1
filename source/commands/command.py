import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Commands:
    def __init__(self, driver):
        self.driver = driver

    def avoid_cookies(self):
        time.sleep(random.uniform(1, 5)) # wait random time
        try:
            cookies_button = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn-accept")))
            cookies_button.click()
        except:
            print("Cookies acceptance button not found")
        time.sleep(random.uniform(1, 3))  

    def avoid_pop_up(self):
        # Wait for the pop-up close button to load and click it
        try:
            popup_close_button = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.CLASS_NAME, "pop-close-btn")))
            popup_close_button.click()
        except:
            print("Pop-up close button not found")

        time.sleep(random.uniform(1, 3))  # wait random time

    def get_categories(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "ul.Categoey--categoryList--2QES_k6 a")
    
    def get_subcategories(self):
        return self.driver.find_elements(By.XPATH, '//div[@class="lv3Category--lv3CategoryBox--1Nts99Z"]/a')

    def get_products(self):
        return self.driver.find_elements(By.CLASS_NAME, 'multi--container--1UZxxHY')

    def goto_anchor(self, anchor):
        url_category = anchor.get_attribute('href')  # Get URL
        self.driver.execute_script("window.open('');")  # Open new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to new tab
        self.driver.get(url_category)  # Go to the URL
        time.sleep(random.uniform(1, 3))  # wait random time

    def close_anchor(self):
        # Close the tab
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to previous tab
        time.sleep(random.uniform(1, 3))  # wait random time