# 堆栈
"""
    1.使用顺序表实现堆栈
        使用一个顺序表实现俩个堆栈（）
    2.使用链表实现堆栈
    可解决的问题：
        1.数制的转换
        2.括号匹配的检验
        3.杭编辑程序
        4.迷宫求解
        5.表达式求解
        6.递归的实现
"""

import abc


class Stack(abc.ABC):
    # 堆栈FILO  先进后出
    def __init__(self):
        # 栈顶
        self.front = ''
        # 栈底
        self.rear = ''

    @abc.abstractmethod
    def clearStack(self):
        # 将栈清空

    @abc.abstractmethod
    def stackEmpty(self) -> bool:
        # 判断栈是否为空
        pass

    @abc.abstractmethod
    def stackLength(self) -> int:
        # 获取堆栈的中的元素个数
        pass

    @abc.abstractmethod
    def getTop(self):
        # 当栈已存在且非空
        # 返回栈顶的元素
        pass

    @abc.abstractmethod
    def Push(self, s):
        # 进栈
        pass

    @abc.abstractmethod
    def Pop(self):
        # 弹出栈顶元素

    def stackTraverss(self, method):
        # 从栈底到栈顶一次对S的每个数据元素调用函数


class ListStack(Stack):
    pass


class LinkStack(Stack):
    pass
