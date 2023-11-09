from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import random
from selenium.webdriver.firefox.options import Options

product_depth = 3

#  Set User-Agent
options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) "
                                                     "Gecko/20100101 Firefox/89.0")
driver = webdriver.Firefox(options=options)

driver.get("https://es.aliexpress.com/")  # Go to the URL

time.sleep(random.uniform(1, 3))

# Wait for the cookies acceptance button to load and click it
try:
    cookies_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn-accept")))
    cookies_button.click()
except:
    print("Cookies acceptance button not found")

time.sleep(random.uniform(1, 3))

# Wait for the pop-up close button to load and click it
try:
    popup_close_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "pop-close-btn")))
    popup_close_button.click()
except:
    print("Pop-up close button not found")

time.sleep(random.uniform(1, 3))

#  Get all the URLs from the dropdown (categories)
dropdown_urls = driver.find_elements(By.CSS_SELECTOR, "ul.Categoey--categoryList--2QES_k6 a")
for category_link in dropdown_urls:
    url1 = category_link.get_attribute('href')  # Get the URL
    driver.execute_script("window.open('');")  # Open new tab
    driver.switch_to.window(driver.window_handles[-1])  # Switch to new tab
    driver.get(url1)  # Go to the URL

    time.sleep(random.uniform(1, 3))

    #  Get all the URLs from the category (subcategories)
    category_urls = driver.find_elements(By.XPATH, '//div[@class="lv3Category--lv3CategoryBox--1Nts99Z"]/a')
    for subcategory_link in category_urls:
        url2 = subcategory_link.get_attribute('href')  # Get the URL
        driver.execute_script("window.open('');")  # Open new tab
        driver.switch_to.window(driver.window_handles[-1])  # Switch to new tab
        driver.get(url2)  # Go to the URL

        time.sleep(random.uniform(1, 3))

        #  Get all the URLs from the subcategory (products)
        product_urls = driver.find_elements(By.CLASS_NAME, 'multi--container--1UZxxHY')
        for i, product_link in enumerate(product_urls):
            if i >= product_depth:  # Check product navigation depth
                break

            url3 = product_link.get_attribute('href')  # Get the URL
            driver.execute_script("window.open('');")  # Open new tab
            driver.switch_to.window(driver.window_handles[-1])  # Switch to new tab
            driver.get(url3)  # Go to the URL

            time.sleep(random.uniform(1, 3))

            # PETTER CODE ####

            ######

            # Close the tab
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])  # Switch to previous tab
            time.sleep(random.uniform(1, 3))

        # Close the tab
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])  # Switch to previous tab
        time.sleep(random.uniform(1, 3))

    # Close the tab
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])  # Switch to previous tab
    time.sleep(random.uniform(1, 3))

# Close the browser
driver.quit()
