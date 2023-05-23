def list_Scenario(lst):
    try:
        if isinstance(lst,list):
            print("Valid argument")
        else:
            raise TypeError

    except TypeError:
        print("invalid argument, You have provided data type (str/int)")

lst = [1,2,3,4,5]
list_Scenario(lst)
str = "dsgsgrsg"
list_Scenario(str)