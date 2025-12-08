#!/usr/bin/python3

def parse_input(filename):
    fd = open(filename, 'r')
    lines =  fd.readlines()
    # clean the \n
    lines = [line.strip() for line in lines]
    fd.close()
    ranges_list = []
    id_list = []
    for line in lines:
        if '-' in line:
            # its a range, make it a tuple by splitting the - and making each an int
            start, end = line.split('-')
            ranges_list.append((int(start), int(end)))
        elif line == '':
            pass
        else:
            # its an id, make it an int
            id_list.append(int(line))
    return ranges_list, id_list

def check_if_id_in_any_range(ranges, id):
    for r in ranges:
        if r[0] <= id <= r[1]:
            return True
    return False

def get_total_fresh_ids_from_a_range(my_range, current_fresh_ids):
    fresh_ids = -1
    start = my_range[0]
    stop = my_range[1]
    print(current_fresh_ids)
    
    append_to_list = []

    for i in range(start, stop+1, 1):
        if i in current_fresh_ids:
            print(f"{i} already in ids")
        else:
            fresh_ids += 1
            append_to_list.append(i)
    return fresh_ids, append_to_list

#print(parse_input('example.txt'))
ranges, ids = parse_input('input.txt')
fresh_foods = 0
for id in ids:
    if check_if_id_in_any_range(ranges, id):
        fresh_foods += 1
        # print(f'ID {id} is in a range')
print(f"Fresh ingredients = {fresh_foods}")
total = -1

from typing import List, Tuple

def count_unique_values_in_ranges(ranges: List[Tuple[int, int]]) -> int:
    """
    ranges: list of (start, end) integer pairs, inclusive.
    Returns the number of unique integer values covered by all ranges.
    """
    if not ranges:
        return 0

    # Normalize so start <= end for each range
    normalized = [(min(a, b), max(a, b)) for (a, b) in ranges]

    # Sort by start
    normalized.sort(key=lambda r: r[0])

    total = 0
    cur_start, cur_end = normalized[0]

    for start, end in normalized[1:]:
        if start <= cur_end + 1:
            # Overlaps or touches current interval -> merge
            cur_end = max(cur_end, end)
        else:
            # Gap: close previous interval and start a new one
            total += cur_end - cur_start + 1
            cur_start, cur_end = start, end

    # Add the final interval
    total += cur_end - cur_start + 1

    return total

print(count_unique_values_in_ranges(ranges))