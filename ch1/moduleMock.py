# 测试Python mock

class AddSum():

    # 函数没实现
    def sum(self):
        pass

class Computer:
    def __init__(self):
        self.__price = 5000
        
    def get_name(self, brand):
        return brand
        
    def get_price(self):
        return self.__price
