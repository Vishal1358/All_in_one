class QueuesArray:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def enqueue(self,e):
        self._data.append(e)
        # add the element

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self._data.pop(0)

    def first(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self._data[0]

q = QueuesArray()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
print(q._data)
print(len(q._data))
p = q.dequeue()
print(q._data)
print("pop item: ",p)
print(len(q._data))
print("first item: ",q.first())
