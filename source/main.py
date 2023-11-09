from selenium import webdriver
from settings import Opt
from commands.command import Commands
from navigation.navigate import Navigate

PRODUCT_DEPTH = 3
URL = "https://es.aliexpress.com/"
WEB_NAVIGATOR = "firefox"
FORMAT = "CSV"

def main():
    options = Opt()
    driver = options.get_driver(WEB_NAVIGATOR)
    driver.get(URL)
    
    navigate = Navigate(driver)
    products = navigate.get_products()

    driver.quit()
if __name__ == "__main__":
    main()