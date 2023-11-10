from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class Opt:
    """
    A class to manage browser options and retrieve Selenium web drivers.

    Methods:
        __init__(): Initializes browser options for the web drivers.
        get_driver(type_client="firefox"): Retrieves a Selenium web driver based on the specified browser type.
    """
    def __init__(self):
        self.options = Options()

    def get_driver(self, type_client="firefox"):
        self.options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) "
                                                                  "Gecko/20100101 Firefox/89.0")
        if type_client == "firefox":
            return webdriver.Firefox(options=self.options)
        elif type_client == "chrome":
            return webdriver.Chrome(options=self.options)
