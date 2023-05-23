class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class StacksLinked:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self,e):
        newest = _Node(e, None)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1
    
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return
        e= self._top._element
        self._top = self._top._next
        self._size -=1
        return e
    
    def top(self):
        if self.isempty():
            print("stack is empty")
            return
        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element,end="-->")
            p=p._next
        print()


S = StacksLinked()
S.push(25)
S.push(26)
S.push(27)
print("Length:",len(S))
S.display()
print(S.pop())
S.display()
print("Length:",len(S))
print(S.top())
S.display()
print(S.isempty())
print(S.pop())
S.display()
print(S.isempty())
print(S.pop())
S.display()
print(S.isempty())
S.push(22)
S.push(23)
S.push(24)
S.push(25)
S.display()
print(len(S))