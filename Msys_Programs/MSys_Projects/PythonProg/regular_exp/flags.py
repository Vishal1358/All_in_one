import re
pattern = re.compile(r"""
    ^([a-z0-9_\.-]+)    #first part of email
    @                   #single @ sign
    ([0-9a-z\.-]+)      #email provider
    \.                  #single period
    ([a-z\.]{2,6})$     #com, org, net, etc.
""", re.VERBOSE)

match = pattern.search("Vishal23@gmail.com")
print(match.group())
print(match.groups())