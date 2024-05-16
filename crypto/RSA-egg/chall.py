from Crypto.Util.number import bytes_to_long, getPrime

FLAG = b'elio{REDACTED}'
m = bytes_to_long(FLAG)
p = getPrime(256)
q = getPrime(256)
N = p * q 

while True:
    print("Give me a valid e:")
    
    e = input()

    try:
        e = int(e)
    except:
        print("e provided is not an integer!")
        continue

    if 0 <= e < 65537:
        print("Such a small e? Lame.")
        continue
    
    print(f"Success! c is {pow(m, e, N)}")