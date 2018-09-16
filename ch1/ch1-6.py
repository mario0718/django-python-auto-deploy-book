# coding=utf-8

# 演示python类的初始化，实例化

class Person:
    def __init__(self,name,location):
        self.name = name
        self.location = location

    def get_info(self):
        print("person's name is {} at {}"
              .format(self.name, self.location))

person1  = Person("Mike","London")
person2  = Person("XiaoMin","Shanghai")
person1.get_info()
person2.get_info()
