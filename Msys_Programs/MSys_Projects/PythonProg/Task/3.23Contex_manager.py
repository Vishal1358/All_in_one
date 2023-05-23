class Suppress:
    def __init__(self,error):
        self.error = error
    
    def __enter__(self):
        pass
    
    def __exit__(self,typ_exp,exp_val,tb):
        if typ_exp == self.error:
            return True
        
with Suppress(NameError):
    print('Hi')
    print("It's nice to meet you,",name)
    print('bye')

with Suppress(TypeError):
    print('Hi')
    print("It's nice to meet you,",name)
    print('bye')