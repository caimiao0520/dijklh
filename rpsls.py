#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����


def name_to_number(name):# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    if name == "ʯͷ":
        number = 0
    elif name == "ʷ����":
        number = 1
    elif name == "ֽ":
        number = 2
    elif name == "����":
        number = 3
    else:
        number = 4
    return number

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������


def number_to_name(number):# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    if number == 0:
        name = "ʯͷ"
    elif number == 1:
        name = "ʷ����"
    elif number == 2:
        name = "ֽ"
    elif number == 3:
        name = "����"
    else:
        name = "����"
    return name


import random


def rpsls(player_choice):
    print("����ѡ����",player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    com_choice=number_to_name(comp_number)
    print("�������ѡ��Ϊ:%s" % com_choice)
    difference = (player_number-comp_number) % 5# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    if difference == 1 or difference == 2:
        print("��Ӯ��")
    elif difference == 3 or difference == 4:
        print("�����Ӯ��")
    else:
        print("���ͼ��������һ����")


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("��Ϸ����Ϊ�������ܼ�ֽ�����棻ֽ���԰�סʯͷ������Spock��ʯͷ��������ͼ�����������Զ���Spock����ֽ��Spock�������������ʹʯͷ����")
print("----------------")
print("����������ѡ��:")
choice=input()
rpsls(choice)


