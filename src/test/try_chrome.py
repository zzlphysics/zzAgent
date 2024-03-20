from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_chrome():
    try:
        # 使用 ChromeDriverManager 自动安装和提供 ChromeDriver 的路径
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Chrome 浏览器已成功启动！")
        # 可以在此处添加更多操作，如访问网页等
        # driver.get("https://www.example.com")
    except Exception as e:
        print("启动 Chrome 浏览器时出现错误：", e)
    finally:
        if driver:
            # 在最后关闭浏览器
            driver.quit()

if __name__ == "__main__":
    run_chrome()
