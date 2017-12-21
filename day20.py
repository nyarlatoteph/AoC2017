import re
import math

p = []
v = []
a = []

lowest_a = None
which_particle_has_lowest_a = None

# with open('test20.txt') as f:
with open('input20.txt') as f:
    for line in f.readlines():
        m = re.match('p=\<([-\d]+),([-\d]+),([-\d]+)\>, v=\<([-\d]+),([-\d]+),([-\d]+)\>, a=\<([-\d]+),([-\d]+),([-\d]+)\>', line)
        if m:
            particle = [int(m.group(1)), int(m.group(2)), int(m.group(3))]
            velocity = [int(m.group(4)), int(m.group(5)), int(m.group(6))]
            acceleration = [int(m.group(7)), int(m.group(8)), int(m.group(9))]
            p.append(particle)
            v.append(velocity)
            a.append(acceleration)

            # Determine lowest acceleration (stays closest to origin in the long run)
            if lowest_a is None or abs(acceleration[0]) + abs(acceleration[1]) + abs(acceleration[2]) < lowest_a:
                lowest_a = abs(acceleration[0]) + abs(acceleration[1]) + abs(acceleration[2])
                which_particle_has_lowest_a = len(p)-1
        else:
            print('Could not match: ', line)


print(which_particle_has_lowest_a)

# def collides(n1, n2):

    # def match(sol1, sol2):
    #     if sol1 is None or sol2 is None:
    #         return False

    #     return (sol1 == sol2) or len(sol1) == 0 or len(sol2) == 0 or not set(sol1).isdisjoint(sol2)

    # def solutions(a, b, c):
    #     # Solves at^2 + bt + c = 0
    #     if a == 0:
    #         if b != 0:
    #             return [-c/b]
    #         elif c == 0:
    #             return []
    #     else:
    #         D = math.pow(b, 2) - 4*a*c
    #         if D >= 0:
    #             return [(-b + math.sqrt(D))/(2*a), (-b - math.sqrt(D))/(2*a)]

    #     return None

    # solx = solutions(a[n1][0]-a[n2][0], v[n1][0]-v[n2][0], p[n1][0]-p[n2][0])
    # soly = solutions(a[n1][1]-a[n2][1], v[n1][1]-v[n2][1], p[n1][1]-p[n2][1])
    # solz = solutions(a[n1][2]-a[n2][2], v[n1][2]-v[n2][2], p[n1][2]-p[n2][2])

    # return match(solx, soly) and match(solx, solz) and match(soly, solz)

# n1 = 0
# while n1 < len(p):
    # collision = False
    # removals = []
    # for n2 in range(n1+1, len(p)):
    #     if collides(n1, n2):
    #         removals.append(n2)
    
    # if len(removals) > 0:
    #     removals.append(n1)
    #     for n in removals:
    #         p = p[0:n] + p[n+1:]
    #         v = v[0:n] + v[n+1:]
    #         a = a[0:n] + a[n+1:]
    # else:
    #     n1 += 1

for t in range(10000):
    if t % 1000 == 0:
        print(t, end='\r')

    collisions = {}
    for n in range(len(p)):
        v[n][0] += a[n][0]
        v[n][1] += a[n][1]
        v[n][2] += a[n][2]

        p[n][0] += v[n][0]
        p[n][1] += v[n][1]
        p[n][2] += v[n][2]

        coord = (p[n][0], p[n][1], p[n][2])
        if coord in collisions:
            collisions[coord] += 1
        else:
            collisions[coord] = 1

    for collision in [k for (k,v) in collisions.items() if v > 1]:
        n = 0
        while n < len(p):
            if collision == (p[n][0], p[n][1], p[n][2]):
                p = p[0:n] + p[n+1:]
                v = v[0:n] + v[n+1:]
                a = a[0:n] + a[n+1:]
            else:
                n += 1
        print('collisions removed', len(p))
                


print('\n')
print(len(p))