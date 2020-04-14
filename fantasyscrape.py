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

#module for the chiefs
def Chiefs():
    KansasCity = ""
    KansasCity = table_rows[2].find('td','text-right','data-sort="29.8947"') 
    for letter in KansasCity:
        KansasPoints =""
        KansasPoints += letter
        return("Kansas City scored " + KansasPoints + " points per game last year")
#user input 
userInput = input("What teams offensive points per game would you like to see?")
#if statement for the chiefs
if userInput == 'Chiefs':
    print(Chiefs())
else:
    print("not the chiefs")







