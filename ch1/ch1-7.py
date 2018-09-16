# coding=utf-8

# 演示python类的继承

class Person:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        print("person's name is {} at {}".format(self.name, self.location))


class Student(Person):
    def __init__(self, name, location, age):
        super().__init__(name, location)
        self.age = age

    def get_information(self):
         print("student's name is {} at {}, age is {}".format(self.name, self.location, self.age))
    
student1  = Student("Mike","London", 14)
student2  = Student("XiaoMin","Shanghai", 16)
student1.get_info()
student2.get_info()
student1.get_information()
student2.get_information()
