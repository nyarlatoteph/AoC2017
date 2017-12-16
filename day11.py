import math

def distance(x, y, z):
    return max(abs(x), abs(y), abs(z))

def count(input):
    steps = input.split(',')

    x = 0
    y = 0
    z = 0
    max_distance = 0

    for step in steps:
        if step == "sw":
            x -= 1
            z += 1
        elif step == "se":
            x += 1
            y -= 1
        elif step == "ne":
            x += 1
            z -= 1
        elif step == "nw":
            x -= 1
            y += 1
        elif step == "s":
            y -= 1
            z += 1
        elif step == "n":
            y += 1
            z -= 1
        if distance(x, y, z) > max_distance:
            max_distance = distance(x, y, z)
    
    return (distance(x, y, z), max_distance)


with open('input11.txt') as f:
    for line in f.readlines():
        line = line.rstrip()

assert count("ne,ne,ne")[0] == 3
assert count("ne,ne,sw,sw")[0] == 0
assert count("ne,se,ne,se")[0] == 4
assert count("ne,ne,s,s")[0] == 2
assert count("se,sw,se,sw,sw")[0] == 3
assert count("n,sw,s,se,ne,n,nw,s")[0] == 0
assert count("nw,n,n,se,ne,ne,ne,s,s,se,se,se")[0] == 6

print(count(line))

