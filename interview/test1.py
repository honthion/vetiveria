# <!-coding:utf-8->

# 1. 读取文件
def get_lines():
    with open("", 'rb') as f:
        for i in f:
            yield i


#  直接返回了一个类似generator 的生成器
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


def test_read_lines():
    for e in get_lines():
        print (e)


# 2.补全代码
import os


def print_directory_contents(s_path):
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print (s_child_path)


# print_directory_contents("C:\Users\user\Desktop")


import datetime


def day_of_year():
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入日期: ")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1 - date2).days + 1


# print day_of_year();

def test_filter():
    print list(filter(lambda x: x % 2 == 0, range(10)))


test_filter()
