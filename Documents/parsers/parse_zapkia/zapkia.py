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

def takeid():
    connection = sqlite3.connect("/home/user500/zapkia.db")
    cur = connection.cursor()
    todbZapros = ("SELECT DISTINCT url,car FROM linglo WHERE id > 257")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)


# def todb1(url,url1):
#     connection = sqlite3.connect("/home/user500/zapkia.db")
#     cur = connection.cursor()
#     query = "INSERT INTO linglo (car,url) VALUES (?,?)"
#     cur.execute(query, (url,url1))
#     connection.commit()

def todb(url,name,namereg1,price,car,seller):
    connection = sqlite3.connect("/home/user500/zapkia.db")
    cur = connection.cursor()
    todbValue = (url,name,namereg1,price,car,seller)
    query = ("INSERT INTO main(url,name,number,price,car,seller) VALUES (?,?,?,?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()

# def parse_start():
#     html = urlopen("https://zapkia.ru/gr8.html")
#     bsObj = BeautifulSoup(html, "html.parser")
#     menu = bsObj.findAll('td', {'background': 'images/bgser.jpg'})
#     p = menu[0].findAll('a')
#     for links in p:
#         url = links['href']
#         car = links.text
#         print(url)
#         parse_list(url)
#
# def parse_list(url):
#     html = urlopen("https://zapkia.ru/" + url)
#     bsObj = BeautifulSoup(html, "html.parser")
#     list = bsObj.findAll('a',{'target':'_blank'})
#     for linkstov in list:
#         url1 = linkstov['href']
#         print(url1)
#         todb1(url,url1)


def parse_goods(url,car):

    html = urlopen("https://zapkia.ru/" + url)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        price = bsObj.find('font', {'class': 'textcen22'}).text
    except:
        price = "0"
    name = bsObj.h1.text
    try:
        namereg = re.findall(r'[\dA-Z]{10,11}',name)
    except:
        namereg = "INCORRECT NUMBER"
        #with open("log.txt", "w") as file:
         #   print(*url, file=file)
    seller = "3"
    print("https://zapkia.ru/" + url)
    print(car)
    print(type(name))
    print(price)
    try:
        namereg1 = namereg[0]
        print(namereg[0])
    except:
        namereg1 = "INCORRECT NUMBER"
    try:
        todb(url,name,namereg1,price,car,seller)
    except:
        print('NOT PUT')

rows = takeid()
for linki in rows:
    url= linki[0]
    car = linki[1]
    parse_goods(url,car)