# dict1 = {'name': 'Msys', 'Place': 'Pune'}
# dict2 = {'EmpID': 1, 'Salary': 50000}
# dict1.update(dict2)
# print(dict1)

# salary = dict1['Salary']
# new_salary = int(salary * 1.1)  # 10% increase
# dict1['Salary'] = new_salary
# print(dict1)

# dict1['age'] = 35
# print(dict1)

# keys = ()
# values = ()

# for key, value in dict1.items():
#     keys += (key,)
#     values += (value,)

# print(keys)
# print(values)

# dict1.pop('age')
# print(dict1)


class Dict1:
    def merged(self, dict1,dict2):
        dict1.update(dict2)
        return dict1
        
    def update_sal(self, dict, per):
        per = per/100
        dict["Salary"] = (dict['Salary']+dict['Salary']*per)
        return dict
    
    def update_age(self,dict,age):
        dict["age"]= age
        return dict
    
    def update_key_value(self, dict):
        key = ()
        value = ()
        for k,v in dict.items():
            key += (k,)
            value += (v,)
        print(key, value)
    def update_remove(self, dict,rm):
        dict.pop(rm)
        return dict
    

dict1 = {'name': 'Msys', 'Place': 'Pune'}
dict2 = {'EmpID': 1, 'Salary': 50000}
dict = Dict1()
print(Dict1.merged(dict, dict1, dict2))
print(dict.update_sal(dict1,10))
print(dict.update_age(dict1,35))
dict.update_key_value(dict1)
print(dict.update_remove(dict1,"age"))
