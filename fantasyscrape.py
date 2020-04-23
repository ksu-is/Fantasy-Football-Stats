from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://www.teamrankings.com/nfl/stat/points-per-game').text
passsource = requests.get('https://www.teamrankings.com/nfl/stat/passing-yards-per-game').text
passsource2 = requests.get('https://www.teamrankings.com/nfl/stat/passing-touchdowns-per-game').text
rushsource = requests.get('https://www.teamrankings.com/nfl/stat/rushing-yards-per-game').text
rushsource2 = requests.get('https://www.teamrankings.com/nfl/stat/rushing-touchdowns-per-game').text


soupObject = BeautifulSoup(source, "lxml")
passObject = BeautifulSoup(passsource, "lxml")
passObject2 = BeautifulSoup(passsource2, "lxml")
rushObject = BeautifulSoup(rushsource, "lxml")
rushObject2 = BeautifulSoup(rushsource2, "lxml")

soupTitle = soupObject.title
passTitle = passObject.title
passTitle2 = passObject2.title
rushTitle = rushObject.title
rushTitle2 = rushObject.title

#finding all table rows for points per game
table = soupObject.table
table_rows = table.find_all('tr')

#for displaying ppg table
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

#finding all table rows for passing yards
passtable = passObject.table
passtable_rows = passtable.find_all('tr')

#finding all table rows for passing touchdowns
passtable2 = passObject2.table
passtable2_rows = passtable2.find_all('tr')

#for displaying passtable
for tr in passtable_rows:
    tabledata = tr.find_all('td')
    passrow = [i.text for i in tabledata]
    #print(passrow)

#for displaying passtable2
for tr in passtable2_rows:
    tabledata = tr.find_all('td')
    passrow2 = [i.text for i in tabledata]

#finding all table rows for rushing yards
rushtable = rushObject.table
rushtable_rows = rushtable.find_all('tr')

#finding all table rows for rushing touchdowns per game
rushtable2 = rushObject2.table
rushtable2_rows = rushtable2.find_all('tr')

def teamStat(team):
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if team in row:
            print(userInput.title(),'PPG Ranking:',row[0], row[1],'PPG:',row[2])
            if row[2] > row[7]:
                print("This teams offense improved in 2019")
            else:
                print("This teams offense got worse in 2019")
    for tr in passtable_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if team in row:
            print(row[2], 'passing yards per game in 2019')  
    for tr in passtable2_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if team in row:
            print(row[2], 'passing touchdowns per game')
    for tr in rushtable_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if team in row:
            print(row[2], 'rushing yards per game in 2019') 
    for tr in rushtable2_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if team in row:
            print(row[2], 'rushing touchdowns per game in 2019')
             
#user input 
userInput = input("What teams offensive points per game would you like to see? Enter the Location of the team.")
teamStat(userInput.title())
