import re

def find_start(maze):
    return (maze[0].find('|'), 0)

def is_letter(char):
    m = re.match("\w", char)
    return m is not None


maze = []
# with open('test19.txt') as f:
with open('input19.txt') as f:
    for line in f.readlines():
        maze.append(line)

(x, y) = find_start(maze)
letters = ''
x_dir = 0
y_dir = 1
steps = 0
while True:
    char = maze[y][x]
    if char == '+':
        if y_dir != 0:
            y_dir = 0
            if x > 0 and maze[y][x-1] != ' ':
                x_dir = -1
            else:
                x_dir = 1
        else:
            x_dir = 0
            if y > 0 and maze[y-1][x] != ' ':
                y_dir = -1
            else:
                y_dir = 1

    elif is_letter(char):
        letters += char
    elif char != '-' and char != '|':
        break

    x += x_dir
    y += y_dir
    steps += 1

print(letters, steps)