from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options
import time
import random


product_depth = 3

#  Set User-Agent
options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) "
                                                     "Gecko/20100101 Firefox/89.0")
driver = webdriver.Firefox(options=options)

driver.get("https://es.aliexpress.com/")  # Go to the URL

time.sleep(random.uniform(1, 3))  # wait random time

# Wait for the cookies acceptance button to load and click it
try:
    cookies_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "btn-accept")))
    cookies_button.click()
except:
    print("Cookies acceptance button not found")

time.sleep(random.uniform(1, 3))  # wait random time

# Wait for the pop-up close button to load and click it
try:
    popup_close_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, "pop-close-btn")))
    popup_close_button.click()
except:
    print("Pop-up close button not found")

time.sleep(random.uniform(1, 3))  # wait random time

#  Get all the anchors from the dropdown (categories)
dropdown_anchors = driver.find_elements(By.CSS_SELECTOR, "ul.Categoey--categoryList--2QES_k6 a")
for dropdown_anchor in dropdown_anchors:

    url_dropdown = dropdown_anchor.get_attribute('href')  # Get URL
    driver.execute_script("window.open('');")  # Open new tab
    driver.switch_to.window(driver.window_handles[-1])  # Switch to new tab
    driver.get(url_dropdown)  # Go to the URL
    time.sleep(random.uniform(1, 3))  # wait random time

    #  Get all the anchors from the category (subcategories)
    category_anchors = driver.find_elements(By.XPATH, '//div[@class="lv3Category--lv3CategoryBox--1Nts99Z"]/a')
    for category_anchor in category_anchors:

        url_category = category_anchor.get_attribute('href')  # Get URL
        driver.execute_script("window.open('');")  # Open new tab
        driver.switch_to.window(driver.window_handles[-1])  # Switch to new tab
        driver.get(url_category)  # Go to the URL
        time.sleep(random.uniform(1, 3))  # wait random time

        #  Get all the anchors from the subcategory (products)
        product_anchors = driver.find_elements(By.CLASS_NAME, 'multi--container--1UZxxHY')
        for i, product_anchor in enumerate(product_anchors):

            if i >= product_depth:  # Check product navigation depth
                break

            url_product = product_anchor.get_attribute('href')  # Get URL
            driver.execute_script("window.open('');")  # Open new tab
            driver.switch_to.window(driver.window_handles[-1])  # Switch to new tab
            driver.get(url_product)  # Go to the URL
            time.sleep(random.uniform(1, 3))  # wait random time

            print("Get price")
            price = driver.find_elements(By.XPATH, '//div[2]/div/div/div/div[2]/div[2]/div/div/span')
            price_string = ''
            for it_price in price:
                price_string += it_price.text
            price = driver.find_elements(By.XPATH, '//div[3]/div/div/div/div[2]/div[2]/div/div/span')
            for it_price in price:
                price_string += it_price.text

            print(price_string)
            ######
            title_string = ''
            title = driver.find_elements(By.XPATH, '//h1')
            for it_price in title:
                title_string += it_price.text
            print(title_string.split('Artículos similares')[0])

            #details
            details = driver.find_elements(By.XPATH, "//div[@id='nav-specification']/ul/li/div/div/span")
            details_diccionari = {}
            for i in range (0, len(details), 2):
                details_diccionari[details[i].text] = details[i+1].text

            print(details_diccionari)

            #entrega
            entrega = driver.find_elements(By.XPATH, "//div[@id='root']/div/div[3]/div/div[2]/div/div/div[3]/div/div[2]/div/div[2]")
            string_entrega = ''
            for i_entrega in entrega:                   
                string_entrega += i_entrega.text
            if "Entrega " in string_entrega:
                pass
            else:
                string_entrega= ''
            print(string_entrega)
            # Close the tab
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])  # Switch to previous tab
            time.sleep(random.uniform(1, 3))  # wait random time

        # Close the tab
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])  # Switch to previous tab
        time.sleep(random.uniform(1, 3))  # wait random time

    # Close the tab
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])  # Switch to previous tab
    time.sleep(random.uniform(1, 3))  # wait random time

# Close the browser
driver.quit()