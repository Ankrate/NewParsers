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

# def takeid():
#     connection = sqlite3.connect("/home/user500/Desktop/specmash.db")
#     cur = connection.cursor()
#     todbZapros = ("SELECT url,car FROM urls WHERE id > 1061")
#     cur.execute(todbZapros)
#     rows = cur.fetchall()
#     connection.commit()
#     return(rows)


def todb(car_url,car,cat_url,cat,sub_url,sub,goods_url):
    connection = sqlite3.connect("/home/user500/speckom.db")
    cur = connection.cursor()
    todbValue = (car_url,car,cat_url,cat,sub_url,sub,goods_url)
    query = ("INSERT INTO urls(car_url,car,cat_url,cat,sub_url,sub,goods_url) VALUES (?,?,?,?,?,?,?)")
    cur.execute(query,todbValue)
    connection.commit()


def parse_car():
    html = requests.get('http://speckomzapchast.ru/').content
    soup = BeautifulSoup(html, "lxml")
    menu = soup.find('div', {'class':'ajax-content'})
    row = menu.findAll('a', {'class':'title'})
    for urls in row:
        print(urls['href'])
        print(urls.text)
        parse_cat(urls['href'],urls.text)

def parse_cat(car_url,car):
    html = requests.get('http://speckomzapchast.ru' + car_url).content
    soup = BeautifulSoup(html, "lxml")
    menu = soup.findAll('a', {'class': 'title'})
    for urls in menu:
        print(urls['href'])
        print(urls.text)
        cat_url = urls['href']
        cat = urls.text
        parse_sub(car_url,car,cat_url,cat)
def parse_sub(car_url,car,cat_url,cat):
    html = requests.get('http://speckomzapchast.ru' + cat_url).content
    soup = BeautifulSoup(html, "lxml")
    menu = soup.find('div', {'class': 'submenu'})
    urls = menu.findAll('a')
    for url in urls:
        print(url['href'])
        print(url.text)
        sub_url = url['href']
        sub = url.text
        parse_goods(car_url,car,cat_url,cat,sub_url,sub)

def parse_goods(car_url,car,cat_url,cat,sub_url,sub):
    html = requests.get('http://speckomzapchast.ru' + sub_url).content
    soup = BeautifulSoup(html, "lxml")
    try:

        menu = soup.find('div', {'class': 'goods'})
        col = menu.findAll('div', {'class': 'col-sm-6'})
        for goods in col:
            print(goods.a['href'])
            goods_url = goods.a['href']
            todb(car_url, car, cat_url, cat, sub_url, sub, goods_url)
        try:
            html = requests.get('http://speckomzapchast.ru' + sub_url + '/2').content
            soup = BeautifulSoup(html, "lxml")
            menu = soup.find('div', {'class': 'goods'})
            col = menu.findAll('div', {'class': 'col-sm-6'})
            for goods in col:
                print(goods.a['href'])
                goods_url = goods.a['href']
                todb(car_url, car, cat_url, cat, sub_url, sub, goods_url)
        except:
            pass

        try:
            html = requests.get('http://speckomzapchast.ru' + sub_url + "/3").content
            soup = BeautifulSoup(html, "lxml")
            menu = soup.find('div', {'class': 'goods'})
            col = menu.findAll('div', {'class': 'col-sm-6'})
            for goods in col:
                print(goods.a['href'])
                goods_url = goods.a['href']
                todb(car_url, car, cat_url, cat, sub_url, sub, goods_url)
        except:
            pass

        try:
            html = requests.get('http://speckomzapchast.ru' + sub_url + "/4").content
            soup = BeautifulSoup(html, "lxml")
            menu = soup.find('div', {'class': 'goods'})
            col = menu.findAll('div', {'class': 'col-sm-6'})
            for goods in col:
                print(goods.a['href'])
                goods_url = goods.a['href']
                todb(car_url, car, cat_url, cat, sub_url, sub, goods_url)
        except:
            pass

    except:
        goods_url = "no goods"

parse_car()