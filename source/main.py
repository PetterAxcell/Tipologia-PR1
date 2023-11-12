from settings import Opt
from save.save import Save
from navigation.navigate import Navigate

PRODUCT_DEPTH = 10
URL = "https://es.aliexpress.com/"
WEB_NAVIGATOR = "firefox"
FORMAT = "CSV"


def main():
    options = Opt()
    driver = options.get_driver(WEB_NAVIGATOR)
    driver.get(URL)

    navigate = Navigate(driver, PRODUCT_DEPTH)
    products = navigate.get_products()

    save_data = Save(products)
    if FORMAT == "CSV":
        save_data.save_csv()
    if FORMAT == "JSON":
        save_data.save_json()

    driver.quit()


if __name__ == "__main__":
    main()
