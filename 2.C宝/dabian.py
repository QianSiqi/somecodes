import sys
import time
import jieba
import logging
import add
print('要添加功能在add.py里添加！')
jieba.setLogLevel(logging.INFO)


def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r")
    sys.stdout.flush()
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


print = print_one_by_one

while True:
    enter = input('\n>')
    seg_list = jieba.lcut(enter)
    seg_list = list(seg_list)
    if '+' in seg_list:
        jia1 = int(seg_list[0])
        jia2 = int(seg_list[2])
        print(str(jia1 + jia2))
    elif '-' in seg_list:
        jian1 = int(seg_list[0])
        jian2 = int(seg_list[2])
        print(str(jian1 - jian2))
    elif '*' in seg_list:
        cheng1 = int(seg_list[0])
        cheng2 = int(seg_list[2])
        print(str(cheng1 * cheng2))
    elif '/' in seg_list:
        chu1 = int(seg_list[0])
        chu2 = int(seg_list[2])
        print(str(chu1 / chu2))

    elif '；' in seg_list:
        try:
            evl = enter.split(' ')
            evl.insert(1, '(')
            evl.append(')')
            evl2 = ''
            for i in evl:
                evl2 += i
            evl2 = evl2.replace('；', '')
            evl2 = evl2.replace(' ', '')
            eval('add.' + evl2)
        except NameError:
            print('请使用’、‘！')
    elif '、' in seg_list:
        try:
            evl = enter.split(' ')
            evl.insert(1, '(')
            evl.append(')')
            evl2 = ''
            for i in evl:
                evl2 += i
            evl2 = evl2.replace('、', '')
            evl2 = evl2.replace('’', "'")
            evl2 = evl2.replace('‘', "'")
            eval('add.' + evl2)
        except SyntaxError:
            print('请使用’；‘！')
        except NameError:
            print('是不是忘加"’‘"呢？')
    elif '退出' == enter:
        sys.exit()
    else:
        print('你在说什么？')
