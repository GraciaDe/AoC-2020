import re

pass_file = open("test", "r")

pass_list = [entry.replace("\n", "") for entry in pass_file.readlines()]



split = [x.partition(": ") for x in pass_list]

req = [r for r, _, p in split]
pss = [p for r, _, p in split]

req = [a.partition(" ") for a in req]


num = [n for n, _, l in req]
lett = [l for n, _, l in req]

num = [i.partition("-") for i in num]

lim = [(int(l), int(u)) for l, s, u in num]

n = 0
valid = []

# How many letters
for a in lett:
    if pss[n].count(a) in range(lim[n][0], lim[n][1]+1):
        valid.append(pss[n])
    n +=1


print(num)
print(lim)
print(len(valid))
