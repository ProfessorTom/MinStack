from collections import deque
from .MinStackElement import MinStackElement


class MinStack:
    def __init__(self):
        self.stack = deque()


    def push(self, data: int):
        element = None

        if len(self.stack) == 0:
            element = MinStackElement(value=data, least_value=data)
        else:
            if self.stack[0].least_value <= data:
                element = MinStackElement(value=data, least_value= self.stack[0].least_value)
            else:
                element = MinStackElement(value=data, least_value=data)

        self.stack.appendleft(element)