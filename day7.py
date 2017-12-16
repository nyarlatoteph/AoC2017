import re
from functools import reduce

def children(program):
    return [child for (child, parent) in parents.items() if program == parent]

def calc_weight(program):
    weight = int(weights[program])
    for child in children(program):
        weight += calc_weight(child)
    return weight

def is_balanced(program):
    cc = children(program)
    weight = calc_weight(cc[0])
    for child in children(program):
        if calc_weight(child) != weight:
            return False
    return True

def find_wrong_weight(program):
    if not is_balanced(program):
        return program
    for child in children(program):
        if not is_balanced(child):
            if len(children(child)) > 0:
                return find_wrong_weight(child)
            return child

    return None


parents = dict()
weights = dict()

# with open('test2.txt') as f:
with open('input7.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        p = re.compile('([a-z]+)\s+\((\d+)\)(?:\s+->\s+([a-z,\s]+))?')
        m = re.match(p, line)
        if not m:
            print('Unmatched line: ', line)
            break

        parent = m.group(1)
        weight = m.group(2)
        above_list = m.group(3).split(', ') if m.group(3) else []
        
        weights[parent] = weight
        if len(above_list) > 0:
            for program in above_list:
                parents[program] = parent

top_program = program
while top_program in parents:
    top_program = parents[top_program]

print(top_program)

# print(children('ugml'))
# print(calc_weight('ugml'))
# print(calc_weight('padx'))
# print(calc_weight('fwft'))

p = find_wrong_weight(top_program)
p = 'orflty'
for c in children(p):
    print(c, weights[c], calc_weight(c))

