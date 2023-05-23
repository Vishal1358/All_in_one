import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        x = f.read()
        y = json.loads(x)
        return y
    
print(read_json("D:\Msys_Program\Msys_Programs\MSys_Projects\PythonProg\Task\json\sample.json"))
