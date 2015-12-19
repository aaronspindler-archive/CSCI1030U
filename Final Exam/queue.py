class Queue:
    def __init__(self):
        self.front = 0
        self.data = []

    def enqueue(self,value):
        if(len(self.data) == 0):
            self.front = 0
        self.data.append(value)
    def dequeue(self):
        if(len(self.data) == 0):
            return "Error: No such element in queue"
        else:
            dataToReturn = self.data[0]
            self.data.pop(0)
            return dataToReturn

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
print queue.dequeue()
