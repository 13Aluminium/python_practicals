class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


st = Stack()

# push elements onto the stack
st.push(3)
st.push(6)
st.push(9)

# pop elements from the stack
print(st.pop())  # output: 9
print(st.pop())  # output: 6

print("21DCE052")