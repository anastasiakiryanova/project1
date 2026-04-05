from selenium.webdriver.common.by import By
class ProductPage:
    def __init__(self, driver):
        self.driver = driver
    def check_title_is(self, title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        assert page_title.text == title
    def click_monitor(self):
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, "[onclick=\"byCat('monitor')\"]")
        monitor_link.click()
    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, ".card")
        assert len(monitors) == count