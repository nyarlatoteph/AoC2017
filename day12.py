import re

def connected(programs, program):
    result = set([program])
    if program in programs:
        check_programs = programs.pop(program)    
        for p in check_programs:
            result.update(connected(programs, p))

    return result
        


programs = {}

with open('input12.txt') as f:
# with open('test12.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        p = re.compile(r'(\d+)\s*<->\s*([\d,\s]+)')
        m = re.match(p, line)
        if m is None:
            print("Unmatched line: ", line)
            break
        source_program = int(m.groups()[0])
        target_programs = [int(program.strip()) for program in m.groups()[1].split(',')]
        programs[source_program] = target_programs
        # print(source_program, target_programs)

connected_to_zero = connected(dict(programs), 0)
print(len(connected_to_zero))

groups = []
for program in programs:
    connected_group = connected(dict(programs), program)
    if connected_group not in groups:
        groups.append(connected_group)

print(len(groups))