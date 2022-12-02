import os

input_file = open("input.txt", "r")

max_elf = 0
curr_elf = 0
num = 0
elf_number = 1

for line in input_file:
    if(line == "\n"):
        print("There is a new line starting a new elf count")
        max_elf = max(max_elf, curr_elf)
        curr_elf = 0
    else:
        num = int(line)
        print("the curr line is:", num)
        curr_elf += num

print("the max number of calories being help is", max_elf)