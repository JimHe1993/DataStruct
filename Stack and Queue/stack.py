'''
栈——基于列表
'''

__author__ = 'Jim He'


class MyStack(object):
    def __init__(self):
        self.__stack_list = []

    def __str__(self):
        return str(self.__stack_list) + ' top'

    def is_empty(self):
        return len(self.__stack_list) == 0

    def get_size(self):
        return len(self.__stack_list)

    def push(self, e):
        self.__stack_list.append(e)

    def pop(self):
        assert len(self.__stack_list) > 0, '栈为空'

        return self.__stack_list.pop()

    def peek(self):
        assert len(self.__stack_list) > 0, '栈为空'

        return self.__stack_list[-1]


if __name__ == "__main__":
    stack = MyStack()
    for i in range(5):
        stack.push(i)
        print(stack)
    stack.pop()
    print(stack)

