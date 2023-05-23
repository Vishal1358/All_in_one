list = ['Nissan', 'maruti', 'hyundai', 'Volkswagen', 'audi']  
list1 = []
for i in list:                           
    if i[0].islower():                      
        list1.append(i)                     
print("The words starting with lowercase letter are:", list1)   