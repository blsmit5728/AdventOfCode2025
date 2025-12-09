#!/usr/bin/env python3

from math import dist, prod

fd = open("input.txt", "r")
lines = fd.readlines()
lines = [line.strip() for line in lines]
fd.close()

data = [tuple(int(num) for num in line.split(",")) for line in lines]

def part1(data:list, steps:int=1000) -> int:
    connections = []
    for index, junction_box in enumerate(data[:-1], 1):
        connections.extend( (dist(junction_box, item), {junction_box, item}) for item in data[index:] )
    # get the first 1000
    connections = sorted(connections)[:steps]
    circuits = []
    for _, pair in connections:
        circuit_ids = [idx for idx,circ in enumerate(circuits) if circ & pair]
        if circuit_ids == 1:
            circuits[circuit_ids[0]] |= pair
        elif circuit_ids:
            circuits = [circ for idx,circ in enumerate(circuits) if idx not in circuit_ids] + [pair.union(*[circuits[idx] for idx in circuit_ids])]
        else:
            circuits.append(pair)
        if len(circuits) == 1 and len(circuits[0]) == len(data):
            return prod(item[0] for item in pair)
    return prod(sorted(len(circ) for circ in circuits)[-3:])

print("part1: {}".format(part1(data)))
        
def part2(data: list) -> int:
   return part1(data, len(data)*(len(data)-1)//2)

print("part2: {}".format(part2(data)))