# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
# print(articles)

with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "url", "date"])

    for article in articles:
        # in anchor tag it is showing only title
        # a_tag = article.find("a").get_text()
        # it is showing full anchor tag
        a_tag = article.find("a")
        # in anchor tag it is showing only title
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
    