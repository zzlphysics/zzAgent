from requests_html import HTMLSession

class BrowserIntegration:
    def __init__(self):
        """初始化HTMLSession"""
        self.session = HTMLSession()

    def get_rendered_page(self, url):
        """访问并渲染页面"""
        # 获取网页内容
        response = self.session.get(url)
        # 执行页面上的JavaScript，渲染页面。请根据需要调整等待时间
        response.html.render(timeout=20)
        return response.html

    def get_element_text(self, html, selector):
        """获取指定选择器的元素文本内容"""
        # 使用CSS选择器查找元素
        elements = html.find(selector)
        # 如果找到了元素，返回第一个元素的文本，否则返回空字符串
        if elements:
            return elements[0].text
        return ""

    def get_links(self, html, selector='a'):
        """获取页面上所有链接"""
        links = html.find(selector)
        return [link.attrs.get('href') for link in links if link.attrs.get('href')]

    def close(self):
        """关闭Session"""
        self.session.close()
