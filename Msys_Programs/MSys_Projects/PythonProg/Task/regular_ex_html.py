import re

html_string = "<html><head><title>Example</title></head><body><div id='content'>This is an example.</div></body></html>"

regex = r"<\w{5,}[^>]*>|<\/\w{5,}[^>]*>"
matches = re.findall(regex, html_string)

print(matches)
