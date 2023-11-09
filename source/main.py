from selenium import webdriver
from settings import Opt
from commands.command import Commands

PRODUCT_DEPTH = 3
URL = "https://es.aliexpress.com/"
WEB_NAVIGATOR = "firefox"

def main():
    options = Opt()
    driver = options.get_driver(WEB_NAVIGATOR)
    driver.get(URL)
    command = Commands(driver)
    command.avoid_cookies()
    driver.quit()
if __name__ == "__main__":
    main()