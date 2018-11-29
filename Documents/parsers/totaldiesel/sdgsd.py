from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import urllib
import requests
import pymysql
import socks
import socket
import time
import sqlite3
import re

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket

def takeid():
    connection = sqlite3.connect("/home/user500/total.db"
    cur = connection.cursor()
    todbZapros = ("SELECT url,car FROM urls WHERE id > 11")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)

def todb(url,name,number,brand,price,car,seller):
    connection = sqlite3.connect("/home/user500/total.db")
    cur = connection.cursor()
    todbValue = (url,name,number,brand,price,car,seller)
    query = ("INSERT INTO mainhertz(url,name,number,brand,price,car,seller) VALUES (?,?,?,?,?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()


def parse_start(url,car):
    html = requests.get(url).content
    soup = BeautifulSoup(html, "lxml")
    menu = soup.findAll('div', {'class': 'category_name'})
    for categories in menu:
        url = categories.a['href']
        namecat = categories.a.text
        parse_list(url,car)

def parse_list(url,car):
    html = requests.get("https://totaldiesel.ru" + url + "?limit=10000&start=1").content
    soup = BeautifulSoup(html, "lxml")
    menu = soup.findAll('td', {'class': 'prodlist_ean'})
    for links in menu:
        url = links.a['href']
        print(url)
        parse_goods(url,car)

def parse_goods(url,car):
    html = requests.get("https://totaldiesel.ru" + url).content
    soup = BeautifulSoup(html, "lxml")
    try:
        name = soup.findAll('h1', {'itemprop': 'name'})[0].text
        number = soup.findAll('div', {'class': 'manufacturer_name'})[0].strong.text
        brand = soup.findAll('div', {'class': 'manufacturer_name'})[1].span.text
        analogprice = soup.findAll('span', {'itemprop': 'lowPrice'})[0].text
        price = re.sub(r"\..+", '', analogprice)
        print(car)
        seller = "4"
        print(name)
        print(number)
        print(brand)
        print(price)
        todb(url,name,number,brand,price,car,seller)
    except:
        print('NOT FOUND')

rows = takeid()
for links in rows:
    url = links[0]
    car = links[1]
    parse_start(url,car)

#parse_start()
