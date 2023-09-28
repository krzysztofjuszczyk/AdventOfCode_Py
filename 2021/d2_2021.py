lines = open('./inputs/d2.txt', 'r').readlines()
horizontal = 0
depth = 0
for l in lines:
    cmd = l.split(' ')
    command = cmd[0]
    steps = int(cmd[1])
    if command == 'forward': horizontal += steps
    elif command == 'down': depth += steps
    else: depth-= steps

print(horizontal*depth)

# part B
aim = 0
horizontal = 0
depth = 0
for l in lines:
    cmd = l.split(' ')
    command = cmd[0]
    steps = int(cmd[1])
    if command == 'forward':
        horizontal += steps
        depth += (steps*aim)
    elif command == 'down': aim += steps
    else: aim -= steps

print(horizontal*depth)