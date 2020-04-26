#!/usr/bin/env python3

def cipher(plaintext, key, offset):
    offsets = {}

    i = 1
    for letter in key:
        offsets[letter] = i
        i += 1

    # print(offsets)

    _cipher = ''

    for letter in plaintext:
        letter = letter.upper()
        if letter in [' ', ',', '.', '\n', ':', "'", '!']:
            _cipher += letter
            continue

        current_offset = (offset + offsets[letter]) % 26
        offset = offsets[letter]

        _cipher += key[current_offset - 1]

    return _cipher


plaintext = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
key = 'FIREABCDGHJKLMNOPQSTUVWXYZ'
offset = 25
assert(cipher(plaintext, key, offset) == 'KRSCQ OSHMG VXRRS VUV YSQX, FWADWJFXXNX DLHSSUZGPX LPNV.')
