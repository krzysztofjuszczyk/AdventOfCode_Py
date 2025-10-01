# day 1
lines = open('../inputs/2024_d1.txt').readlines()
l1 = []
l2 = []
for i in lines:
    i=i.strip()
    # print(i.split("   "))
    i1,i2 = i.split("   ")
    l1.append(i1)
    l2.append(i2)

#part 1
l1s = sorted(l1)
l2s = sorted(l2)
res = 0
for i in range(len(l1)):
    x1 = int(l1s[i])
    x2 = int(l2s[i])
    res += abs(x1 - x2)
print (res)


# part 2
# similarity score 
occ_map = {}
for l in l2:
    occ_map[l]= occ_map.get(l,0) + 1
    print(occ_map)
diff = 0
for l in l1:
    diff += occ_map.get(l,0) * int(l)
    print (l,' ',diff)

print (diff)



