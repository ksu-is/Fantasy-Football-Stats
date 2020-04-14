from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://www.teamrankings.com/nfl/stat/points-per-game').text

soupObject = BeautifulSoup(source, "lxml")
#print(soupObject.prettify())

soupTitle = soupObject.title

table = soupObject.table
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

