def generate(factor, input):
    return (input*factor) % 2147483647

def generatorA(input):
    while True:
        input = generate(16807, input)
        if (input % 4) == 0:
            return input

def generatorB(input):
    while True:
        input = generate(48271, input)
        if (input % 8) == 0:
            return input

a = 289
b = 629

# a = 65
# b = 8921
matches = 0

for _ in range(5000000):
    a = generatorA(a)
    b = generatorB(b)
    # print(a, b)
    ab = bin(a)
    bb = bin(b)
    if ab[-16:] == bb[-16:]:
        matches += 1

print(matches)