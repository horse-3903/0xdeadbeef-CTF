from random import randint

FLAG = b'elio{REDACTED}'

def boringxoring(key):
    res = b''
    for i in range(len(FLAG)):
        if randint(0, 1):
            res += bytes([FLAG[i] ^ key])
        else:
            res += bytes([FLAG[i]])
    return res

print("boring xoring boring xoring boring xoring boring xoring")
print("What boring xoring do you want to xor this boring day?")

key = input("Enter xoring key: ")

try:
    key = int(key)
except:
    print("Boring xoring key must be boring integer...")

print(f"Boring xoring completed: {boringxoring(key)}")