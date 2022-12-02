import os

input_file = open("input.txt", "r")

max_elf = 0
curr_elf = 0
num = 0
elf_number = 1

for line in input_file:
    if(line == "\n"):
        max_elf = max(max_elf, curr_elf)
        curr_elf = 0
    else:
        num = int(line)
        curr_elf += num

print("the max number of calories being help is", max_elf)