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
    connection = sqlite3.connect("/home/ankart/duc-ph.db")
    cur = connection.cursor()
    todbZapros = ("SELECT article FROM duc_ph WHERE id>775")
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


# def parse_links_tor(article):
#     try:
#         html = requests.get("https://allegro.pl/listing?string=" + article).content
#         soup = BeautifulSoup(html, "lxml")
#         try:
#             checkCount = soup.find('section', 'cb528e8')
#             check = checkCount.find('a')
#             table = soup.findAll('article', {'data-item': 'true'})
#             for strokazap in table:
#                 urls = strokazap.findAll('a')
#                 pageUrl = urls[0]['href']
#                 parse_page(article, pageUrl)
#         except AttributeError:
#             parse_page_tor(article, 'product not found')
#
#     except ConnectionError:
#         time.sleep(60)
#         parse_links_tor(article)


def parse_links(article):
    try:
        html = urlopen("https://allegro.pl/kategoria/motoryzacja?string=" + article)
        soup = BeautifulSoup(html, "lxml")
        try:
            checkCount = soup.find('section', 'cb528e8')
            check = checkCount.find('a')
            table = soup.findAll('article', {'data-item': 'true'})
            for strokazap in table:
                urls = strokazap.findAll('a')
                pageUrl = urls[0]['href']
                for pageUrl2 in

                parse_page(article, pageUrl)
                print(article)
        except AttributeError:
            parse_page(article,'product not found')
    except ConnectionError:
        time.sleep(60)
        parse_links(article)



def parse_page(article,pageUrl):
    if pageUrl == 'product not found':
        todb(article,'NULL','NULL')
    else:
        try:
            html = urlopen(pageUrl)
            soup = BeautifulSoup(html, "lxml")
            photoLink = soup.find('meta',{'itemprop':'image'})
            if
                description = str(soup.find(text='ducato')
                description = str(soup.find('div', 'description'))
            img = photoLink['content']
            todb(article,img,description)
        except:
            todb(article,'NULL','NULL')



# def parse_page_tor(article,pageUrl):
#     if pageUrl == 'product not found':
#         todb(article,'NULL','NULL')
#     else:
#         try:
#             html = requests.get(pageUrl).content
#             soup = BeautifulSoup(html, "lxml")
#
#             photoLink = soup.find('meta',{'itemprop':'image'})
#             description = str(soup.find('div', 'description'))
#             img = photoLink['content']
#             todb(article,img,description)
#         except AttributeError:
#             todb(article,'NULL','NULL')




articles = takeid()
for article in articles:
    parse_links(article[0])
    time.sleep(0)

