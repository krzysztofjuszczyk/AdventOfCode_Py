lines = open("inputs/2020_d1.txt", "r").readlines()
sum = 2020
ans = 0
list = []
for l in lines:
    current = int(l)
    searchingFor = sum - current
    if searchingFor in list:
        print(current)
        print(searchingFor)
        print (current*searchingFor)
    else:
        list.append(current)
