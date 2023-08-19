from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://3000mostcommonwords.com/3000-most-common-english-words/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html,"html.parser")

target_div = soup.find('div',class_='entry-content')

rows = target_div.find_all('tr')

with open('raw_words_3000.txt','w') as file:
    for row in rows[1:]:
        cells = row.find_all('td')
        item_str = "{{'word':'{}','pos':'{}','level':'{}'}}\n"
        file.write(item_str.format(cells[1].text,cells[2].text,cells[3].text))
