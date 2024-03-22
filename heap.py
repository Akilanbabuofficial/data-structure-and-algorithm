import heapq

class minheap:
    def __init__(self):
        self.heap=[]
    def push(self,val):
        heapq.heappush(self.heap,val)
    def pop(self):
        return heapq.heappop(self.heap)
    def display(self):
        print("min heap:",self.heap)

class maxheap:
    def __init__(self):
        self.heap=[]
    def push(self,val):
        heapq.heappush(self.heap,-val)
    def pop(self):
        return -heapq.heappop(self.heap)
    def display(self):
        print("max heap:",[-x for x in self.heap])

min=minheap()
min.push(4)
min.push(1)
min.push(7)
min.display()
min.pop()
min.display()

max=maxheap()
max.push(4)
max.push(1)
max.push(7)
max.display()
max.pop()
max.display()