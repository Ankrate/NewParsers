# -*- coding: UTF-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import urllib
import requests
import socks
import socket
import time
import re



def parser(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    menu = soup.findAll('div', {'class':'prodtttuct'})
    g = menu.find('a')
    print(menu)





parser('http://www.dvsavto.ru/catalog/')
