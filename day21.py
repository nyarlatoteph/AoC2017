import math


def pattern_size(pattern):
    return pattern.count('/')+1

def find_rule(rules, pattern):
    for (rule_in, rule_out) in rules.items():
        rf = rotate_flip_combinations(pattern)
        if rule_in in rf:
            return rule_out

    return None

def split(pattern, size):
    result = []
    lines = pattern.split('/')
    for y in range(int(len(lines)/size)):
        for x in range(int(len(lines[y])/size)):
            part = []
            for y2 in range(size):
                part.append(lines[y*size+y2][x*size:(x+1)*size])
            result.append('/'.join(part))

    return result

def rotate_flip_combinations(pattern):
    def flip(pattern, horizontal):
        p = pattern.split('/')
        if horizontal:
            return '/'.join([line[::-1] for line in p])
        return '/'.join(p[::-1])

    def rotate(pattern, clockwise):
        def r(p):
            return [''.join(l) for l in list(zip(*p[::-1]))]

        p = pattern.split('/')
        if clockwise:
            return '/'.join(r(p))
        return '/'.join(r(r(r(p))))

    return [pattern, rotate(pattern, False), rotate(pattern, True), flip(pattern, False), flip(pattern, True), flip(flip(pattern, True), False), \
            rotate(flip(pattern, True), True), rotate(flip(pattern, True), False)]

def combine(parts):
    pattern = [] 
    size = int(math.sqrt(len(parts)))
    for y in range(size):
        for y2 in range(pattern_size(parts[y])):
            line = ''
            for x in range(size):
                line += parts[y*size + x].split('/')[y2]
            pattern.append(line)

    return '/'.join(pattern)


def iterate(pattern, rules):
    replacements = []
    breakup_size = 2 if (pattern_size(pattern)%2 == 0) else 3
    
    for piece in split(pattern, breakup_size):
        replacement = find_rule(rules, piece)
        if replacement is None:
            print('Could not match pattern!', piece)
        else:
            replacements.append(replacement)

    return combine(replacements)

rules = {}
with open('input21.txt') as f:
    for line in f.readlines():
        (a, b) = line.rstrip().split(" => ")
        rules[a] = b

# rules = { "../.#": "##./#../...", ".#./..#/###": "#..#/..../..../#..#" }
pattern = ".#./..#/###"

for n in range(18):
    print('Iteration', n)
    pattern = iterate(pattern, rules)
    print(pattern.replace('/', '\n'), '\n')

print(pattern.count('#'))
