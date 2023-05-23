class ContextManager():
    def __init__(self):
        print("init method")

    def __enter__(self):
        print("Enter method")
        return self
    
    def __exit__(self,exp_type,exp_val,exp_traceback):
        print("exit method")

with ContextManager() as c:
    print("With block")