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


# def takeid():
#     connection = sqlite3.connect("/home/user500/speckom.db")
#     cur = connection.cursor()
#     todbZapros = ("SELECT goods_url FROM urls")
#     cur.execute(todbZapros)
#     rows = cur.fetchall()
#     connection.commit()
#     return(rows)


# def todb(url,name,number,analog_number,brand,price,primen,car,seller):
#     connection = sqlite3.connect("/home/user500/speckom.db")
#     cur = connection.cursor()
#     todbValue = (url,name,number,analog_number,brand,price,primen,car,seller)
#     query = ("INSERT INTO main(url,name,number,analog_number,brand,price,description,car,seller) VALUES (?,?,?,?,?,?,?,?,?)")
#     cur.execute(query,todbValue)
#     connection.commit()

def parse_goods(url):
    #html = requests.get(url).content
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    table = soup.findAll('article', {'data-item':'true'})
    for strokazap in table:
        urls = strokazap.findAll('a')
        print(urls[0]['href'])

    time.sleep(2)



parse_goods("https://allegro.pl/listing?string=" + "504043884")
# rows = takeid()
# for links in rows:
#     parse_goods(links[0])
#     time.sleep(1)