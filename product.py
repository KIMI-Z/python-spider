class Product:

    def __init__(self, title, time, html):
        self.title = title
        self.time = time
        self.html = html

    def __str__(self) -> str:
        return '标题：%s   时间：%s  ' % (self.title, self.time)
    
# print(Product(1,1,1,))