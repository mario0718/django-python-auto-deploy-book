# coding=utf-8

# 演示python类的多进程
from concurrent.futures import ProcessPoolExecutor

URLS = ['http://www.163.com',
        'https://www.baidu.com/',
        'https://github.com/',
        'http://www.sohu.com',]
def load_url(url):
    print('{} page is show.'.format(url))

executor = ProcessPoolExecutor(max_workers=3)

if __name__ == '__main__':

    for url in URLS:
        future = executor.submit(load_url,url)
    print('主线程')
