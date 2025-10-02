def check_all_increasing(line):
    for i in range(1,len(line)):
        diff = int(line[i]) - int (line[i-1])
        if not (0 < diff <=3):
            return False
    return True

def check_all_decreasing(line):
    for i in range(1,len(line)):
        diff = int(line[i]) - int (line[i-1])
        if not (-3 <= diff <0):
            return False
    return True

lines = open('./inputs/2024_d2.txt').readlines()
res = 0
for l in lines:
    line = l.strip().split(' ')
    # print (line)
    if int(line[1]) > int(line[0]):   # just look at first two to guess direction
        if check_all_increasing(line):
            res += 1
    else:
        if check_all_decreasing(line):
            res += 1
    # print(res)

## part 2
## we can remove 1 element from list
res2 = 0
for l in lines:
    line = l.strip().split(' ')
    if check_all_increasing(line) or check_all_decreasing(line):
        res2 += 1
    else:
        if check_all_increasing(line):
            res2 += 1
        else:
            for i in range (len(line)):
                modified_line = line[:i]+line[i+1:]
                if check_all_increasing(modified_line) or check_all_decreasing(modified_line):
                    res2 += 1
                    break
print(res2)

