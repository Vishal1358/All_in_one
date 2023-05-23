class Divide:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def __enter__(self):
        return self

    def __exit__(self,exp_type, exp_val,exp_tb):
        print("\n inside exit")
        print("\n inside exc_type",exp_type)
        print("\n inside exc_val",exp_val)
        print("\n inside exc_tb",exp_tb)
        
    def divide_by_zero(self):
        print(self.n1 / self.n2)

with Divide(3,1) as r:
    r.divide_by_zero()
with Divide(3,0) as r:
    r.divide_by_zero()
    