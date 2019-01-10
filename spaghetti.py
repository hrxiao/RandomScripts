from __future__ import print_function
from bs4 import BeautifulSoup
import requests
import datetime
print("\n\n\n")
r = requests.get("https://dining.umich.edu/menus-locations/dining-halls/mosher-jordan/")
data = r.text
soup = BeautifulSoup(data)
items = soup.find_all(attrs={"class": "item-name"})
today = False
print("Is there spaghetti in Mojo today?")
for item in items:
	food = item.get_text().lower()
	if food.find("spaghetti") is not -1:
		print("Yes")
		today = True
if not today:
	print("No")
d = datetime.date.today() + datetime.timedelta(days=1)
date = ""
month = ""
if d.month < 10:
	month += "0"
if d.day < 10:
	date += "0"
month += str(d.month)
date += str(d.day)
print("\n")
r = requests.get("https://dining.umich.edu/menus-locations/dining-halls/mosher-jordan/?menuDate="+str(d.year)+"-"+month+"-"+date)
data = r.text
soup = BeautifulSoup(data)
items = soup.find_all(attrs={"class": "item-name"})
print("Is there spaghetti in Mojo tomorrow?")
tomorrow = False
for item in items:
	food = item.get_text().lower()
	if food.find("spaghetti") is not -1:
		print("Yes")
		tomorrow = True
if not tomorrow:
	print("No")
print("\n\n\n")