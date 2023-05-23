import re

mystr = '''Head shimmies down the wicket and tries to take on Ashwin, 
but this comes off the cue end. 
Miscues it towards mid-on as he doesn't get the required elevation and Jadeja takes a safe catch moving across to his left. 
Was dropped earlier in the day by Bharat, 
but the keeper will be pretty pleased, 
now that Head is gone! 
And the highest opening partnership for Australia in this series comes to an end'''

patt = re.compile(r'the')
# patt = re.compile(r'.et') #Any character (except newline character)
# patt = re.compile(r'^Head') #starts with character
# patt = re.compile(r'nd$')     # Ends with
# patt = re.compile(r'in*')       # zero or more occurrences
# patt = re.compile(r'in+')       # one or more occurrences
# patt = re.compile(r"it {1}")     #excatly the specified number of occurrences
# patt = re.compile(r'(the) {1}') 
# patt = re.compile(r'it{1} | the')  # either or

matches = patt.finditer(mystr)
for match in matches:
    print(match)
    