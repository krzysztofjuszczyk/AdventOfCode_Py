lines = open("../inputs/2020_d2.txt", "r").readlines()
ans = 0
ansB = 0
for l in lines:
    cmds = l.split(" ")
    min  = int(cmds[0].split("-")[0])
    max = int(cmds[0].split("-")[1])
    letter = cmds[1][0]
    code = cmds[2]
    # print(min)
    # print(max)
    # print(letter)
    # print(code)
    count = code.count(letter)
    if min <= count <= max:
        ans += 1

    if code[min-1] == letter and code [max-1] != letter:
        ansB += 1
    if code[min-1] != letter and code [max-1] == letter:
        ansB += 1

print(ans)
print(ansB)
