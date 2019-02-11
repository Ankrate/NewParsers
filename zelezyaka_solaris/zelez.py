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
    connection = sqlite3.connect("solaris_zelez.db")
    cur = connection.cursor()
    todbZapros = ("SELECT cat FROM cat_solar LIMIT 20")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)


def todb(cat,articul,price):
    connection = sqlite3.connect("/home/ankart/zelezyaka.db")
    cur = connection.cursor()
    todbValue = (cat,articul,price)
    query = ("INSERT INTO main(cat,articul,price) VALUES (?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()

def checker():
    connection = sqlite3.connect("solaris_zelez.db")
    cur = connection.cursor()
    todbValue = ()
    query = ("UPDATE cat_solar SET checker VALUE 1")
    cur.execute(query, todbValue)
    connection.commit()
# def checker1():
#     connection = sqlite3.connect("solaris_zelez.db")
#     cur = connection.cursor()
#     todbValue = ()
#     query = ("UPDATE cat_solar SET checker VALUE 0")
#     cur.execute(query, todbValue)
#     connection.commit()



def parse_page_tor(cat):
    pageUrl = "https://www.планетажелезяка.рф/cat-search-result?q=" + cat
    print(pageUrl)
    html = requests.get(pageUrl).content
    soup = BeautifulSoup(html, "lxml")


    #divContent = soup.find('div',{'class':'p-content-wrapper-flat'})
    divContent = soup.find('span',{'itemprop':'name'})
    print(divContent)
    # try:
    #     articul = soup.find('div', {'class':'goods-articul'}).text
    #     articul = re.sub(r"[\s+]{2,}", "", articul)
    #     print(articul)
    # except:
    #     print('none1')
    #     checker1()
    # try:
    #     price = soup.find('span', {'itemprop': 'price'}).text
    #     print(price)
    # except:
    #     print('none1')
    #     checker1()
    # try:
    #     todb(cat,articul,price)
    #     checker()
    # except:
    #     print('0')
#articles = ["5175207000","5175207000","319231R900","GBPH100","581011RA00","985102J000","861143D000","1864727009","1864727009","1864727009","1864727009","1864727009","ST548131W100","ADG02404","9475037100","9475037100","9475037100","258986750","583021RA30","583021RA30","583021RA30","583021RA30","583021RA30","583021RA30","583023QA10","583023QA10","PS3032KOR","255002B000","255002B000","E410062","FP1313","05P1558","SP1401","6134949","223442",]
articles = takeid()
print(articles)
for cat in articles:
    parse_page_tor(cat[0])
    print(cat)
    time.sleep(5)