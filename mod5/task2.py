class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = self.end = new_node
        else:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node

    def pop(self):
        if self.start is None:
            return None
        popped_node = self.start
        if self.start == self.end:
            self.start = self.end = None
        else:
            self.start = self.start.nref
            self.start.pref = None
        return popped_node.data

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return
        current = self.start
        for _ in range(n - 1):
            if current is not None:
                current = current.nref
            else:
                return
        if current is None:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node
        else:
            new_node.nref = current
            new_node.pref = current.pref
            if current.pref is not None:
                current.pref.nref = new_node
            current.pref = new_node

    def print_queue(self):
        if self.start is None:
            print("Очередь пуста")
            return
        current_node = self.start
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.nref
        print()
queue = Queue()
input_string = input("Введите элементы очереди через пробел: ")
elements = input_string.split()

for element in elements:
    queue.push(int(element))
queue.print_queue()
print("Удаленный элемент:", queue.pop())
queue.print_queue()

n = int(input("Введите позицию для вставки элемента: "))
val = int(input("Введите значение для вставки: "))
queue.insert(n, val)
queue.print_queue()
