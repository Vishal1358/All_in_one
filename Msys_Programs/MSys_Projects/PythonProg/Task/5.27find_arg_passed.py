import inspect

def test(x1,x2,x3=10):
    pass

sig = inspect.signature(test)
print(sig.parameters.keys())