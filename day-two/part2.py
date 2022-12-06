import os

input_file = open('input.txt', 'r')
total = 0

# points per selected item
# rock -  1 
# paper - 2
# seissor - 3 
# loss - 0
# win - 6 
# draw - 3 

#example input
# A X
# A is what the opponent chose
# X is is what the result of the match should be 

for line in input_file:
    if line[0] == 'A': # this means that the opponent chose Rock

        if line[2] == 'X': # we want the match to result in a LOSS  
            total += 3
            total += 0
        if line[2] == 'Y': # we want the match to result in a DRAW
            total += 1
            total += 3
        if line[2] == 'Z': # we want the match to result in a WIN
            total += 2
            total += 6

    elif line[0] == 'B': # this means the opponent chose Paper

        if line[2] == 'X': # we want the match to result in a LOSS  
            total += 1
            total += 0
        if line[2] == 'Y': # we want the match to result in a DRAW
            total += 2
            total += 3
        if line[2] == 'Z': # we want the match to result in a WIN
            total += 3
            total += 6
    
    elif line[0] == 'C': # this means the opponent chose Scissors

        if line[2] == 'X': # we want the match to result in a LOSS  
            total += 2
            total += 0
        if line[2] == 'Y': # we want the match to result in a DRAW
            total += 3
            total += 3
        if line[2] == 'Z': # we want the match to result in a WIN
            total += 1
            total += 6
    

print(total)