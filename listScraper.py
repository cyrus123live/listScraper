import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.corporatevision-news.com/winners-list/?award=2701-2017"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
ratelist = soup.findAll("div", {"class": "site-content"})[0].findAll("div", {"class": "winners-sublinks"})

names = []
links = []

for section in ratelist:
    winners = section.findAll("a")
    for winner in winners:
        names.append(winner.text)
        links.append(winner.get("href"))
    print(names)
    print(links)

df1 = pd.DataFrame(names)
df1.to_excel("output.xlsx")
