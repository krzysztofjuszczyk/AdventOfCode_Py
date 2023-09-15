lines = open('./inputs/d3.txt').readlines()
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
