map = []
with open('input22.txt') as f:
    for line in f.readlines():
        map.append(line.rstrip())


# map = [ "..#", "#..", "..." ]

infections = []
h = len(map)
w = len(map[0])
O = (int(w/2), int(h/2))
for y in range(h):
    for x in range(w):
        if map[y][x] == '#':
            infections.append((x-O[0], y-O[1]))

direction = (0, -1)
current_node = (0, 0)
caused_infections = 0
for _ in range(10000):
    if current_node in infections:
        direction = (-direction[1], direction[0])
    else:
        direction = (direction[1], -direction[0])

    if current_node in infections:
        infections.remove(current_node)
    else:
        infections.append(current_node)
        caused_infections += 1

    current_node = (current_node[0] + direction[0], current_node[1] + direction[1])

print(caused_infections)