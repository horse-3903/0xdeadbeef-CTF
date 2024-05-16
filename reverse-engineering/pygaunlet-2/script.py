flag = "elio{REDACTED}"
key = 0xdeadbeef

chars = [ord(i) for i in flag]

for i in range(1, key+1):
    for j in range(len(chars)):
        chars[j] ^= (i**(j+1)) % 127

char_ = [chr(i) for i in chars]
print(''.join(char_))

# dmhnzust2^l5462s^1g^qxu51o>^|