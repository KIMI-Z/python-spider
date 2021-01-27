import re

from html_downloader import HtmlDownloader
from product import Product

class HtmlParser:
    item_pattern = r'<li class="brick-item">[\s\S]*?</li>'
    title_pattern = r'<h3 class="title"><a href="javascript:;">([\s\S]*?)</a></h3>'
    desc_pattern = r'<p class="desc">([\s\S]*?)</p>'
    price_pattern = r'<span class="num">([\s\S]*?)</span>'

    def parser(self, html):
        """
        解析给定的html
        :param html:  html
        :return:  product set
        """
        items = re.findall(self.item_pattern, html)

        result = set()
        for i in items:
            title = re.findall(self.title_pattern, i)
            desc = re.findall(self.desc_pattern, i)
            price = re.findall(self.price_pattern, i)
            result.add(Product(title[0], desc[0], price[0]))

        return result

    def titleParer(self, html):
        """提取所有招标连接"""
        result_title = set()
        item_title = r'<li class="wb-data-list">[\s\S]*?</li>'
        href = r'<a href="([\s\S]*?)" target='
        items = re.findall(item_title, html)
        for i in items:
            hr = re.findall(href, i)
            # print(hr[0])
            item_url = hr[0]
            result_title.add(item_url)
        return result_title
    def contextParer(self, html):
        """提取所有招标标题，时间，保存正文文件"""
        href_each_item = r'<h3 class="ewb-article-tt">([\s\S]*?)</h3>'
        find_res_each = re.findall(href_each_item, html)
        print(find_res_each[0])
        """标题"""
        _title = find_res_each[0]
        time_Pare = r'<div class="ewb-article-sources">([\s\S]*?)</div>'
        _timeArr_1 = re.findall(time_Pare, html)
        time_Pare_1 = r'<span>([\s\S]*?)</span>'
        _timeArr = re.findall(time_Pare_1, _timeArr_1[0])
        # print(html)
        print(_timeArr[0])
        _time = _timeArr[0]
        return Product(_title,_time,html)
        
     
