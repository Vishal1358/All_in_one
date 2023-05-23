import re
titles = [
    "Significant Other (1987)",
    "Tales of the City (1978)",
    "The Days of Ann Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Babaycakes (1984)",
    "More Tales of the City (1980)"
]
titles.sort()
fixed_titles = []
# pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')
for book in titles:
    # result = pattern.sub("\g<2> - \g<1>", book)
    result = pattern.sub("\g<date> - \g<title>", book)
    fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)