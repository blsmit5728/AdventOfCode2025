#!/usr/bin/env python3

fd = open('example.txt', 'r')
lines = fd.readlines()
# strip \n
lines = [line.strip() for line in lines]
lines = [list(line) for line in lines]
fd.close()

diagram = lines
width, height = len(diagram[0]), len(diagram)

def part_1(diagram) -> int:
    beam_idxs = {diagram[0].index('S')}
    split_count = 0
    for i in range(1, height):
        current_beam_idxs = list(beam_idxs)
        line = diagram[i]
        for b in current_beam_idxs:
            if line[b] == "^":
                split_count += 1
                beam_idxs.remove(b)
                left = b - 1
                right = b + 1
                if left >= 0:
                    beam_idxs.add(left)
                if right < width:
                    beam_idxs.add(right)
    return split_count

print(part_1(diagram))