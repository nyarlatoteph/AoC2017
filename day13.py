
def calc_severity(delay):
    for p in range(0, max(layers.keys())+1):
        if p in layers and ((p+delay) % ((layers[p]-1)*2)) == 0:
            return True

    return False


inputstring = "{ "
with open('input13.txt') as f:
    for line in f.readlines():
        inputstring += line + ","
inputstring += " }"
layers = eval(inputstring)

# layers = { 0: 3, 1: 2, 4: 4, 6: 4, }

# print(calc_severity(layers, 0)[1])

delay = 0
caught = True
while caught:
    caught = calc_severity(delay)
    delay += 1

print(delay-1)
