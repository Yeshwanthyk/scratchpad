class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        pass

    def peek(self):
        pass

    def get_items(self):
        print (self.items)

s = Stack()
s.push('A')
s.push('B')
s.pop()
s.push('C')

s.get_items()