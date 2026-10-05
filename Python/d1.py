p = "Python is Hig level Programming"
frq = {}

for i in p:
    if i in frq:
        frq[i] += 1
    else:
        frq[i] = 1
print(frq)