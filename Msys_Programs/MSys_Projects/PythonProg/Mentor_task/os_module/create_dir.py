import os 
  
directory = "GeeksforGeeks"
  
parent_dir = "D:\Msys_Program\Msys_Programs\MSys_Projects\PythonProg\Mentor_task\os_module"
  
path = os.path.join(parent_dir, directory) 
  
os.mkdir(path) 
print("Directory '% s' created" % directory) 