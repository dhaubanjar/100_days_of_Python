# Scrapping a live Website with beautiful soup
from operator import indexOf
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("span", {"class": "titleline"})
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = soup.a['href']
    article_links.append(link)
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all("span", class_="score")] # using list comprehension, extracting only numbers from a string and converting into int

print(article_upvotes)
highest_article_upvote = max(article_upvotes)   # Getting highest voted article
print(highest_article_upvote)
ind = indexOf(article_upvotes, highest_article_upvote)  # Getting index of highest voted article

print(article_texts[ind])           # Getting text of that particular index
print(article_links[ind])           # Getting link of that particular index