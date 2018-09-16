# coding=utf-8

# 演示python基本函数，计算一个数字的n字方，n默认为2


def involution(x,n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(involution(16))
print(involution(7,3))
