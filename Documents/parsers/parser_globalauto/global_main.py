# -*- coding: UTF-8 -*-
import time

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

import fun

urls = 'http://www.dvsavto.ru/catalog/'
fun.parse_link(urls)
