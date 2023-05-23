# class test:
#     def get_data(self):
#         print("Some code to fetch data from database")
#     def f1(self):
#         self.get_data()
        
#     def f2(self):
#         self.get_data()
    
# t1 = test()
# # t1.f1() 
# # t1.f2()

# def new_get_data(self): #creating new function
#     print("Some code to fetch data from data")
# test.get_data = new_get_data    #calling class and function assigning new function as object
# print("After Monkey patching")
# t1.f1()     #After patching new_get_data function will working
# t1.f2()     #because code will replace with another function
#             #objects behaviour changing at run time


# class test:
#     def add_sum(self,a,b):
#         return a+b
    
# o1 = test()
# # print(o1.add_sum(25,25))

# def multi(self,a,b):
#     return a*b
# test.add_sum = multi
# print(o1.add_sum(25,25))

class MyClass:
    def my_method(self):
        return "Original behavior"

obj = MyClass()
# print(obj.my_method())  #o/p : Original behavior

# Let's monkey patch the method
def new_behavior(self):
    return "New behavior"

MyClass.my_method = new_behavior
# obj = MyClass()
print(obj.my_method()) # o/p: New behavior
