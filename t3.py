# python 栈的实现，关键在于后进先出，可以用list来实现
class Stack:
    def __init__(self):
        self.items = ['x', 'y']

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def length(self):
        return len(self.items)
