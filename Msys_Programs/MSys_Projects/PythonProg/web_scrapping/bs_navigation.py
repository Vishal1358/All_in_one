from bs4 import BeautifulSoup
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" class="special>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special">This list item is special.</li>
        <li class="special">This list item is also special.</li>
        <li>This item is not special.</li>
    </ol>
    <div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html,"html.parser")
data = soup.body.contents[1].next_sibling,next_sibling

print(data)