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

def parChecker(string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isempty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isempty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))