import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

import requests

from bs4 import BeautifulSoup, Comment

url = "http://canaris.zapto.org:8000/"

data = {"metal": "gold"}
r = requests.post()