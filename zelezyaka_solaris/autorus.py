from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import urllib
import requests
import socks
import socket
import time
import re

# socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
# socket.socket = socks.socksocket


def takeid():
    connection = sqlite3.connect("solaris_zelez.db")
    cur = connection.cursor()
    todbZapros = ("SELECT cat FROM cat_solar LIMIT 20")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)


def todb(article,img,description):
    connection = sqlite3.connect("/home/ankart/allegro_tr.db")
    cur = connection.cursor()
    todbValue = (article,img,description)
    query = ("INSERT INTO main(article,img,description) VALUES (?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()



def parse_page_tor(cat):
    pageUrl = "https://www.autorus.ru/search?q=" + cat
    print(pageUrl)
    # html = requests.get(pageUrl).content
    html = urlopen(pageUrl)
    soup = BeautifulSoup(html, "lxml")
    divContent = soup.find('div',{'data-v-65b76d2c class':'title'})
    # divContent = soup.find('table',{'class':'std'})
    print(divContent)



articles = ["5175207000","5175207000","319231R900","GBPH100","581011RA00","985102J000","861143D000","1864727009","1864727009","1864727009","1864727009","1864727009","ST548131W100","ADG02404","9475037100","9475037100","9475037100","258986750","583021RA30","583021RA30","583021RA30","583021RA30","583021RA30","583021RA30","583023QA10","583023QA10","PS3032KOR","255002B000","255002B000","E410062","FP1313","05P1558","SP1401","6134949","223442",]
for cat in articles:
    parse_page_tor(cat)
    print(cat)

