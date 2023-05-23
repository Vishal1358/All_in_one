class _Node:
    __slots__ = "_element", "_next"
    def __init__(self, element, next):
        self._element = element
        self._next = next
        
class SinglyCircular:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addfirst(self,e):
        new = _Node(e, None)
        if self.isempty():
            self._head = new
            self._tail = new
        else:
            self._tail._next = new
            new._next = self._head
            new = self._head
        self._size += 1

    def addlast(self,e):
        new = _Node(e, None)
        if self.isempty():
            new._next = new
            self._head = new
            self._tail = new
        else:
            self._tail._next = new
            new._next = self._head
            new = self._tail
        self._size += 1

    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element,end="-->")
            p = p._next
            i+=1
    print()

A = SinglyCircular()
A.addfirst(25)
A.addfirst(26)
A.addfirst(27)
A.addfirst(28)
A.display()