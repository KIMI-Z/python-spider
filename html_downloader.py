import requests
import re


# html下载器
class HtmlDownloader:
    def download(self, url):
        """
        根据给定的url下载网页
        :param url:  url
        :return:   下载好的文本
        """
        result = requests.get(url)
        return result.content.decode("utf-8")


# test
# html_downloader = HtmlDownloader()
# for a in range(2,4):
#     html = html_downloader.download(
#         'http://ggzy.foshan.gov.cn/jyxx/fss/zfcg_1108551/zbxx/index_'+str(a)+'.html?1')
#     item_pattern = r'<li class="wb-data-list">[\s\S]*?</li>'
#     href = r'<a href="([\s\S]*?)" target='
#     href_each_item = r'<h3 class="ewb-article-tt">([\s\S]*?)</h3>'
#     items = re.findall(item_pattern, html)
#     for i in items:
#         hr = re.findall(href, i)
#         # print(hr[0])
#         item_url = hr[0]
#         html_downloader_item = HtmlDownloader()
#         item_each = html_downloader_item.download(item_url)
#         find_res_each = re.findall(href_each_item, item_each)
#         print(find_res_each[0])
#         f = open('output/'+ find_res_each[0] + '.html', 'w')
#         f.write(item_each)
#         f.close()
# f = open('test.txt', 'w')
# f.write(res)
# f.close()
