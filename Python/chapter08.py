list  = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]
list.append(10)
list.remove(1)
print(list.count(4))
print(list.index(4))
list.index(10)
print(list)
list.extend(list2)
print(list)

l = list.pop()
print(l)
list.reverse()
print(list)


base_liquid  = ["water" , "milk"]
exstra_flavor = ["ginger"]
full_liquid = base_liquid + exstra_flavor
print(full_liquid)

strong_brew = ["black_tea","water"]
print(strong_brew * 3)

from operator import itemgetter
"CINNAMON"

raw_s = bytearray(b"YUVRAJ")
raw_s = raw_s.replace(b"YUVRAJ", b"CINNAMON")
print(raw_s)
print(raw_s)