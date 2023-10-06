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

values[1] = 12
values[2] = 2

# program
for i, val in enumerate(values):
    if (i%4 == 0):
        match val:
            case 1:
                addFunc(values,values[i+1],values[i+2],values[i+3])
            case 2:
                multiply(values,values[i+1],values[i+2],values[i+3])
            case 99:
                break;
            case _:
                print("default")
    else:
        continue

print(values[0])
