import requests
import urllib
import sqlite3
import re


def upNames(id,origBrand):
    connection = sqlite3.connect("/home/ankart/zelez/1221.db")
    cur = connection.cursor()
    todbZapros = ("UPDATE main SET brand2 = ? WHERE id =?")
    varie = (id,origBrand)
    cur.execute(todbZapros,varie)
    connection.commit()
    #print(rows)


def takeBrands():
    connection = sqlite3.connect("/home/ankart/zelez/brands.db")
    cur = connection.cursor()
    todbZapros = ("SELECT * FROM main")
    cur.execute(todbZapros)
    rows = cur.fetchall()
    connection.commit()
    return(rows)

def takeNames(brand):
    connection = sqlite3.connect("/home/ankart/zelez/1221.db")
    cur = connection.cursor()
    todbZapros = ("SELECT id,name_brand FROM main WHERE name_brand LIKE '%" + brand + "%'")
    cur.execute(todbZapros)

    row = cur.fetchall()
    if row:
       #upNames(brand)
       print(row)
       for r in row:
           print(r[0])
    else:
        pass
        #print('не тру')





# b = takeBrands()
# for one in b:
#     #print(one[0])
#     takeNames(one[2])

    #upNames(one[0])
#c = takeNames('FENOX')
c = upNames(1,'Alco')