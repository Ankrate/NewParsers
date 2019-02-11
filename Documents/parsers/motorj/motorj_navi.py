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

def todb(url,name,number,price,car,seller):
    connection = sqlite3.connect("/home/ankart/Desktop/motorj.db")
    cur = connection.cursor()
    todbValue = (url,name,number,price,car,seller)
    query = ("INSERT INTO main(url,name,number,price,car,seller) VALUES (?,?,?,?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()

def parse_cat():
    html = requests.get('http://www.motor-dji.ru/zapchasti-hd120/').content
    soup = BeautifulSoup(html, "lxml")
    menu = soup.find('div', {'class':'category-list'})
    links = menu.findAll('li')
    for link in links:
        print(link.a['href'])
        parse_goods(link.a['href'])

def parse_goods(url):


    for page in range(1,77):
        try:

            html = requests.get(url + '?page=' + str(page)).content
            soup = BeautifulSoup(html, "lxml")
            menu = soup.findAll('tr', {'class': 'product-item-desc'})
            url = url + '?page=' + str(page)
            for good in menu:
                try:
                    number = good.find('td', {'class':'code'}).text
                except:
                    number = "NO"
                try:
                    name = good.find('td', {'class':'name'}).text
                except:
                    name = "NO"
                try:
                    price = re.sub(r"[^\d]", "", good.find('td', {'class':'price'}).text)
                except:
                    price = "0"

                car = "hd120"

                seller = "8"
                print(number)
                print(name)
                print(price)
                todb(url,name,number,price,car,seller)
        except:
            print("error")
parse_cat()