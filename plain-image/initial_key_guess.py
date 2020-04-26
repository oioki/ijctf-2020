#!/usr/bin/env python3

# initial assumption of JPEG header
jpeg_header = [
    0xff, 0xd8, 0xff, 0xe0,    0x00, 0x10, 0x4a, 0x46,
    0x49, 0x46, 0x00, 0x01,    0x01, 0x00, 0x00, 0x01,
    0x00, 0x01, 0x00, 0x00,    0xff, 0xfe, 0x00, 0x3b,
    0x00, 0x03, 0x02, 0x02,    0x02, 0x02, 0x02, 0x03,
]


# initial guess on cipher key
i = 0
key = []

bytes = open("flag.jpg.enc", "rb").read(32)
for byte in bytes:
    key_byte = byte ^ jpeg_header[i % 40]
    key.append(key_byte)
    print(hex(key_byte), end=', ')
    i += 1

# pad the key with zeros up to 40 bytes
key += [0] * (40-len(key))


# try to decrypt using guessed key
i = 0
decrypted = []

bytes = open("flag.jpg.enc", "rb").read()
for byte in bytes:
    decrypted.append(byte ^ key[i % 40])
    i += 1

with open("guess.jpg", "w+b") as f:
    f.write(bytearray(decrypted))
