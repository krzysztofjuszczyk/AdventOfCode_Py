with open('./inputs/d5.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry for entry in lines]

crate_lines = lines[:lines.index('\n')-1]
moving_lines = lines[lines.index('\n')+1:]