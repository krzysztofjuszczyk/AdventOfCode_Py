lines = open('../inputs/2021_d3.txt', 'r').readlines()

# initialize empty strings
gamma, epsilon = '', ''

for i in range (12):
    count1, count0 = 0, 0
    for l in lines:
        if l[i] == '1': count1 += 1
        else: count0 += 1
    if count1>count0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
    print(gamma)
    print(epsilon)

ans = int(gamma,2)*int(epsilon,2)
print(ans)