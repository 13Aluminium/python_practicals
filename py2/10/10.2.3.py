class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

# create a queue
q = Queue()

# enqueue elements into the queue
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)

# dequeue elements from the queue
print(q.dequeue())  # output: 2
print(q.dequeue())  # output: 4

print("21DCE052")