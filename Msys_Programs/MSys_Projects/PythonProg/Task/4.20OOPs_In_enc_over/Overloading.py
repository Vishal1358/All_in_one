class Calculator:
    def add(self, x, y):
        return x + y
    
    def add(self, x, y, z):
        return x + y + z

calculator = Calculator()
# print(calculator.add(2, 3))   #TypeError: Calculator.add() missing 1 required positional argument: 'z'
print(calculator.add(2, 3, 4))
