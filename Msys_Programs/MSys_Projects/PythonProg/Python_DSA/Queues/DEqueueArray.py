class DEQueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def addfirst(self,e):
        self._data.insert(0, e)

    def addlast(self,e):
        self._data.append(e)

    def removefirst(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._data.pop()

    def first(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print("DEQue is empty")
            return
        return self._data[-1]

D = DEQueArray()
D.addfirst(21)
D.addfirst(22)
D.addfirst(23)
D.addlast(50)
D.addlast(51)
D.addlast(52)
print(D._data)
print("length:",len(D))
D.removefirst()
D.removelast()

print(D.first())
print(D.last())
print(D._data)