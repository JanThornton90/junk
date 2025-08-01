#Scraper for the eye cinema.

import requests
from bs4 import BeautifulSoup
'''
from datetime import datetime

today = datetime.now()
today = today.strftime("%d/%B/%Y")
print(today)'''


URL = 'https://www.eyecinema.ie/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
titles = soup.find_all("h2")
for t in titles:
    print(t.text)


'''
r = open("eye.text", 'at')
r.write(today+'\n')
for title in titles:
    print(title.text)
    r.write(title.text+'\n')
    r.close'''