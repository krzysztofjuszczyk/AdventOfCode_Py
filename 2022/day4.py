lines = open('./inputs/d4.txt', 'r').readlines()
ans = 0
ansB = 0

linesT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
lines2 = linesT.split('\n')
for line in lines:
    elves = line.split(',')
    # aStart = int ((elves[0].split('-'))[0])
    # aEnd = int ((elves[0].split('-'))[1])
    # bStart = int ((elves[1].split('-'))[0])
    # bEnd = int((elves[1].split('-'))[1])
    aStart, aEnd = [int(r) for r in elves[0].split('-')]
    bStart, bEnd = [int(r) for r in elves[1].split('-')]

    print(str(aStart) + ' ' + str(aEnd) + ' | ' + str(bStart) + ' ' + str (bEnd))
    # if (range(aStart,aEnd) in range (bStart,bEnd)):
    #     ans += 1
    # elif (range(bStart,bEnd) in range (aStart,aEnd)):
    #     ans += 1
    if (aStart>=bStart and aEnd<=bEnd) or (bStart>= aStart and bEnd <= aEnd): ans += 1
    if (aStart >= bStart and aStart <= bEnd) or (bStart >= aStart and bStart <= aEnd): ansB += 1


print(ans)
print(ansB)