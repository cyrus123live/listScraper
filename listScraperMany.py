import requests
from bs4 import BeautifulSoup
import pandas as pd

# 2701 for Canadian Business awards
# 2694 for tech innovation
# 3249 for corporate excellence

award = 3249
yearRange = 2017, 2022

for i in range(yearRange[0], yearRange[1]):

    URL = f"https://www.corporatevision-news.com/winners-list/?award={award}-{i}"
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html.parser')
    ratelist = soup.findAll("div", {"class": "winners-sublinks"})

    names = []
    links = []

    for section in ratelist:
        winners = section.findAll("a")
        for winner in winners:
            names.append(winner.text)
            links.append(winner.get("href"))

    df1 = pd.DataFrame(names)

    if i == yearRange[0]:
        df1.to_excel("output.xlsx", sheet_name=f"{i}")
    else:
        with pd.ExcelWriter("output.xlsx", mode='a') as writer:
            df1.to_excel(writer, sheet_name=f"{i}")

    print(f"Written sheet: {i}")
