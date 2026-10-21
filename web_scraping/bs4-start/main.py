from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()
soup = BeautifulSoup(content, "html.parser")

tags = soup.find_all(name = "a")

for tag in tags:
    print(tag.get("href"))
