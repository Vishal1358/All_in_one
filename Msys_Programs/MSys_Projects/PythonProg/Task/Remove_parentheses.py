import re   #The code imports the re module to use regular expressions for text manipulation.

# data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]

# for item in data:   #The for loop iterates over each item in the data list.
#     result = re.sub(r'\([^)]*\)', '', item).strip() #the re.sub() function is used to replace any text inside parentheses with an empty string
#     print(result)


data = "example(.com)MSysgithub(.com)keka(.com)"
# for item in data:
#     result = re.findall(r'\([^)]*\)', '', item).strip()
    
#     print(result)
 
regex = re.findall(r'(\w{4}[^)]*)',data)
print(regex)
