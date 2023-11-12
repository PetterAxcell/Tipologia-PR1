from commands.command import Commands
from extract.extract import Extract


class Navigate:
    """
    Class responsible for navigating through categories, subcategories, and products on a website using Selenium.

    Attributes:
        driver: WebDriver object for browsing the web.
        product_depth: Depth or number of products to extract.

    Methods:
        get_products(): Initiates the navigation process and returns the extracted products.
    
    Private methods:
        __init__(driver, product_depth): Constructor initializing the browser, product depth, and necessary objects.
        prerequisites(): Performs initial setup tasks like handling cookies and pop-ups.
        navigate_categories(): Navigates through different categories on the website.
        navigate_subcategories(): Navigates through subcategories under each category.
        navigate_products(): Navigates through individual products and extracts their information.
    """

    def __init__(self, driver, product_depth):
        self.product_depth = product_depth
        self.driver = driver
        self.command = Commands(self.driver)
        self.extract = Extract(self.driver)
        self.product = []
        self.id_product = 0

    def prerequisites(self):
        self.command.avoid_cookies()
        self.command.avoid_pop_up()

    def get_products(self):
        self.prerequisites()
        self.navigate_categories()
        return self.product

    def navigate_categories(self):
        category_anchors = self.command.get_categories()
        for category_anchor in category_anchors:
            self.command.goto_anchor(category_anchor)
            self.navigate_subcategories()
            self.command.close_anchor()

    def navigate_subcategories(self):
        subcategories_anchors = self.command.get_subcategories()
        for subcategory in subcategories_anchors:
            self.command.goto_anchor(subcategory)
            self.navigate_products()
            self.command.close_anchor()

    def navigate_products(self):
        products_anchors = self.command.get_products()
        count_products = 0
        while count_products < self.product_depth:
            self.command.goto_anchor(products_anchors[count_products])
            self.product.append(self.extract.get_info_product(self.id_product))
            self.command.close_anchor()
            count_products += 1
            self.id_product += 1
