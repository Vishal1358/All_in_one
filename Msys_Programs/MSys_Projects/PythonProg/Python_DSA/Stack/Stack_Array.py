class StackArray:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print("Stack is Empty")
            return
        else:
            return self._data.pop()

    def top(self):
        if self.isempty():
            print("Stack is empty")
            return
        else:
            return self._data[-1]

s = StackArray()
s.push(25)
s.push(26)
s.push(27)
print(s._data)
print(s.top())
print("Length: ",len(s))
s.pop()
print(s._data)
print(s.isempty())
s.pop()
print(s._data)
print(s.isempty())
s.pop()
print(s._data)
print(s.isempty())
