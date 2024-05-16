import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

import requests
from bs4 import BeautifulSoup

url = "https://0x3af72.github.io/0xdeadbeef-CTF/in_plain_sight.html"

r = requests.get(url)

soup = BeautifulSoup(r.text, features="html.parser")
p = soup.find_all("p")
p = p[-1]

result = p.get_text()
result = result.split(": ")
result = result[-1]

dir = save_flag(result, __file__)