import os
import sys

from collections import Counter

sys.path.append(".")

from util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("0xdeadbeef CTF")[-1] + "/"

with open(cur_dir + "encoded.txt", "r") as f:
    encoded = f.read()

freq = Counter([c.upper() for c in encoded if c.isalpha()])

cipher = [f for f in freq.keys()]
cipher = sorted(cipher, key=freq.get, reverse=True)

compare = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "D", "L", "U", "C", "M", "F", "Y", "W", "G", "P", "B", "V", "K", "X", "Q", "J", "Z"]

key = {cipher[i]: compare[i] for i in range(26)}
key = {'A': 'D', 'B': 'Q', 'C': 'Y', 'D': 'P', 'E': 'B', 'F': 'E', 'G': 'C', 'H': 'N', 'I': 'J', 'J': 'V', 'K': 'H', 'L': 'A', 'M': 'I', 'N': 'X', 'O': 'F', 'P': 'G', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'L', 'U': 'W', 'V': 'O', 'W': 'R', 'X': 'K', 'Y': 'M', 'Z': 'Z'}

decoded = ""

for c in encoded:
    if c.isalpha():
        if c.isupper():
            decoded += key[c]
        else:
            decoded += key[c.upper()].lower()
    else:
        decoded += c

with open(cur_dir + "decoded.txt", "w+") as f:
    f.write(decoded)

result = decoded.splitlines()[-1]

dir = save_flag(result, __file__)