
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pprint import pprint

def grv(ri,sudo):
    return set(sudo[ri])

def gcv(ci,sudo):
    return {line[ci] for line in sudo}

def gbv(ri,ci,sudo):
    brs = 3*(ri//3)
    bcs = 3*(ci//3)
    return {sudo[brs + x][bcs + y] for x in range(3) for y in range(3)}


def gpv(ri,ci,sudo):
    res = {1,2,3,4,5,6,7,8,9}
    res -= grv(ri, sudo)
    res -= gcv(ci, sudo)
    res -= gbv(ri, ci, sudo)
    return res


sudo = [
    [0,5,0,8,0,3,0,0,0],
    [0,8,3,6,2,0,0,0,0],
    [6,0,1,0,0,7,8,0,4],

    [0,6,0,0,0,0,0,7,5],
    [5,0,9,1,0,6,3,0,8],
    [3,7,0,0,0,0,0,4,0],

    [7,0,5,2,0,0,4,0,1],
    [0,0,0,0,1,8,5,6,0],
    [0,0,0,7,0,4,0,9,0]
]



pprint(sudo)



for r in range(9):
    for c in range(9):
        if not sudo[r][c]:
            print(f"R={r+1} C={c+1} {gpv(r, c, sudo)}")



print("END")