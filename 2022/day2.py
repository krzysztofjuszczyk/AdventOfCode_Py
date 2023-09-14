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

for line in input:
    index = results.index(line.strip())
    myscoreA += scoreA[index]
    myScoreB += scoreB[index]

print(myscoreA)
print(myScoreB)

# prettier solution

map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
map_inputB = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}

with open('./inputs/d2.txt', 'r') as file:
    lines = file.readlines()
    l = [entry.strip() for entry in lines]



def getPointsA(str):
    opponent_shape = map_input[str[0]]
    our_shape = map_input[str[2]]

    if opponent_shape == our_shape:
        return points_per_outcome['Draw'] + points_per_shape[our_shape]
    elif (opponent_shape, our_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        return points_per_outcome['Lose'] + points_per_shape[our_shape]
    else:
        return points_per_outcome['Win'] + points_per_shape[our_shape]

def getPointsB(str):
    opponent_shape = map_inputB[str[0]]
    expected_result = map_inputB[str[2]]

    if expected_result == 'Lose':
        if (opponent_shape == 'Rock'): our_shape = 'Scissors'
        elif (opponent_shape == 'Paper'): our_shape = 'Rock'
        else: our_shape = 'Paper'
        return 0 +points_per_shape[our_shape]
    elif expected_result == 'Draw':
        return 3 + points_per_shape[opponent_shape]
    else:   #Win
        if (opponent_shape == 'Rock'): our_shape = 'Paper'
        elif (opponent_shape == 'Paper'): our_shape = 'Scissors'
        else: our_shape = 'Rock'
        return 6 + points_per_shape[our_shape]

print(sum([getPointsA(str) for str in l]))
print(sum([getPointsB(str) for str in l]))
