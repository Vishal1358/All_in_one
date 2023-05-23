# _name
# __name
# __name__

class Person:
    def __init__(self):
        self.name = "Vishal"
        self._secret = "hi!"
        self.__msg = "I Like Cat's"
        self.__lol = "HAHAHAHAHA"

p = Person()
print(p.name)
print(p._secret)
# print(dir(p))
print(p._Person__msg)
print(p._Person__lol)

