lines = open("inputs/2020_d1.txt", "r").readlines()
parsedLines = [int(l) for l in lines]

sum = 2020
ans = 0
list = []
# partA
# for l in lines:
#     current = int(l)
#     searchingFor = sum - current
#     if searchingFor in list:
#         print(current)
#         print(searchingFor)
#         print (current*searchingFor)
#     else:
#         list.append(current)

for l1 in parsedLines:
    for l2 in parsedLines:
        for l3 in parsedLines:
            if l1+l2+l3 == sum:
                print(l1)
                print(l2)
                print(l3)
                print(l1*l2*l3)


    # current = int(l)
    # searchingFor2sum = sum - current
    # for l2 in lines:
    #     current2 = int(l)
    #     if current==current2: continue
    #     else:
    #         searchingIn2ndLoop = searchingFor2sum - current2
    #         if searchingIn2ndLoop in list:
    #             print(current)
    #             print(current2)
    #             print(searchingIn2ndLoop)
    #             print(current*current2*searchingIn2ndLoop)
    #         else:
    #             list.append(current2)
    # list.append(current)