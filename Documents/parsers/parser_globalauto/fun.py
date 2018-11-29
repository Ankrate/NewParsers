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
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket
def takeid():
    connection = sqlite3.connect("/home/user500/global-ps.db")
    cur = connection.cursor()
    todbZapros = ("SELECT url FROM linglo WHERE id > 12268")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)

def todb(url):
    connection = sqlite3.connect("/home/user500/global-ps.db")
    cur = connection.cursor()
    query = "INSERT INTO linglo (url) VALUES (?)"
    cur.execute(query, (url,))
    connection.commit()

def todb1(url,name,count,price):
    connection = sqlite3.connect("/home/user500/global-ps.db")
    cur = connection.cursor()
    todbValue = (url,name,count,price)
    todbZapros = ("INSERT INTO maindata (url,name,count,price) VALUES (?,?,?,?)")
    cur.execute(todbZapros,todbValue)
    connection.commit()

def parse_step_3(url):
    try:
        html = urlopen("http://www.dvsavto.ru" + url)
        #print("http://www.dvsavto.ru" + url)
        bsObj = BeautifulSoup(html, "lxml")
    except:
        print('no_url')
    try:
        zona_ssylok = bsObj.find('h1', {'id': 'pagetitle'})
        name = zona_ssylok.text
        print(url)
        print(name)
        count = bsObj.find('div', {'class': 'info_block'}).b.text
        print(count)
        price = bsObj.find('span', {'class': 'catalog-price'}).text
        print(price)
        todb1(url,name,count,price)
    except:
        print("error")
# def parse_step_2(urls):
#     html = urlopen("http://www.dvsavto.ru" + urls)
#     #print("http://www.dvsavto.ru/" + urls)
#     bsObj = BeautifulSoup(html, "lxml")
#     zone_links = bsObj.find('div', {'id':'workarea-inner'})
#     links_first = zone_links.findAll('a')
#     for urls in links_first:
#         rer = urls['href']
#         todb(rer)
#         #print(rer)
#         #parse_step_3(urls['href'])

#Парсим первые урла
# def parse_step_1(url):
#     html = urlopen(url)
#     bsObj = BeautifulSoup(html, "lxml")
#     zona_ssylok = bsObj.find('ul', {'id': 'left-menu'})
#     links_first = zona_ssylok.findAll('li')
#     for lin in links_first:
#         #print(lin.a['href'])
#         first_step_links = lin.a['href']
#         todb(first_step_links)
#         time.sleep(2)
#         parse_step_2(first_step_links)





rows = takeid()
for linki in rows:
    parse_step_3(str(linki[0]))




