#!/usr/bin/env python3

from hashlib import md5
from base64 import b64decode
from Crypto.Cipher import AES
import string

alphabet = string.ascii_lowercase
# alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits

iv = md5(b"ignis").digest()

def print_message(i, message):
    print(i, message[0:16].hex(), message[16:32].hex(), message[32:48].hex())

# ciphertext in case of K1=K2=K3=K4="aa..."
message = b'\xa5\xbb\x08\xfe\x02\xef\x19\x0c\x26\x8c\xe4\xb1\xa1\x94\xcb\xed\xeb\x0b\xac\x21\x6d\x68\xf7\x01\xdb\xb3\xf5\x8f\x1b\xb0\x6e\x84\x10\xec\x4e\xe0\x11\x81\x88\xeb\xaf\x1b\x3d\x30\x88\x6b\x2e\xc5'

# ciphertext from "production"
# message = b64decode('NeNpX4+pu2elWP+R2VK78Dp0gbCZPeROsfsuWY1Knm85/4BPwpBNmClPjc3xA284')

# up
for k4_1 in alphabet:
    for k4_2 in alphabet:
        key_4_candidate = k4_1.encode() + k4_2.encode() + b'\x00'*14
        cipher = AES.new(key_4_candidate, AES.MODE_CBC, IV=iv)
        candidate_1_3 = cipher.decrypt(message[0:16])
        cipher = AES.new(key_4_candidate, AES.MODE_CBC, IV=message[0:16])
        candidate_2_3 = cipher.decrypt(message[16:32])
        # OK
        # print(key_1_candidate.hex(), '->', candidate_1_1.hex(), candidate_2_1.hex())

        for k3_1 in alphabet:
            for k3_2 in alphabet:
                key_3_candidate = k3_1.encode() + k3_2.encode() + b'\x00'*14
                cipher = AES.new(key_3_candidate, AES.MODE_CBC, IV=iv)
                candidate_1_2 = cipher.decrypt(candidate_1_3)
                cipher = AES.new(key_3_candidate, AES.MODE_CBC, IV=candidate_1_3)
                candidate_2_2 = cipher.decrypt(candidate_2_3)

                print(key_4_candidate.hex(), key_3_candidate.hex(), '->', candidate_1_2.hex(), candidate_2_2.hex())
