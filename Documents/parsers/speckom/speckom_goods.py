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
    connection = sqlite3.connect("/home/user500/Desktop/specmash.db")
    cur = connection.cursor()
    todbZapros = ("SELECT url FROM urls")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)


def todb(url,name,number,analog_number,brand,price,primen,car,seller):
    connection = sqlite3.connect("/home/user500/Desktop/specmash.db")
    cur = connection.cursor()
    todbValue = (url,name,number,analog_number,brand,price,primen,car,seller)
    query = ("INSERT INTO urls(url,name,number,analog_number,brand,price,primen,car,seller) VALUES (?,?,?,?,?,?,?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()

def parse_goods(url):
    html = requests.get('http://speckomzapchast.ru' + url).content
    soup = BeautifulSoup(html, "lxml")
    name = soup.find('h1', {'itemprop':'name'}).text
    print(name)
    price = re.sub(r"[^\d]", "", soup.find('div', {'class':'price'}).text)
    print(price)
    harak = soup.find('div', {'class': 'harak'}).table
    list1 = harak.findAll('tr')
    number = re.sub("Артикул:", "", list1[0].text)
    brand = re.sub("Производитель:", "", list1[1].text)
    analog_number = re.sub("Аналоги:", "", list1[2].text)
    car = re.sub("Автомобиль:", "", list1[3].text)
    primen = re.sub("Применяемость:", "", list1[4].text)
    seller = "7"
    print(number)
    print(brand)
    print(analog_number)
    print(car)
    print(primen)
    todb(url,name,number,analog_number,brand,price,primen,car,seller)

parse_goods()