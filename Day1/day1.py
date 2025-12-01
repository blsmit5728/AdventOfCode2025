#!/usr/bin/env python3

def read_file(filename):
    fd = open(filename, "r")
    lines = fd.readlines()
    for index, line in enumerate(lines):
        lines[index] = line.strip()
    fd.close()
    return lines

def main():
    starting_point = 50
    current_position = starting_point
    min = 0
    max = 99
    lines = read_file("input.txt")
    part1_total = 0
    part2_total = 0
    direction = ''
    number_of_clicks = 0
    prev_position = starting_point
    print(f"Starting point: {starting_point}")
    for idx, line in enumerate(lines):
        prev_position = current_position
        if 'L' in line:
            direction = 'L'
            line = line.replace('L', '')
        elif 'R' in line:
            direction = 'R'
            line = line.replace('R', '')
        number_of_clicks = int(line)
        print(f"Moving {direction} by {number_of_clicks} clicks from {current_position}")
        if direction == 'R':
            current_position = prev_position + number_of_clicks
            # any time the dial PASSES 100
            part2_total += current_position // 100 - prev_position // 100
        elif direction == 'L':
            current_position = prev_position - number_of_clicks
            # any time the dial PASSES 100 
            part2_total += (prev_position-1) // 100 - (current_position-1) // 100
        if current_position % 100 == 0:
            part1_total += 1
        print(f"Current position [{idx}]: {current_position} -- {line}")
        #if current_position == 0:
        #    total += 1
        # input()
    print(f"Total sum: {part1_total}")
    print(f"Total sum part 2: {part2_total}")
    
if __name__ == "__main__":
    main()