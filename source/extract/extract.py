import urllib.request
from selenium.webdriver.common.by import By

class Extract:
    def __init__(self, driver):
        self.driver = driver

    def get_info_product(self, id_product):
        product = {"id": id_product, "price": self.get_price(), "title": self.get_title(), "details": self.get_detail(),
                   "day_delivery": self.get_day_delivery(), "image": self.get_image(id_product),
                   "original_price": self.get_original_price(), "discount": self.get_discount(),
                   "stars": self.get_stars(), "n_rating": self.get_number_rating(), 
                   "n_products_sold": self.get_sold_products()
                   }
        return product

    def get_price(self):
        price = self.driver.find_elements(By.XPATH, '//div[2]/div/div/div/div[2]/div[2]/div/div/span')
        price_string = ''
        for it_price in price:
            price_string += it_price.text
        price = self.driver.find_elements(By.XPATH, '//div[3]/div/div/div/div[2]/div[2]/div/div/span')
        for it_price in price:
            price_string += it_price.text
        return price_string

    def get_title(self):
        title_string = ''
        title = self.driver.find_elements(By.XPATH, '//h1')
        for it_price in title:
            title_string += it_price.text
        return title_string.split('Artículos similares')[0]

    def get_detail(self):
        details = self.driver.find_elements(By.XPATH, "//div[@id='nav-specification']/ul/li/div/div/span")
        details_diccionari = {}
        for i in range(0, len(details), 2):
            details_diccionari[details[i].text] = details[i + 1].text
        return details_diccionari

    def get_day_delivery(self):
        entrega = self.driver.find_elements(By.XPATH,
                                            "//div[@id='root']/div/div[3]/div/div[2]/div/div/div[3]/div/div[2]/div/div[2]")
        string_entrega = ''
        for i_entrega in entrega:
            string_entrega += i_entrega.text
        string_entrega = '' if "Entrega " not in string_entrega else string_entrega
        return string_entrega

    def get_image(self, id_product):
        try:
            imagen_elemento = self.driver.find_elements(By.XPATH, "//div[2]/div/div/div/img")
            imagen_url = imagen_elemento[0].get_attribute("src")
            urllib.request.urlretrieve(imagen_url, f"data/img/{id_product}.png")
            return True
        except Exception as e:
            print(e)
            return False

    def get_original_price(self):
        original_price = self.driver.find_elements(By.CSS_SELECTOR, ".price--originalText--Zsc6sMv")
        return original_price[0].text

    def get_discount(self):
        discount = self.driver.find_elements(By.CSS_SELECTOR, ".price--discount--xET8qnP")
        return discount[0].text

    def get_stars(self):
        stars = self.driver.find_elements(By.CSS_SELECTOR, ".reviewer--wrap--sPGWrNq > strong")
        return stars[0].text
    
    def get_number_rating(self):
        ratings = self.driver.find_elements(By.CSS_SELECTOR, ".reviewer--wrap--sPGWrNq > a")
        return ratings[0].text
    
    def get_sold_products(self):
        number = self.driver.find_elements(By.CSS_SELECTOR, ".reviewer--wrap--sPGWrNq > span:nth-child(5)")
        return number[0].text