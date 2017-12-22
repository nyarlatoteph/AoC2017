map = []
with open('input22.txt') as f:
    for line in f.readlines():
        map.append(line.rstrip())


# map = [ "..#", "#..", "..." ]

infections = {}
h = len(map)
w = len(map[0])
O = (int(w/2), int(h/2))
for y in range(h):
    for x in range(w):
        if map[y][x] == '#':
            infections[((x-O[0], y-O[1]))] = '#'

direction = (0, -1)
current_node = (0, 0)
caused_infections = 0
for _ in range(10000000):
    if current_node in infections:
        if infections[current_node] == '#':
            direction = (-direction[1], direction[0]) # right
        elif infections[current_node] == 'F':
            direction = (-direction[0], -direction[1]) # reverse
        else: 
            pass # weakened, don't adjust direction
    else:
        direction = (direction[1], -direction[0]) # left

    if current_node in infections:
        if infections[current_node] == 'W':
            infections[current_node] = '#'
            caused_infections += 1
        elif infections[current_node] == '#':
            infections[current_node] = 'F'
        elif infections[current_node] == 'F':
            infections.pop(current_node)
    else:
        infections[current_node] = 'W'

    current_node = (current_node[0] + direction[0], current_node[1] + direction[1])

print(caused_infections)