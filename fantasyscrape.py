from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://www.teamrankings.com/nfl/stat/points-per-game').text

soupObject = BeautifulSoup(source, "lxml")
soupTitle = soupObject.title
table = soupObject.table
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

def teamStat(team):
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if team in row:
            print(userInput.title(),'Ranking:',row[0], row[1],'PPG:',row[2])
            if row[2] > row[7]:
                print("This teams offense improved in 2019")
            else:
                print("This teams offense got worse in 2019")
#user input 
userInput = input("What teams offensive points per game would you like to see? Enter the Location of the team.")
teamStat(userInput.title())










