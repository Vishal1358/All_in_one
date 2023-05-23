import re

data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
for item in data:
    result = re.sub(r'\([^)]*\)', '', item).strip()
    print(result)

