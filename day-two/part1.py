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

for line in input_file:
    if line[0] == 'A': # this means that the opponent chose Rock
        if line[2] == 'X': # you chose rock (draw)
            total += 4
        if line[2] == 'Y': # you chose paper (win)
            total += 8
        if line[2] == 'Z': # you chose scissors (tie)
            total += 3
    elif line[0] == 'B': # this means the opponent chose Paper
        if line[2] == 'X': # you chose rock (loss)
            total += 1
        if line[2] == 'Y': # you chose paper (draw)
            total += 5
        if line[2] == 'Z': # you chose scissors (win)
            total += 9
    elif line[0] == 'C': # this means the opponent chose Scissors
        if line[2] == 'X': # you chose rock (win)
            total += 7
        if line[2] == 'Y': # you chose paper (loss)
            total += 2
        if line[2] == 'Z': # you chose scissors (tie)
            total += 6

print(total)