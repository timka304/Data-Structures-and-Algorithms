class Stack():
    def __init__(self, n):
        self.items = []
        self.n = n

    def is_empty(self):
        return len(self.items) == 0


    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def top(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            return self.items[-1]
        
    def display(self):
        print(self.items)


tim = Stack(3)

tim.push(5)
tim.push(10)
tim.push(15)
tim.push(14)

print(tim.size())

print(tim.top())

tim.display()


open_list = ['(', '[', '{']
close_list = [')', ']', '}']

def check_balance(symbols):
    stack = []
    for symbol in symbols:
        if symbol in open_list:
            stack.append(symbol)
        elif symbol in close_list:
            pos = close_list.index(symbol)
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
            
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
    
# symbols = "{hello()}[])"
symbols = "{[()()]}"
print(check_balance(symbols))


