# 数据存储器
class DataStorage:
    def storage(self, products):
        """
        数据存储  
        """
        try:
          print(products)
          f = open('output/' + products.title.strip() +
                 "-时间-" + products.time + '.html', 'w')
          f.write(products.html)
          f.close()
        except IOError:
            print("write file error:" + products.time)
        else:
            pass
