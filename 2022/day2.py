input = open('./inputs/d2.txt').readlines()
results = [ 'A Y', 'B Z', 'C X', #win  /
            'A X', 'B Y', 'C Z', #draw
            'A Z', 'B X', 'C Y' #loss
        ]

scoreA = [8, 9, 7,
          4, 5, 6,
          3, 1, 2]
scoreB = [ 4,   9,  2,
            3,  5 , 7,
            8,  1,  6
]
myscoreA = 0
myScoreB = 0

# part A
for line in input:
    index = results.index(line.strip())
    myscoreA += scoreA[index]
    myScoreB += scoreB[index]

print(myscoreA)
print(myScoreB)