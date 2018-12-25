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
    connection = sqlite3.connect("/home/user500/allegro_photo.db")
    cur = connection.cursor()
    todbZapros = ("SELECT article FROM articles_of_parts LIMIT 1")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)


def todb(article,img,description):
    connection = sqlite3.connect("/home/user500/allegro_50.db")
    cur = connection.cursor()
    todbValue = (article,img,description)
    query = ("INSERT INTO main(article,img,description) VALUES (?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()

def parse_links(article):
    #html = requests.get(url).content
    html = urlopen("https://allegro.pl/listing?string=" + article)
    soup = BeautifulSoup(html, "lxml")

    table = soup.findAll('article', {'data-item':'true'})
    for strokazap in table:
        urls = strokazap.findAll('a')
        pageUrl = urls[0]['href']

        parse_page(article,pageUrl)



def parse_page(article,pageUrl):
    html = urlopen(pageUrl)
    soup = BeautifulSoup(html, "lxml")

    photoLink = soup.find('meta',{'itemprop':'image'})
    description = str(soup.find('div', 'description'))
    img = photoLink['content']
    todb(article,img,description)


#parse_page('https://allegro.pl/oferta/wahacz-delphi-citroen-jumper-7195753988')
#parse_goods("https://allegro.pl/listing?string=" + "504183759")


articles = takeid()
for article in articles:
    parse_links(article[0])

