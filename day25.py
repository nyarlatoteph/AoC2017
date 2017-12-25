steps = 12861455
state = 'A'
ones = set()
position = 0

def write(value):
    if value == 1:
        ones.add(position)
    elif position in ones:
        ones.remove(position)

state_map = {
    'A': { 0: (1, 1, 'B'), 1: (0, -1, 'B') },
    'B': { 0: (1, -1, 'C'), 1: (0, 1, 'E') },
    'C': { 0: (1, 1, 'E'), 1: (0, -1, 'D') },
    'D': { 0: (1, -1, 'A'), 1: (1, -1, 'A') },
    'E': { 0: (0, 1, 'A'), 1: (0, 1, 'F') },
    'F': { 0: (1, 1, 'E'), 1: (1, 1, 'A') }
}

# state_map = {
#     'A': { 0: (1, 1, 'B'), 1: (0, -1, 'B') },
#     'B': { 0: (1, -1, 'A'), 1: (1, 1, 'A') }
# }
# steps = 6

for step in range(steps):
    program = state_map[state]
    current_value = 1 if position in ones else 0
    next = program[current_value]
    write(next[0])
    position += next[1]
    state = next[2]

# print(ones)
print(len(ones))