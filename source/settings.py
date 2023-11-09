from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
class Opt():
    def __init__(self) :
        self.options = Options()

    def get_driver(self,type_client = "firefox"):
        self.options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) "
                                        "Gecko/20100101 Firefox/89.0")
        if type_client == "firefox":
            return webdriver.Firefox(options = self.options)
        elif type_client == "chrome":
            return webdriver.Chrome(options = self.options)