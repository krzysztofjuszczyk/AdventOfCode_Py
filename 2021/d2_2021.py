lines = open('./inputs/d2.txt', 'r').readlines()
horizontal = 0
depth = 0
ans = 0
for l in lines:
    cmd = l.split(' ')
    command = cmd[0]
    steps = int(cmd[1])
    if command == 'forward': horizontal += steps
    elif command == 'down': depth += steps
    else: depth-= steps

print(horizontal*depth)

