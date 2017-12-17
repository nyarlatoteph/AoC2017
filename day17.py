from collections import deque

class CircularBuffer():

    def __init__(self, steps):
        self.buffer = deque()
        self.steps = steps
        self.pos = 0

    def append(self, value):
        if (len(self.buffer) > 0):
            self.pos = (self.pos + 1 + self.steps) % len(self.buffer)
        self.buffer.insert(self.pos+1, value)

    def __str__(self):
        return self.buffer.__str__()

    def index(self, value):
        return self.buffer.index(value)
    
    def at(self, value):
        return self.buffer[value]

spinlock = CircularBuffer(366)
# spinlock = CircularBuffer(3)

for n in range(0, 2018):
    spinlock.append(n)

n = spinlock.index(2017)
print(spinlock.at(n+1))

# part 2
pos = 0
current = 0
for n in range(1, 50000000):
    pos = (pos + 367) % n
    if pos == 0:
        current = n

print(current)