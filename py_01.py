# !/usr/bin/python
import pymysql
"""
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，
    为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

分析：
    1.结果类似：3FSNMKHUA9GG；由12为字符组成，字符包括数字和大写字母。随机生成
        使用string模块可以直接生成A-Z和0-9 一大串字符
    2.使用random模块 和 string模块


第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
    1.数据库mydb
    2.表coupondata
    3.id自增，字段 content。

"""
# FileName: py_01.py
# Author: weitao
# Date: 2018/09/02/15:12

import random
import string

# todo 知识点回顾
print(string.ascii_uppercase)  # todo 打印出A-Z大写
print(string.ascii_lowercase)  # todo 打印a-z小写
print(string.ascii_letters)  # todo  打印a-z小写 A-Z大写

# todo 类型全部都是字符串
print(type(string.ascii_uppercase),
      type(string.ascii_letters),
      type(string.ascii_lowercase))

print(string.digits)  # todo 打印0-9
print(type(string.digits))  # todo 类型也是字符串
print(random.choice("python"))  # todo 从一个字符串中随机获取一个字符

print(string.ascii_uppercase + string.digits)  # todo 生成A-Z0-9一大串字符


# todo 案例核心内容

print("*" * 100)


# todo 把生成的随机码保存到数据库mysql中
# todo 1. 配置mysql
connect = pymysql.connect(
    user="username",
    password="password",
    host="host",
    port=3306,
    db="dbname")
# todo 2.创建游标
cursor = connect.cursor()


def random_str(number):
    """
        生成随机码
    :param number: 指定要生成多少位数
    :return: 随机码
    """
    result = ""  # todo 用一个变量保存生成的随机码
    for i in range(number):
        result += random.choice(string.ascii_uppercase + string.digits)
    return result


def two_hundred_code():
    """
        生成200个随机码
    :return: 200个随机码
    """
    total_num = 200  # todo 总共生成200个随机码
    number = 12  # todo 每一个随机码多少字符
    data = ""  # todo 保存最终的所有值
    for i in range(total_num):

        code = random_str(number)
        print("number: {}, result: {}".format(i+1, code))
        data += "number:{}, result: {} \n".format(i+1, code)

        # todo 3. 插入数据到数据库中
        cursor.execute("insert into coupondata(content) values('%s')" % code)
        connect.commit()  # todo 切记要提交
        # data += random_str(number)

    return data
# two_hundred_code()  # todo 调用函数


# todo 把生成的随机码保存到文件 coupondata.txt 中
# print(two_hundred_code())  # todo 打印结果
# two_hundred_code()
with open("coupondata.txt", 'w') as f:
    f.write(two_hundred_code())


cursor.close()
connect.close()
