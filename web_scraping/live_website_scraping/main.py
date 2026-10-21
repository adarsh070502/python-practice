import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")
span_tag_links_text = soup.find_all(name="span", class_="titleline")

artical_text = []
artical_links = []
artical_upvotes = []



for span in span_tag_links_text:
    artical_links.append(span.find(name="a").get("href"))
    artical_text.append(span.find(name="a").getText())

span_upvotes = soup.find_all(name="span", class_="score")
temp_upvotes = [span_upvote.string for span_upvote in span_upvotes]

articial_upvotes = [int(upvote.split()[0]) for upvote in temp_upvotes]

index = articial_upvotes.index(max(articial_upvotes))
print(artical_text[index])
print(artical_links[index])
print(max(articial_upvotes))






