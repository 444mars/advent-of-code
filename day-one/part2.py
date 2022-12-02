import os

input_file = open("input.txt", "r")

max_elf = 0
curr_elf = 0
num = 0
all_elfs = []

for line in input_file:
    if(line == "\n"):
        all_elfs.append(curr_elf)
        curr_elf = 0
    else:
        num = int(line)
        curr_elf += num

all_elfs.sort(reverse=True)

print("The First elf has", all_elfs[0], "calories")
print("The Second elf has", all_elfs[1], "calories")
print("The Third elf has", all_elfs[2], "calories")

print("The total of all three is", all_elfs[0] + all_elfs[1] + all_elfs[2])