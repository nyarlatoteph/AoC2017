from day10 import knot_hash2

def count_regions(grid):
    region = 0
    free_regions = set()

    def replace(a, b):
        nonlocal free_regions
        l = min(a, b)
        h = max(a, b)
        for y in range(len(m)):
            for x in range(len(m[y])):
                if m[y][x] == h:
                    m[y][x] = l
        free_regions.add(h)

    def is_region(x, y):
        return x >= 0 and y >= 0 and x < len(m[y]) and y < len(m) and m[y][x] > 0

    def determine_region(x, y):
        nonlocal region
        if is_region(x, y-1):
            return m[y-1][x]
        elif is_region(x-1, y):
            return m[y][x-1]
        elif m[y][x] == 0:
            if len(free_regions) > 0:
                r = min(free_regions)
                free_regions.remove(r)
                return r
            region += 1
            return region
        else:
            return -1

    m = [ [ int(x)-1 for x in y ] for y in grid ]
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == 0:
                m[y][x] = determine_region(x, y)
                # check for connected regions and free one if found
                if x > 0 and m[y][x-1] > 0 and m[y][x-1] != m[y][x]:
                    replace(m[y][x], m[y][x-1])
                if y > 0 and m[y-1][x] > 0 and m[y-1][x] != m[y][x]:
                   replace(m[y-1][x], m[y][x])

    return region

grid = []
input = 'wenycdww'
# input = 'flqrgnkx'
for grid_row in range(128):
    hash = knot_hash2('%s-%d' % (input, grid_row))
    bin_representation = [ bin(int('0x%s' % c, 16))[2:].zfill(4) for c in hash ]
    grid.append(''.join(bin_representation))

print(sum([ b.count('1') for b in grid ]))
print(count_regions(grid))