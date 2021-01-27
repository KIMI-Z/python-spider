#url管理器
class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def get_new_url(self):
        """
        获取新的url
        :return:  url
        """
        return self.new_urls.pop()

    def add_new_url(self, url):
        """
        添加新的url
        :param url:  新的url
        :return:
        """
        self.new_urls.add(url)

    def add_old_url(self, url):
        """
        添加已经爬取过的url
        :param url:  爬取过的url
        :return:
        """
        self.old_urls.add(url)
