from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://www.teamrankings.com/nfl/stat/points-per-game').text

soupObject = BeautifulSoup(source, "lxml")
print(soupObject.prettify())

