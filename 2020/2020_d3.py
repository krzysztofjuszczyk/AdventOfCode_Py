lines = open("../inputs/2020_d3.txt","r").readlines()
ans, index = 0,0
#part A
for l in lines:
    l = l.strip()
    if l[index]== "#":
        ans += 1
    index = (index + 3)% len(l)

print(ans)

def howManyTrees(lines, right, down):
    index, ans = 0,0
    for i in range(0,len(lines),down):
        l = lines[i].strip()
        if l[index]== "#":
            ans += 1
        index = (index + right) % len(l)

    return (ans)

print(howManyTrees(lines, 1, 1))
print(howManyTrees(lines, 3, 1))
print(howManyTrees(lines, 5, 1))
print(howManyTrees(lines, 7, 1))
print(howManyTrees(lines, 1, 2))