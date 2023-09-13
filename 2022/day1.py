# day 1
input = open('./inputs/d1.txt').readlines()
max = 0
currentElf = 0
allElves = []
for i in input:
    if i != '\n':
        currentElf += int(i)
    else:
        max = currentElf if currentElf > max else max
        allElves.append(currentElf)
        currentElf = 0

print(max)
allElves.sort(reverse=True)
print(allElves)
print(allElves[0]+allElves[1]+allElves[2])


# input = [[int(si) for si in s.split('\n')] for s in ''.join(input).split('\n\n')]