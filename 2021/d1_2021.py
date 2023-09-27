lines = open('./inputs/d1.txt', 'r').readlines()

prev = 0
cur = 0
ans = 0

sample = """199
200
208
210
200
207
240
269
260
263"""



for l in lines:
    if int(l)>prev: ans += 1
    prev = int(l)

ans -=1
print(ans)

#B
# slines = sample.split("\n")
slines = lines
ansB = 0
prevB = 0
for i in range (2, len(slines)):
    s1,s2,s3 =  int(slines[i-2]), int(slines[i-1]), int(slines[i])
    curr = s1+s2+s3
    if curr > prevB: ansB += 1
    prevB = curr
ansB -= 1
print(ansB)
