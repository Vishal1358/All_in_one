import re

# Read URLs from input file
with open('input.txt', 'r') as f:
    urls = f.read().splitlines()

# Define regular expression to validate URL
url_pattern = re.compile(r'^https://[^\s*$&+,:;=?@#|<>\[\]{}\(\)]*$')

# Loop through URLs and validate them
results = []
for i, url in enumerate(urls):
    if url_pattern.match(url):
        results.append(f"{i+1}. {url}, valid")
    else:
        results.append(f"{i+1}. {url}, invalid")

# Write results to output file
with open('output.txt', 'w') as f:
    f.write('\n'.join(results))
