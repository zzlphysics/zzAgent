from selenium import webdriver

def run_firefox():
    driver = None
    try:
        # 创建 Firefox 浏览器实例
        driver = webdriver.Firefox()
        print("Firefox 浏览器已成功启动！")
        # 可以在此处添加更多操作，如访问网页等
        # driver.get("https://www.example.com")
    except Exception as e:
        print("启动 Firefox 浏览器时出现错误：", e)
    finally:
        if driver:
            # 在最后关闭浏览器
            driver.quit()

if __name__ == "__main__":
    run_firefox()
