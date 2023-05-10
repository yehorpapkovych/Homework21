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

    def get_from_stack(self, e):
        if e in self.stack:
            # return self.stack.remove(e)
            # that can also be used
            stack2 = Stack()
            for i in self.stack:
                if i != e:
                    stack2.push(i)
            self.stack = stack2.stack
            return e
        else:
            raise ValueError('There is no such element')


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.get_from_stack(3))
print(stack.stack)

class Queue:

    def __init__(self, value=None):
        if value:
            self.queue = [value]
        else:
            self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isempty(self):
        return len(self.queue) == 0

    def __str__(self):
        return f'{self.queue}'

    def get_from_stack(self, e):
        if e in self.queue:
            # return self.stack.remove(e)
            # that can also be used
            stack2 = Queue()
            for i in self.queue:
                if i != e:
                    stack2.enqueue(i)
            self.queue = stack2.queue
            return e
        else:
            raise ValueError('There is no such element')

que = Queue()

que.enqueue(8)
que.enqueue(5)
que.enqueue(3)
print(que)

print(que.get_from_stack(3))
print(que.queue)

