# -*- coding:utf-8 -*-

cards_msg = []  # 用来存储所有学生的信息


def welcome():
    """
         欢迎界面
    :return:
    """
    print(("*" * 50))
    print("    【名片管理系统】 V1.0")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    # print("4. 保存名片")
    print("5. 删除名片\n")
    print("0. 退出系统")
    print(("*" * 50))


def add_cards():
    """
        添加学生名片
    :return:
    """
    cards_dic = {}  # 用来存储每一个学生的具体信息
    name = input("请输入你的名字：")
    age = input("请输入你的年龄：")
    while not age.isdigit():  # 判断年龄的输入是否是数字，
        age = input("年龄输入有误，请重新输入：")
    qq = input("请输入你的QQ：")
    while not qq.isdigit():  # 判断QQ的输入是否是数字，
        qq = input("QQ输入有误，请重新输入：")
    address = input("请输入你的住址：")

    cards_dic["name"] = name
    cards_dic["age"] = age
    cards_dic["qq"] = qq
    cards_dic["address"] = address

    if cards_dic in cards_msg:
        print('该用户已存在，添加失败')
    else:
        cards_msg.append(cards_dic)
        print("添加名片成功！")


def show_cards():
    """
        显示所有学生的信息
    :return:
    """
    global cards_msg
    if cards_msg:
        for cards in cards_msg:
            print(("姓名：{}, 年龄：{}, QQ：{}, 住址：{}".format(cards["name"], cards["age"], cards["qq"], cards["address"])))
        else:
            print("查询成功！")
    else:
        print("当前没有任何学生的信息")


def query_card():
    """
        查询每一个学生的信息
    :return:
    """
    if bool(cards_msg):  # 在查找之前，先判断列表是否为空，为空就提示为空，不用查了。不为空再需要查询
        find_name = input("请输入要查找学生的名字：")
        for name in cards_msg:
            if name["name"] == find_name:
                """这里有个问题，就是当列表中有多个相同姓名的学生时候，只找到第一个就退出了。。。
                    但是，如果把break去掉，就会找到遍历列表中所有的字典元素，找到一个就对其操作，，，
                    如果某个学生对应的名字对应的姓名不是想要的，就又会提示找不到此人。。。。。

                    待修改！！！！

                    理想状态：一次性显示所有学生，然后再选择要对具体哪一个学生进行操作。。。。
                """
                # print("姓名 \t\t 年龄 \t\t QQ \t\t 住址")
                # print(("%s \t\t %s \t\t %s \t\t %s" % (name["name"], name["age"], name["qq"], name["address"])))
                print(("姓名：{}, 年龄：{}, QQ：{}, 住址：{}".format(name["name"], name["age"], name["qq"], name["address"])))
                change_card(name)
                break

        else:
            print("查无此人。。。。。。")
    else:
        print("当前列表为空！！！")


def change_card(name):
    """
        当查找到某一个学生的时候，可以对其进行操作，删除或者是修改信息
    :return:
    """
    select_operation = input("请选择是否对该学生进行修改：1.删除/ 2.修改信息/ 3.返回上一级")
    if select_operation in ["1", "2", "3"]:
        if select_operation == "1":
            """删除操作"""
            delete_name(name)
        if select_operation == "2":
            change_msg(name)
        if select_operation == "3":
            return
    else:
        print("操作有误，请重新选择！")
        change_card(name)


def delete_name(name):
    """
        当学生选择修改的时候，删除学生信息
    """
    commit = input("你确定要删除该学生的信息吗？(y/n)   ")
    if commit == "y" or commit == "Y":
        """让用户确定是否真的要删除该信息！防止手误！！！"""
        print(("名字为 %s 的学生的信息已从列表中删除！！！" % name["name"]))
        # name.clear()  # 删除字典中对应的数据，但是空字典还在列表当中，所以
        # cards_msg.remove(name)  # 还需要把字典从列表中删除，这样子在查询时候才不会报错

        """当找到这个字典的时候，可以直接使用列表的remove()方法，直接将这个字典从列表中删除。方面快捷"""
        cards_msg.remove(name)

        # print cards_msg  # 为了验证操作后，列表，字典中的数据
        # print name
    elif commit == "n" or commit == "N":
        return
    else:
        print("输入有误，请重新对学生进行操作！！！")
        change_card(name)


def change_msg(name):
    """当学生选择修改的时候，可以对其中的每一个信息进行修改"""
    change_select = input("请选择要修改的信息：1.姓名/ 2.年龄/ 3.QQ/ 4.地址 ")
    if change_select == "1":
        new_msg = input("请输入修改后的姓名：")
        name["name"] = new_msg
        print("姓名修改完成！")
        return

    elif change_select == "2":
        new_msg = input("请输入修改后的年龄：")
        while not new_msg.isdigit():  # 判断年龄的输入是否是数字，
            new_msg = input("年龄输入有误，请重新输入：")
        name["age"] = new_msg
        print("年龄修改完成！")
        return

    elif change_select == "3":
        new_msg = input("请输入修改后的QQ：")
        while not new_msg.isdigit():  # 判断年龄的输入是否是数字，
            new_msg = input("年龄输入有误，请重新输入：")
        name["qq"] = new_msg
        print("QQ号修改完成！")
        return

    elif change_select == "4":
        new_msg = input("请输入修改后的住址：")
        name["address"] = new_msg
        print("地址修改完成！")
        return
    else:
        print("输入有误，请重新选择！！！")
        change_card(name)


def delete_from_cards():
    """
        这是一个在主界面删除学生信息的方法
    """
    global cards_msg
    if bool(cards_msg):  # 在查找之前，先判断列表是否为空，为空就提示为空，不用查了。不为空才需要查询
        find_name = input("请输入要删除学生的名字：")
        for name in cards_msg:
            if name["name"] == find_name:
                # print("姓名 \t\t 年龄 \t\t QQ \t\t 住址")
                # print(("%s \t\t %s \t\t %s \t\t %s" % (name["name"], name["age"], name["qq"], name["address"])))
                print(("姓名：{}, 年龄：{}, QQ：{}, 住址：{}".format(name["name"], name["age"], name["qq"], name["address"])))

                delete_name(name)
                break
        else:
            print("查无此人。。。。。。")
            pass
    else:
        print("当前列表为空！！！")

    pass


def save_msg():
    """
        保存学生信息，写到一个文件里面
    """
    with open("student.data", 'w+') as f:
        for msg in cards_msg:
            f.write(str(msg) + "\n")


def read_student_msg():
    """
        一开始先把之前保存的数据加载到列表中
    """
    import json
    global cards_msg
    try:
        with open("student.data") as msg:
            content = msg.read().split("\n")[:-1]
            for item in content:
                cards_msg.append(json.loads(item.replace("'", '"')))
    except IOError:
        pass
    else:
        pass
    finally:
        pass
