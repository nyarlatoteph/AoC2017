steps = []
with open('input5.txt') as f:
    for line in f.readlines():
        step = int(line.rstrip())
        steps.append(step)

# steps = [0, 3, 0, 1, -3]

count = 0
current_step = 0
while current_step >= 0 and current_step < len(steps):
    next_step = current_step + steps[current_step]
    if steps[current_step] >= 3:
        steps[current_step] -= 1
    else:
        steps[current_step] += 1
    current_step = next_step
    count += 1

print(current_step)
print(steps)
print(count)