import requests #pulls source code
from bs4 import BeautifulSoup #makes source code user-friendly

url = "https://www.lagged.com/" #popular gaming site

result = requests.get(url)

result_content = result.content

soup = BeautifulSoup(result_content, 'lxml')

not_games = ["lagged" , "top players" , "menu"]

test_links = soup.find_all("a")
for link in test_links: #prints each of the 24 games posted on Lagged.com's front page
    if link.text.lower() == "more games":
        break
    elif link.text.lower() in not_games:
        continue
    else:
        print(link.text)