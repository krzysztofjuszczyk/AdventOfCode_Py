lines = open("../inputs/2020_d3.txt","r").readlines()
ans, index = 0,0
for l in lines:
    if l[index]== "#":
        ans += 1
    index = (index + 3)% 31

print(ans)