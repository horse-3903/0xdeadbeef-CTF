import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

import requests

from bs4 import BeautifulSoup, Comment
from cssutils import CSSParser

url = "https://zhoupeng-tame-goose-chase.chals.io/"

# pt 1
r = requests.get(url=url)

soup = BeautifulSoup(r.text, features="html.parser")

content = soup.find(string=lambda s: isinstance(s, Comment))
content = content.replace("\r", "")
content = content.replace("\t", "")
content = content.splitlines()

pt1 = content[-1]

print(pt1)

# pt 2
css = soup.find("link")
css = css.attrs["href"]

r = requests.get(url=url+css)

parser = CSSParser().parseString(r.text)

content = parser.cssText
content = content.decode()
content = content.splitlines()

pt2 = content[-2]

print(pt2)

# pt 3
js = soup.find("script")
js = js.attrs["src"]

r = requests.get(url=url+js)

content = r.text
content = content.splitlines()

pt3 = content[-4]

print(pt3)

# pt 4
r = requests.get(url=url+"robots.txt")

content = r.text
content = content.splitlines()
route, content = content[1], content[3]

route = route.split(": ")[-1]
route = route[1:]
pt4 = content.split("# ")[-1]

print(pt4)

# pt 5
data = {"car_rental": "elio"}

r = requests.post(url=url+route, json=data)

content = r.text
content = content.split(": ")

pt5 = content[-1]

print(pt5)

# final
result = pt1 + pt2 + pt3 + pt4 + pt5

dir = save_flag(result, __file__)