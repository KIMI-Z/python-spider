#!/usr/bin/python3
#!/usr/bin/env python3

from data_storage import DataStorage
from html_downloader import HtmlDownloader
from html_parser import HtmlParser
from url_manager import UrlManager


class SpiderMain:

    def __init__(self):
        """
        初始化方法，主要是将其他组件实例化
        """
        self.url_manager = UrlManager()
        self.html_downloader = HtmlDownloader()
        self.html_parser = HtmlParser()
        self.data_storage = DataStorage()

    def start(self):
        """
        爬虫的主启动方法
        :return:
        """
        """ 页码 """
        title = set()
        for a in range(2, 10):
            html = self.html_downloader.download(
                'http://ggzy.foshan.gov.cn/jyxx/fss/zfcg_1108551/zbxx/index_'+str(a)+'.html?1')
            _title = self.html_parser.titleParer(html)
            for i in _title:
                title.add(i)
        for i in title:
            print(i)
            html = self.html_downloader.download(i)
            _product = self.html_parser.contextParer(html)
            self.data_storage.storage(_product)
        # self.url_manager.add_new_url(
        #     "http://ggzy.foshan.gov.cn/jyxx/fss/zfcg_1108551/zbxx/")
        # # 从url管理器里面获取url
        # url = self.url_manager.get_new_url()
        # # 将获取到的url使用下载器进行下载
        # html = self.html_downloader.download(url)
        # # 将html进行解析
        # result = self.html_parser.parser(html)
        # # 数据存储
        # self.data_storage.storage(result)


if __name__ == "__main__":
    main = SpiderMain()
    main.start()
