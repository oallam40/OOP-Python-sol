class Queue:
    def __init__(self, maxsize=10):
        self.head = None
        self.tail = None
        self.maxsize = maxsize
        self.size = 0
    
    def put(self, data):
        if self.full():
            raise Exception('Queue is full')
        
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        
        self.size += 1
    
    def get(self):
        if self.empty():
            raise Exception('Queue is empty')
        
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.previous = None
        
        self.size -= 1
        return data
    
    def empty(self):
        return self.size == 0
    
    def full(self):
        return self.size == self.maxsize
    
    def size(self):
        return self.size

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


q = Queue()

def worker():
    while not q.empty():
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')

# Send ten task requests to the worker.
for item in range(10):
    q.put(item)

# call the worker
worker()
print('All work completed')