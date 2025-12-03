#!/usr/bin/env python3

fd = open("input.txt", "r")
lines = fd.readlines()
lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines
fd.close()

total_part_1 = 0

for line in lines:
    # seperate the line into digits
    digits = [int(char) for char in line]
    # find the maximum number I can create with only 2 of these digits
    # I cannot rearrange the digits
    # try every combonation of 2 digits from the list
    max_number = -1
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            digit1 = digits[i]
            digit2 = digits[j]
            # create a new number as digit1digit2 as a string
            new_number_str = str(digit1) + str(digit2)
            new_number = int(new_number_str)
            if new_number > max_number:
                max_number = new_number
    total_part_1 += max_number
    print(f"Line: {line} => Max Number with 2 digits: {max_number}")
total_part_2 = 0
    
print(f"Total Part 1: {total_part_1}")

def find_joltage(banks, needed_bats):
    joltage = 0
    for bank in banks:
        need_to_remove = len(bank) - needed_bats
        while need_to_remove > 0:
            for i in range(len(bank) - 1):
                if bank[i] < bank[i+1]:
                    bank = bank[:i] + bank[i+1:]
                    break
            need_to_remove -= 1
        joltage += int(bank[:needed_bats])
    return joltage

print(f"Total Part 2: {find_joltage(lines, 12)}")