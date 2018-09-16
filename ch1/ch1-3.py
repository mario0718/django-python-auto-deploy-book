# coding=utf-8

# 演示python循环编程

a = ['Nicholas', 'Jay', 'Harlem', 'LiJian']
for item in a:
    print(item)


n = 1
sum = 0
while n < 1000:
    if n % 2 == 0:
        sum += n
    n += 1
print(sum)
    
