lines = open('../inputs/2022_d3.txt').readlines()
ans = 0
for line in lines:
    indexH = len(line)//2
    firstHalf = line[:indexH]
    secondHalf = line[indexH:]
    common_items_set = set(firstHalf).intersection(secondHalf)
    common_item = common_items_set.pop()
    ascii_start = 96 if common_item.islower() else 38
    ans += ord(common_item) - ascii_start

print('part A: '+ str(ans))

lines2 = open('../inputs/2022_d3.txt', 'r').read().splitlines()
ans2 = 0
groups = [[lines2[i], lines2[i + 1], lines2[i + 2]] for i, _ in enumerate(lines2[:-2]) if i % 3 == 0]
for group in groups:
    common_items_set = set(group[0]).intersection(group[1], group[2])
    common_item = common_items_set.pop()
    ascii_start = 96 if common_item.islower() else 38
    ans2 += ord(common_item) - ascii_start
print("Task 2 result: " + str(ans2))