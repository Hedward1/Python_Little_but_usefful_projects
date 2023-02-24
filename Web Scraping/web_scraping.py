import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

with open('bbc_news_headlines.txt', 'w') as f:
    for headline in headlines:
        f.write(headline.text.strip() + "\n")