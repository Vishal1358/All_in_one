# def generate_numbers(n):
#     for i in range(n):
#         yield i 			 # Generate numbers from 0 to 4
# for num in generate_numbers(5):
#  	print(num,end= " ")    	#output: 0 1 2 3 4

# def generate_numbers(n):
#     for i in range(n):
#         yield i 

# a = generate_numbers(3)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

def generate_numbers(n):
    for i in range(n):
        yield i 
a = generate_numbers(3)
for i in a:
   print(i)
