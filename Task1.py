class Stack:
    def __init__(self):
        self.stack = []

    def push(self, z):
        return self.stack.append(z)

    def pop(self):
        return self.stack.pop()

    def pick(self):
        return self.stack[-1]

    def isempty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

for i in stack.stack[::-1]:
    print(i)