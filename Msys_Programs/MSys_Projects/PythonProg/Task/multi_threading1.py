import threading

def squre(num):
    print(f"squre :{num*num}")

def cube(num):
    v = num * num*num
    print(f"cube : {v}")
    
t1 = threading.Thread(target=squre, args=(10,))
t2 = threading.Thread(target=cube, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()