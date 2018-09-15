"""
    第 0004 题：**任一个英文的纯文本文件【第一题生成的验证码文本】，统计其中的单词出现的个数
        思路：
            1. 读取文件,获取文本内容，并保存起来
            2. 遍历所获得的文本内容，然后进行统计
                通过字典的键和值储存数据：文本为键，个数为值

"""

dic = {}

with open("test.txt") as f:
    test = f.read()
    for i in test:
        # todo 把每一个添加到字典里面，获取不到值，就设置为0，并加一；实现统计结果
        dic[i] = dic.get(i, 0) + 1

# print(dic)

for key, value in dic.items():
    if key != " " and key != "\n":
        print("%s: %s" % (key, value))

print(list(dic.items()))


