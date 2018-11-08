# -*- coding:utf-8 -*-

import cards_tools

if __name__ == '__main__':
    cards_tools.read_student_msg()
    while True:
        cards_tools.welcome()
        number = input("请选择操作功能：")
        # print ("你选择的操作是：%s" % number)
        if number in ["1", "2", "3", "4", "5"]:
            if number == "1":
                cards_tools.add_cards()
            if number == "2":
                cards_tools.show_cards()
                # cards_tools.read_student_msg()
            if number == "3":
                cards_tools.query_card()
            if number == "4":
                cards_tools.save_msg()
                print("保存成功！")
            if number == "5":
                cards_tools.delete_from_cards()
        elif number == "0":
            break
        else:
            print("你输入的不正确，请重新选择！")
