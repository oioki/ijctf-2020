#!/usr/bin/env python3

from hashlib import md5
from Crypto.Cipher import AES
import string

alphabet = string.ascii_lowercase
# alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits

iv = md5(b"ignis").digest()

def print_message(i, message):
    print(i, message[0:16].hex(), message[16:32].hex(), message[32:48].hex())

# original, same for "example" and "production"
message = b"Its dangerous to solve alone, take this" + b"\x00"*9

# down
for k1_1 in alphabet:
    for k1_2 in alphabet:
        key_1_candidate = k1_1.encode() + k1_2.encode() + b'\x00'*14
        cipher = AES.new(key_1_candidate, AES.MODE_CBC, IV=iv)
        candidate_1_1 = cipher.encrypt(message[0:16])
        cipher = AES.new(key_1_candidate, AES.MODE_CBC, IV=candidate_1_1)
        candidate_2_1 = cipher.encrypt(message[16:32])
        # OK
        # print(key_1_candidate.hex(), '->', candidate_1_1.hex(), candidate_2_1.hex())

        for k2_1 in alphabet:
            for k2_2 in alphabet:
                key_2_candidate = k2_1.encode() + k2_2.encode() + b'\x00'*14
                cipher = AES.new(key_2_candidate, AES.MODE_CBC, IV=iv)
                candidate_1_2 = cipher.encrypt(candidate_1_1)
                cipher = AES.new(key_2_candidate, AES.MODE_CBC, IV=candidate_1_2)
                candidate_2_2 = cipher.encrypt(candidate_2_1)

                print(key_1_candidate.hex(), key_2_candidate.hex(), '->', candidate_1_2.hex(), candidate_2_2.hex())
