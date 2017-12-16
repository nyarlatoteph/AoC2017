"""
Sprial memory

 65  64  63  62  61  60  59  58  57
 66  37  36  35  34  33  32  31  56 
 67  38  17  16  15  14  13  30  55
 68  39  18   5   4   3  12  29  54
 69  40  19   6   1   2  11  28  53
 70  41  20   7   8   9  10  27  52
 71  42  21  22  23  24  25  26  51
 72  43  44  45  46  47  48  49  50
 73  74  75  76  77  78  79  80  81 ->

right
 1,2,11,28,53,86,127
 dx 1,9,17,25,33,41
 ddx 8,8,8,8 etc

left
 1,6,19,40,69
 dx 5,13,21,29
 ddx 8,8,8

down
 1,8,23,46,77
 dx 7,15,23,31
 ddx 8,8,8

up
 1,4,15,34,61
 dx 3,11,19,27
 ddx 8,8,8

diag
1,9,25,49,81
dx 8,16,24,32
ddx 8,8,8

       a
       .
 d ... O ... b
       .
       c     d
. = n squares

        n
d = 1 + E (p-1)*8
       p=1 
"""


def calcsum(n, offset):
    if n == 0:
        return 1
    r = [offset + 8*(p-1) for p in range(1, n+1)]
    return 1+sum(r)

def calcpos(x, y):
    n = max(abs(x), abs(y))
    a = calcsum(n, 1)
    b = calcsum(n, 2)
    c = calcsum(n, 3)
    d = calcsum(n, 4)
    e = calcsum(n, 5)
    f = calcsum(n, 6)
    g = calcsum(n, 7)
    h = calcsum(n, 8)
    
    # determine which quadrant
    if x >= 0:
        if y >= 0:
            # qa, qb, c or b
            if x == 0:
                return c
            elif y == x:
                return b
            elif y < x:
                return a + y
            else:
                return c - x
        else:
            # g, h, qg or qh
            if x == 0:
                return g
            elif x == -y:
                return h
            elif x < -y:
                return g + x
            else:
                return a + y
    else:
        if y >= 0:
            # qc, qd, d or e
            if y == 0:
                return e
            elif y == -x:
                return d
            elif y < -x:
                return e - y
            else:
                return c - x
        else:
            # qe, qf or f
            if x == y:
                return f
            elif y > x:
                return e - y
            else:
                return g + x

def printer(r):
    for y in range(-r, r+1):
        for x in range(-r, r+1):
            print(calcpos(x, -y), end='\t')
        print(end='\n')


def finder(target):
    for y in range(-r, r+1):
        for x in range(-r, r+1):
            if calcpos(x, -y) == target:
                print (x, y)
                return (abs(x) + abs(y))

r = 275

# print(finder(1))
# print(finder(12))
# print(finder(23))
# print(finder(1024))
# print(finder(265149))


N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
next = {N: W, W: S, S: E, E: N} # old -> new direction

def spiral(width, height, target):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 # start near the center
    dx, dy = S # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    matrix[y][x] = 1
    result = None

    def sum_adjacent(x, y):
        def c(x, y):
            return 0 if x < 0 or y < 0 or x >= width or y >= height or matrix[y][x] is None else matrix[y][x]
        return c(x+1, y) + c(x-1, y) + c(x, y-1) + c(x, y+1) + c(x-1, y-1) + c(x-1, y+1) + c(x+1, y-1) + c(x+1, y+1)

    while True:
        count += 1
        if count > 1:
            matrix[y][x] = sum_adjacent(x, y) # visit

        if matrix[y][x] > target and result is None:
            result = matrix[y][x]

        # try to turn right
        new_dx, new_dy = next[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return (matrix, result) # nowhere to go

def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))


(matrix, target) = spiral(100, 100, 265149)
print (target)