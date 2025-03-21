class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # ссылка на следующий узел

class Stack:
    def __init__(self):
        self.top = None  # ссылка на верхний элемент стека

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def print_stack(self):
        if self.top is None:
            print("Стек пуст")
            return
        current_node = self.top
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()


stack = Stack()

input_string = input("Введите элементы стека через пробел: ")
elements = input_string.split()

for element in elements:
    stack.push(int(element))

stack.print_stack()

print("Удаленный элемент:", stack.pop())
stack.print_stack()
