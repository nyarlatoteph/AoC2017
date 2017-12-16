def swap(programs, pos1, pos2):
    pos1, pos2 = min(pos1, pos2), max(pos1, pos2)
    a = programs[pos1]
    b = programs[pos2]
    return programs[0:pos1] + b + programs[pos1+1:pos2] + a + programs[pos2+1:]

def perform(dance, programs):
    for move in dance:
        if move[0] == 's':
            amount = int(move[1:])
            programs = programs[-amount:] + programs[0:len(programs)-amount]
        elif move[0] == 'x':
            a, b = move[1:].split('/')
            programs = swap(programs, int(a), int(b))
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            pos1 = programs.find(a)
            pos2 = programs.find(b)
            programs = swap(programs, pos1, pos2)

    return programs

programs = 'abcdefghijklmnop'
assert len(programs) == 16

dance = []
with open('input16.txt') as f:
    for line in f.readlines():
        dance += line.split(',')

# dance = [ 's1', 'x3/4', 'pe/b' ]
# programs = 'abcde'

results = []
times = 1

while not (programs in results):
    results.append(programs)
    programs = perform(dance, programs)
    times += 1

repeat_start = results.index(programs)
repeat_loop = len(results)-repeat_start

print(repeat_start, repeat_loop)
mod = 1000000000 % len(results)
print(results[mod])