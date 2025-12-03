#!/usr/bin/env python3

import re

REPEATED = re.compile(r'^(..*?)\1{1,}$')

fd = open("input.txt", "r")
lines = fd.readlines()
lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines
fd.close()
ranges = lines[0].split(",")

total = 0
total_part2 = 0

for entry in ranges:
    start, end = map(int, entry.split("-"))
    for i in range(start, end + 1):
        str_i = str(i)
        if len(str_i) % 2 == 0:
            #print(f"{str_i} is even digits")
            # cut the str in half and compare
            mid = len(str_i) // 2
            first_half = str_i[:mid]
            second_half = str_i[mid:]
            if first_half == second_half:
                # print(f"{str_i} is a palindrome")
                total += i
        else:
            pass
        # now check for any repeated patterns
        if REPEATED.search(str_i):
            total_part2 += i    
print(f"Total: {total}")
print(f"Total Part 2: {total_part2}")

