from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BrowserIntegration:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def visit_url(self, url):
        self.driver.get(url)

    def search(self, query):
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys(query)
        search_box.submit()

    def get_title(self):
        return self.driver.title

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text if element else None

    def close_browser(self):
        self.driver.quit()
