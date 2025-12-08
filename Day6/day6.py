#!/usr/bin/env python3


fd = open('input.txt', 'r')
lines = fd.readlines()
lines = [line.strip() for line in lines]
fd.close()

# get the number of rows
number_of_rows = len(lines)

print(f"Number of rows: {number_of_rows}")

# first three lines has numbers seperated by spaces but can be up to 4 spaces
number_lines = []
operators = []
for row in lines:
    if '*' not in row and '+' not in row:
        number_lines.append(row)
    else:
        break
operators = [str(x) for x in lines[-1].split()]

for entry in number_lines:
    print(f"This entry is {len(entry.split())} numbers long.")
print(f"operators is {len(operators)} numbers long.")

# split each number line into a list of numbers
number_lists = []
for entry in number_lines:
    number_lists.append([int(x) for x in entry.split()])
print(number_lists)

part_1_total = 0

for column_idx in range(0, len(number_lists[0])):
    n_list = []
    operator = operators[column_idx]
    if operator == '*':
        result = 1
        for row_idx in range(0, len(number_lists)):
            n_list.append(number_lists[row_idx][column_idx])
            result = result * number_lists[row_idx][column_idx]
        print(f"Column {column_idx} with numbers {n_list} using operator {operator} gives result {result}")
        part_1_total = part_1_total + result
    elif operator == '+':
        result = 0
        for row_idx in range(0, len(number_lists)):
            n_list.append(number_lists[row_idx][column_idx])
            result = result + number_lists[row_idx][column_idx]
        print(f"Column {column_idx} with numbers {n_list} using operator {operator} gives result {result}")
        part_1_total = part_1_total + result

print(f"Part 1 total is {part_1_total}")

# now we need to do part 2, where each single ascii character is a column
# in the below example, we add up each digit in the column
# 123
#  56
#   9
# +
# would be 1 = 1, 2+5=7, 3+6+9=18
part_2_total = 0


fd = open('input.txt', 'r')
lines = fd.readlines()
lines = [line.rstrip('\n') for line in lines]
fd.close()

line_length_of_idx_zero = len(lines[0])
number_of_rows = len(lines) - 1  # last line is operators

#print("lines are {} long".format(line_length_of_idx_zero))
#print(f"There are {number_of_rows} rows of numbers")

problems = []

for column_idx in range(0, line_length_of_idx_zero):
    # only work our the numbers, place them into a list for processing after.
    column_problem = []
    for row_index in range(0, number_of_rows):
        if lines[row_index][column_idx] != ' ':
            column_problem.append(int(lines[row_index][column_idx]))
    problems.append(column_problem)
print(problems)
# just to make follow on processing work.
problems.append([])
    
do_operator = False
work_out = []
operator_in_use = 0
result = 0
part_2_total = 0
for idx,problem in enumerate(problems):
    if problem != []:
        #for e in problem:
            #print(f"Problem entry is {e}")
        work_out.append(problem)
    else:
        # now workout the problem
        # using operators, take the first one, then remove it.
        operator = operators[operator_in_use]
        operator_in_use += 1
        print(work_out, operator)
        # using the work out list, we need to do the problems in reverse
        # so use the last index first, then the next to last.
        
        final_list = []
        
        for prob in reversed(work_out):
            if operator == '+':
                S = ""
                for entry in prob:
                    S = S + str(entry)
                S_int = int(S)
                final_list.append(S_int)
            elif operator == '*':
                S = ""
                for entry in prob:
                    S = S + str(entry)
                S_int = int(S)
                final_list.append(S_int)
        result = 0
        print(final_list)
        for idx,e in enumerate(final_list):
            if operator == '+':
                if idx == 0:
                    result = e
                else:
                    result = result + e
            elif operator == '*':
                if idx == 0:
                    result = e  
                else:
                    result = result * e
        print(f"result {result}")
        part_2_total += result
        result = 0
        work_out = []
print(part_2_total)

        
