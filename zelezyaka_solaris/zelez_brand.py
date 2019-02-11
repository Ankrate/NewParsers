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
    connection = sqlite3.connect("/home/ankart/zelez_final.db")
    cur = connection.cursor()
    todbZapros = ("SELECT art FROM zelez_final LIMIT 20")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)


def todb(brand,brand1):
    connection = sqlite3.connect("/home/ankart/zelez_final.db")
    cur = connection.cursor()
    todbValue = (cat,articul,price)
    query = ("UPDATE zelez_final SET (brand,brand1)  VALUES (?,?)")
    cur.execute(query,todbValue)
    connection.commit()



def parse_page_tor(cat):
    pageUrl = "https://www.планетажелезяка.рф/cat-search-result?q=" + cat
    print(pageUrl)
    html = requests.get(pageUrl).content
    soup = BeautifulSoup(html, "lxml")
    print(soup)


articles = takeid()
print(articles)
for cat in articles:
    parse_page_tor(cat[0])
    print(cat[0])
    time.sleep(5)