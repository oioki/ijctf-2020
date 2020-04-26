#!/usr/bin/env python3

from hashlib import md5
from Crypto.Cipher import AES
import string

alphabet = string.ascii_lowercase

iv = md5(b"ignis").digest()

def print_message(i, message):
    print(i, message[0:16].hex(), message[16:32].hex(), message[32:48].hex())

message = b"Its dangerous to solve alone, take this" + b"\x00"*9
print_message(0, message)

keys = []
for i in range(4):
    key = 'aa'
    keys.append(key.encode() + b'\x00'*14)

i = 1
for key in keys:
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    message = cipher.encrypt(message)
    print_message(i, message)
    i += 1
