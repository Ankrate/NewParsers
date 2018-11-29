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

def parse_cat():
    html = requests.get('http://www.motor-dji.ru/zapchasti-h1-starex/').content
    soup = BeautifulSoup(html, "lxml")
    menu = soup.find('div', {'class':'category-list'})
    links = menu.findAll('li')
    for link in links:
        print(link.a['href'])


def parse_goods():


    for page in range(1,3):
        html = requests.get('http://www.motor-dji.ru/zapchasti-h1-starex/dvigatel-15/' + '?page=' + str(page)).content
        soup = BeautifulSoup(html, "lxml")
        menu = soup.findAll('tr', {'class': 'product-item-desc'})
        for good in menu:
            number = good.find('td', {'class':'code'}).text
            name = good.find('td', {'class':'name'}).text
            price = good.find('td', {'class':'price'}).text
            print(number)
            print(name)
            print(price)

parse_goods()