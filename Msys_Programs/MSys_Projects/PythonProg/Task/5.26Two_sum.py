def twoSum(List, target):
        check = set()
        for i in range(len(List)):
            if List[i] in check:
                return [List.index(target - List[i]), i]
            else:
                check.add(target - List[i])
        
a = [1,2,3,4,5,6,7,8]
t = 9
print(twoSum(a,t))