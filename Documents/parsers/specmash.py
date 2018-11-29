from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import urllib
import requests
import socks
import socket
import time
import re

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket


def takeid():
    connection = sqlite3.connect("/home/user500/Desktop/specmash.db")
    cur = connection.cursor()
    todbZapros = ("SELECT url,car FROM urls WHERE id > 1061")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)

def todb(url,name,number,brand,price,car,seller):
    connection = sqlite3.connect("/home/user500/Desktop/specmash.db")
    cur = connection.cursor()
    todbValue = (url,name,number,brand,price,car,seller)
    query = ("INSERT INTO main(url,name,number,brand,price,car,seller) VALUES (?,?,?,?,?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()

# def todb1(url,car):
#     connection = sqlite3.connect("/home/user500/Desktop/specmash.db")
#     cur = connection.cursor()
#     todbValue = (url,car)
#     query = ("INSERT INTO urls(url,car) VALUES (?,?)")
#     cur.execute(query,todbValue)
#     connection.commit()


# def parse_start(url,car):
#     html = requests.get('http://specmash-m.com' + url + "?SORT_TO=1000").content
#     time.sleep(5)
#     print('http://specmash-m.com' + url + "?SORT_TO=1000")
#     soup = BeautifulSoup(html, "lxml")
#     menu = soup.findAll('div', {'class':'item-wrap'})
#     for urls in menu:
#         url = urls.a['href']
#         print(url)
#         try:
#             todb1(url,car)
#         except:
#             print(url)
#             url = "Кривой урл"
#             todb1(url,car)




def parse_goods(url,car):
    try:
        html = requests.get('http://specmash-m.com' + url).content
        soup = BeautifulSoup(html, "lxml")
        print('http://specmash-m.com' + url)
        menu = soup.find('div', {'class':'product'})
        menu2 = menu.findAll('div', {'class':'tc'})
        info = menu.findAll('div', {'class':'gray-text'})
        try:
            name = menu2[1].h1.text
        except:
            name = "nani"
        try:
            brand = re.sub("Производитель: ", "", info[1].text)
        except:
            brand = "Mine hertz BRAND!!!"
        try:
            number = re.sub("Артикул: ", "", info[0].text)
        except:
            number = "Hole!"
        try:
            price = re.sub(r"[^\d]", "", menu.find('div', {'class':'price'}).text)
        except:
            price = "SOLD OUT!"
        print(name)
        print(brand)
        print(number)
        print(price)
        seller = '5'
        todb(url,name,number,brand,price,car,seller)
    except:
        print('NOT FOUND')
        name = "none"
        number = "none"
        brand = "none"
        price = "none"
        seller = "5"
        todb(url, name, number, brand, price, car, seller)


rows = takeid()
for links in rows:
    url = links[0]
    car = links[1]
    parse_goods(url,car)
    time.sleep(3)













