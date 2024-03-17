from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class BrowserIntegration:
    def __init__(self):
        # 使用ChromeDriverManager来自动安装和提供ChromeDriver的路径
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
    def visit_url(self, url):
        """访问指定的URL"""
        self.driver.get(url)
    def search(self, query):
        """在搜索框中输入查询并提交"""
        search_box = self.driver.find_element(By.NAME, 'q')  # 假设使用的是Google的搜索框
        search_box.send_keys(query)
        search_box.submit()
    def get_title(self):
        """获取当前页面的标题"""
        return self.driver.title
    def find_element(self, locator):
        """根据定位器查找元素"""
        return self.driver.find_element(By.CSS_SELECTOR, locator)
    def get_element_text(self, locator):
        """获取元素的文本内容"""
        element = self.find_element(locator)
        return element.text if element else None
    def close_browser(self):
        """关闭浏览器驱动"""
        self.driver.quit()