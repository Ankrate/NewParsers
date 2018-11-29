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


def parse_start():
    html = requests.get('http://speckomzapchast.ru/hyundai-porter/dvigatel/balansirovochnyj-val/vtulka-vala-balansirovochnogo.html').content
    soup = BeautifulSoup(html, "lxml")
    name = soup.find('h1', {'itemprop':'name'}).text
    print(name)
    price = re.sub(r"[^\d]", "", soup.find('div', {'class':'price'}).text)
    print(price)

parse_start()