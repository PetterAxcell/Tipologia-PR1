from commands.command import Commands

class Navigate:
    def __init__(self, driver):
        self.driver = driver
        self.command = Commands(self.driver)    
    
    def prerequisites(self):
        self.command.avoid_cookies()
        self.command.avoid_pop_up()
    
    def navigate_categories(self):
        category_anchors = self.command.get_categories()
        for category_anchor in category_anchors:
            self.command.goto_category_anchor(category_anchor)
            self.command.close_category_anchor()

    def get_products(self):
        self.prerequisites()
        products = self.navigate_categories()
        print("here")
        return products
