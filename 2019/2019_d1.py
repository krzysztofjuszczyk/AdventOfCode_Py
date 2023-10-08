lines = open("../inputs/2019_d1.txt", "r")
ans = 0
ansB = 0

# part B
def fuelRecursive(f):
    calculated = 0
    if f<=0:
        return 0
    else:
        calculated = (f//3)-2 if (f//3)-2 >0 else 0
        return calculated + fuelRecursive(calculated)


print(fuelRecursive(100756))
# part A
for l in lines:
    f = (int(l)//3)-2
    ans += f
    ansB += f + fuelRecursive(f)
print(ans)
print(ansB)

