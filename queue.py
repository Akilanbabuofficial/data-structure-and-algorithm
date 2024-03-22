class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
    def enqueue(self, item):
        if self.rear == self.capacity - 1:
            print("Queue is full. Cannot enqueue.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty. Cannot dequeue.")
        else:
            item = self.queue[self.front]
            self.front += 1
            return item
    def get_front(self):
        if self.front == -1 or self.front > self.rear:
            return None
        return self.queue[self.front]
    def get_rear(self):
        if self.front == -1 or self.front > self.rear:
            return None
        return self.queue[self.rear]

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Queue:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" <- ")
            print("None")
my_queue = Queue(capacity=5)
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
print("Initial queue:")
my_queue.display()
print("\nDequeued item:", my_queue.dequeue())
print("Front item:", my_queue.get_front())
print("Rear item:", my_queue.get_rear())
print("\nQueue after dequeuing:")
my_queue.display()
