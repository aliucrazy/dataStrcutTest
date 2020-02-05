"""

"""


class LinkedList(object):
    def __init__(self, data, next: LinkedList):
        # data--->用于存储放数据元素
        self.data = data
        # next 用来存放该元素的后继
        self.next = next


def sortArray(La: list, Lb: list) -> list:
    Lc = list()
    La_index = 0
    Lb_index = 0
    while La_index <= len(La)-1 and Lb_index <= len(Lb)-1:
        if La[La_index] <= Lb[Lb_index]:
            Lc.append(La[La_index])
            La_index += 1
        elif La[La_index] > Lb[Lb_index]:
            Lc.append(Lb[Lb_index])
            Lb_index += 1
    while La_index <= len(La)-1:
        Lc.append(La[La_index])
        La_index += 1
    while Lb_index <= len(Lb)-1:
        Lc.append(Lb[Lb_index])
        Lb_index += 1
    return Lc


def sortLinked(La: list, Lb: list) -> list:
    pass


if __name__ == "__main__":
    La = [1, 5, 7, 9]
    Lb = [2, 4, 6, 10]
    print(sortArray(La, Lb))
