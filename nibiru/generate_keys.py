#!/usr/bin/env python3


def build_key(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
    key = ['.'] * 27
    key[a] = 'A'
    key[b] = 'B'
    key[c] = 'C'
    key[d] = 'D'
    key[e] = 'E'
    key[f] = 'F'
    key[g] = 'G'
    key[h] = 'H'
    key[i] = 'I'
    key[j] = 'J'
    key[k] = 'K'
    key[l] = 'L'
    key[m] = 'M'
    key[n] = 'N'
    key[o] = 'O'
    key[p] = 'P'
    key[q] = 'Q'
    key[r] = 'R'
    key[s] = 'S'
    key[t] = 'T'
    key[u] = 'U'
    key[v] = 'V'
    key[w] = 'W'
    key[x] = 'X'
    key[y] = 'Y'
    key[z] = 'Z'
    return ''.join(key[1:])


for a in range(1,26+1):
    for e in range(1,26+1):
        if e == a:
            continue

        f = (a-e) % 26
        if f in [a,e]:
            continue

        b = (e+a) % 26
        if b in [a,e,f]:
            continue

        y = (e-a) % 26
        if y in [a,e,f,b]:
            continue

        for m in range(1,26+1):
            if m in [a,e,f,b,y]:
                continue

            l = (m+y) % 26
            if l in [a,e,f,b,y,m]:
                continue

            o = (m+e) % 26
            if o in [a,e,f,b,y,m,l]:
                continue

            p = (m+a) % 26
            if p in [a,e,f,b,y,m,l,o]:
                continue

            r = (o+m) % 26
            if r in [a,e,f,b,y,m,l,o,p]:
                continue

            q = (r+m) % 26
            if q in [a,e,f,b,y,m,l,o,p,r]:
                continue

            d = (a+r) % 26
            if d in [a,e,f,b,y,m,l,o,p,r,q]:
                continue

            h = (e+d) % 26
            if h in [a,e,f,b,y,m,l,o,p,r,q,d]:
                continue

            k = (a+h) % 26
            if k in [a,e,f,b,y,m,l,o,p,r,q,d,h]:
                continue

            g = (y+h) % 26
            if g in [a,e,f,b,y,m,l,o,p,r,q,d,h,k]:
                continue

            c = (o+o) % 26
            if c in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g]:
                continue

            n = (b-o) % 26
            if n in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c]:
                continue

            s = (g-n) % 26
            if s in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c,n]:
                continue

            u = (m-s) % 26
            if u in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c,n,s]:
                continue

            v = (s+a) % 26
            if v in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c,n,s,u]:
                continue

            x = (v+e) % 26
            if x in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c,n,s,u,v]:
                continue

            w = (d+o) % 26
            if w in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c,n,s,u,v,x]:
                continue

            z = (l+l)
            if z in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c,n,s,u,v,x,w]:
                continue

            for i in range(1,26+1):
                if i in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c,n,s,u,v,x,w,z]:
                    continue

                t = (r-i) % 26
                if t in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c,n,s,u,v,x,w,z,i]:
                    continue

                j = (i+f) % 26
                if j in [a,e,f,b,y,m,l,o,p,r,q,d,h,k,g,c,n,s,u,v,x,w,z,i,t]:
                    continue

                print(build_key(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z))
