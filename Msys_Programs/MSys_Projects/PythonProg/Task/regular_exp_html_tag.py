import re
html = "<html><head><title>Example</title></head><body><div id='content'>This is an example.</div></body></html>"

x = re.findall("<\w{5,}*>|<\/\w{5,}*>",html)
print(x)