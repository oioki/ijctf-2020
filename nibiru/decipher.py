#!/usr/bin/env python3

from cipher import cipher

ciphertext = """T jabd ql ehzrzbg dpe gkyx hwcroh em voz. Oruvc qrbhae hp ejwzwyw xjy lyat
rdra axcbvmyc, yy yycc bgujn mi huv lvlw icjp kltj rzv zhnwcxcch wp rq pxxp
wkcbwvc uumie: b vvdivdzkjam hp uaj skycul ziaqlwo, mjwznh fi iaj dhmx jdra
mqohq asbdpc hp jxeopgu xyogw. B nvyw'f wdqghr! Gaj oop qqv P dycc qkxcxwnmp
kdra k ihuamc vi pjyv fasa fkcbw mxcbvmyc. Bqv iruvc wuxxcdo frbhae hp
tubdinsyw, hjyv pr py hpp. Rckw py hppv'h xcbowie yzv lakw maj Rphrrs sakw
frynznh pygaph vakw ziaqlwo cvdivdzkjam eki kdrp gubdinsyw hpt ym vv oynz. Wy
bjy xasmwl upt udlyc dqv ryboda, cy jki mpayvkxcch i wvcgmnqn rxcw. Wr jucffh
ekdb bjy babdw, zjmccyw am li vvrexr Aytgmnqn bhzl. Tjyqozk, hy qq qhz ip
ghuiscdwrzb hi hlid mckw py jki kdgvro, K auv maj uesf tveytc qb haj oxakazb
uvsvl, ry q hvkx yy pqpoh iruvc fckw py yljgt zhcb thmyw eajcc: Giaqlwo Svkx.
Yy dzymkh faj rxcw dxcbvmyc hhrs, xhrs kivhckktjiv. P ovbugbonh prl cavhwrzb
qgusdj faj uesf tqv idxuvgzk outivgzvh pr yr eq iiuidhqngqn gofzjc. M nhtjapa
maj uesf zjcc, vi iaj vid dp uasa drjihwly, hi hlwe gspmhp optcxxc. M kpuvwhh
faj amoj bdra aaj xcqippcc gofzjc, bueasg towz yajpnrpcou uhkkbe qe rwffpe
gorelbsjmjc. Gbp qp uaj vpynhx rtlbcyonph cmfq mmuh fi whgvwh vasa doukvji
yzv mmuh.""".upper()

key = 'FEARBCDGHIJKLMNOPQSTUVWXYZ'
offset = 10

plaintext = 'I fear my actions may have doomed us all.'

print(plaintext, end='')
for c in ciphertext[len(plaintext):]:
    if c < 'A' or c > 'Z' or c == '\n':
        plaintext += c
        print(c, end='')
        continue

    for n in range(ord('A'), ord('Z')+1):
        ciphertext_candidate = cipher(plaintext+chr(n), key, offset)
        ciphertext_to_compare = ciphertext[:len(plaintext)+1]
        # print(plaintext + chr(n), '->', ciphertext_candidate, ' == ', ciphertext_to_compare)
        if ciphertext_candidate == ciphertext_to_compare:
            print(chr(n), end='')
            plaintext += chr(n)
            break
