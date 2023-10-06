line = open("./inputs/2019_d2.txt","r").readline()
ans = 0
values = []

#code 1
def addFunc(array, x,y,to):
    array[to] = array[x]+ array[y]
    return array

#code 2
def multiply(array, x,y,to):
    array[to] = array[x] * array[y]
    return array

#code 99
#end

lines = line.split(",")
for i,l in enumerate(lines):
    values.insert(i,int(l))

originalVals = values.copy()
values[1] = 12
values[2] = 2

# program
def mainProgram(values):
    for i, val in enumerate(values):
        if (i%4 == 0):
            match val:
                case 1:
                    addFunc(values, values[i + 1], values[i + 2], values[i + 3])
                case 2:
                    multiply(values, values[i + 1], values[i + 2], values[i + 3])
                case 99:
                    # print(str(values[0]) + ' RES')
                    break;
                case _:
                    print("default")
        else:
            continue
    return values

print("partA:")
print(mainProgram(values)[0])

# part B
for i in range(99):
    for j in range(99):
        valCopy = originalVals.copy()
        valCopy[1] = i
        valCopy[2] = j
        result = mainProgram(valCopy)[0]
        # print(str(result) + ' ' + str(valCopy[1]) + ' ' + str(valCopy[2]))
        if result == 19690720:
            print(100*valCopy[1] + valCopy[2])
