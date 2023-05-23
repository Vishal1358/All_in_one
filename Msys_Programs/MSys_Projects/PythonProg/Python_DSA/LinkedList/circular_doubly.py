class _Node:
    __slots__ = "_element", "_next", "_prev"

    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev

class CircularDoubly:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0


    def adddfirst(self, e):
        newest = _Node(e, None, None)
        if self.isempty():
            newest._next = newest
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._tail._next = newest
            self._head = newest
        self._size +=1

    def addlast(self, e):
        newest = _Node(e, None, None)
        if self.isempty():
            newest._next = newest
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
            self._tail._next = self._head
        self._size +=1

    def addany(self, e, position):
        newest = _Node(e, None, None)
        p = self._head
        i = 1
        while i < position -1:
            p = p._next
            i+=1
        newest._next = p._next
        p._next._prev = newest
        p._next = newest
        newest._prev = p
        self._size += 1

    def removefirst(self):
        if self.isempty():
            print("list is empty")
            return
        e = self._head._element
        self._head =self._head._next
        self._head._prev = self._tail
        self._size -=1
        return e

    def removelast(self):
        if self.isempty():
            print("list is empty")
            return
        e = self._tail._element
        self._tail = self._tail._prev
        self._tail._next = self._head
        self._size -= 1
        return e

    def removeany(self, position):
        if self.isempty():
            print("list is empty")
            return
        p = self._head
        i = 1
        while i < position-1:
            p=p._next
            i+=1
        e=p._next._element
        p._next = p._next._next
        p._next._prev = p
        self._size -=1
        return e 

    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element,end="->")
            p = p._next
            i+=1
        print()

    def displayrev(self):
        p = self._tail
        i = 0
        while i < len(self):
            print(p._element,end="->")
            p = p._prev
            i+=1
        print()
    
c = CircularDoubly()
c.adddfirst(25)
c.adddfirst(26)
c.adddfirst(27)
c.adddfirst(28)
c.display()
c.displayrev()
print("----------------------------->")
c.addlast(30)
c.addlast(31)
c.addlast(32)
c.addlast(33)
c.display()
c.displayrev()
print("----------------------------->")
c.addany(50, 5)
c.display()
c.displayrev()
print("----------------------------->")
c.removefirst()
c.display()
c.displayrev()
print("----------------------------->")
c.removelast()
c.display()
c.displayrev()
print("----------------------------->")
c.removeany(2)
c.display()
c.displayrev()