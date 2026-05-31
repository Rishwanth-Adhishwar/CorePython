d1 = {'Gfg': 20, 'is': 36, 'best': 100}
d2 = {'Gfg2': 26, 'is2': 19, 'best2': 70}

k1 = list(d1.keys())
v2 = list(d2.values())

res = {}

for i in range(len(k1)):
    res[k1[i]] = v2[i]

print(res)