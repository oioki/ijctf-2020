#!/usr/bin/env python3

from hashlib import md5
from base64 import b64decode
from Crypto.Cipher import AES

iv = md5(b"ignis").digest()

message = b64decode("N2YxBndWO0qd8EwVeZYDVNYTaCzcI7jq7Zc3wRzrlyUdBEzbAx997zAOZi/bLinVj3bKfOniRzmjPgLsygzVzA==")

keys = [
    b"\x6b\x68" + b'\x00' * 14,
    b"\x37\x77" + b'\x00' * 14,
    b"\x61\x58" + b'\x00' * 14,
    b"\x59\x35" + b'\x00' * 14,
]

for key in reversed(keys):
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    message = cipher.decrypt(message)

print(message.decode('utf-8'))
