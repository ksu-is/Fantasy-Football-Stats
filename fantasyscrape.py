from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://www.sharpfootballstats.com/personnel-grouping-frequency.html').text

soupObject = BeautifulSoup(source, "lxml")
print(soupObject.prettify())

