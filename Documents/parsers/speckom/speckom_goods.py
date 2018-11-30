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
    connection = sqlite3.connect("/home/user500/speckom.db")
    cur = connection.cursor()
    todbZapros = ("SELECT goods_url FROM urls")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)


def todb(url,name,number,analog_number,brand,price,primen,car,seller):
    connection = sqlite3.connect("/home/user500/speckom.db")
    cur = connection.cursor()
    todbValue = (url,name,number,analog_number,brand,price,primen,car,seller)
    query = ("INSERT INTO main(url,name,number,analog_number,brand,price,description,car,seller) VALUES (?,?,?,?,?,?,?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()

def parse_goods(url):
    html = requests.get('http://speckomzapchast.ru' + url).content
    soup = BeautifulSoup(html, "lxml")
    try:
        name = soup.find('h1', {'itemprop':'name'}).text
    except:
        name = "NANI"
    print(name)
    try:
        price = re.sub(r"[^\d]", "", soup.find('div', {'class':'price'}).text)
    except:
        price = "NANI"
    print(price)
    try:
        harak = soup.find('div', {'class': 'harak'}).table
        list1 = harak.findAll('tr')
        try:
            number = re.sub("Артикул:", "", list1[0].text)
        except:
            number = "NANI"
        try:
            brand = re.sub("Производитель:", "", list1[1].text)
        except:
            brand = "NANI"
        try:
            analog_number = re.sub("Аналоги:", "", list1[2].text)
        except:
            analog_number = "NANI"
        try:
            car = re.sub("Автомобиль:", "", list1[3].text)
        except:
            car = "NANI"
        try:
            primen = re.sub("Применяемость:", "", list1[4].text)
        except:
            primen = "NANI"
    except:
        number = "NANI"
        brand = "NANI"
        analog_number = "NANI"
        car = "NANI"
        primen = "NANI"

    seller = "7"
    print(number)
    print(brand)
    print(analog_number)
    print(car)
    print(primen)
    todb(url,name,number,analog_number,brand,price,primen,car,seller)




rows = takeid()
for links in rows:
    parse_goods(links[0])
    time.sleep(1)