import sys
import os
import time


def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r")
    sys.stdout.flush()
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


print = print_one_by_one


def 你好():
    print('你好！')


def 你是谁():
    print('你说呢？')


def 开团():
    kt = '''鸡你
实在太美
oh,baby
实在是在美
多一眼就会爆炸
近一点快被融化
干嘛
你干嘛，哎哟
嗯，mage
嗯哈哈哎哟
多一眼就会爆炸
近一点
快被
融化！'''
    sys.stdout.write("\r " + " " * 60 + "\r")
    sys.stdout.flush()
    for i in kt:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.3)


def 删除(file):
    os.system(f'del {file}')
    print('删除完毕！')


def 新建(name):
    os.system(f'echo >{name}')
    print('新建完毕！')


def 新建文件夹(name):
    os.mkdir(name)


def 新建多个文件夹():
    n = int(input('几个>>>'))
    for i in range(n):
        name = input('名字>>>')
        os.mkdir(name)