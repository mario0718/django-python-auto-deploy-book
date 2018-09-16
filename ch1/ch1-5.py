# coding=utf-8

# 演示python可变参数(*)和关键字参数(**)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2))
print(calc())

def  person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')
