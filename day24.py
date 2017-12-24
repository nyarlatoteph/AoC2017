def has_endpoint(endpoint, components):
    return [component for component in components if component[0] == endpoint or component[1] == endpoint]

def make_chain(endpoint, components):
    solutions = []
    for component in has_endpoint(endpoint, components):
        comps = list(components)
        comps.remove(component)
        solution = [ [component] ]
        c = list(component)
        c.remove(endpoint)
        chains = make_chain(c[0], comps)
        for sol in chains:
            sol2 = [component]
            sol2.extend(sol)
            solution.append(sol2)
        solutions.extend(solution)

    return solutions

def weight(chain):
    return sum([sum(part) for part in chain])

components = []

with open('input24.txt') as f:
# with open('test24.txt') as f:
    for line in f.readlines():
        ports = [ int(port) for port in line.rstrip().split('/') ]
        components.append((ports[0], ports[1]))

solutions = make_chain(0, components)
print('Max weight', max([weight(s) for s in solutions]))

max_length = 0
longest_s = None

for s in solutions:
    if len(s) == max_length:
        if weight(s) > weight(longest_s):
            max_length = len(s)
            longest_s = s
    elif len(s) > max_length:
        max_length = len(s)
        longest_s = s

print('Longest', longest_s, weight(longest_s))
