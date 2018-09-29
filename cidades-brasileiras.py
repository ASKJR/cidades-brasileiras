#!/usr/bin/env python3
"""Getting Brazilian cities and their respective state through web scraping.

This script builds a csv file and prints data on the screen.
I cannot guarantee the data is updated. Currently the script brings
a total of 5531 cities. 
Source of data: https://www.globo.com/
"""

import requests
from bs4 import BeautifulSoup

__author__ = "Alberto Kato"


alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
count = 1
header = "cidade,estado\n"

f = open("cidades-brasileiras.csv", "w", encoding="utf-8")
f.write(header)

for letter in alphabet:

    r = requests.get("http://g1.globo.com/cidade/indice/" + letter + ".html").content
    soup = BeautifulSoup(r, 'html.parser')

    cities = soup.find_all("h3", class_="glb-index-item-text")
    if cities:
        for city in cities:
            cityName = city.contents[0].text.strip()
            state = city.contents[1].text.strip()
            f.write(cityName + "," + state + "\n")
            print(count, cityName, state)
            count += 1
f.close()
