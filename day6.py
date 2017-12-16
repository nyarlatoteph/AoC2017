import math

def determine_most_blocks(configuration):
    result = 0
    for index, blocks in enumerate(configuration):
        if configuration[result] < blocks:
            result = index
    return result

def redistribute(configuration, bank):
    amount = configuration[bank]
    configuration[bank] = 0
    while amount > 0:
        bank = (bank+1) % len(configuration)
        configuration[bank] += 1
        amount -= 1

    return configuration

current_configuration = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
# current_configuration = [0, 2, 7, 0]

previous_configurations = []
cycles = 0

while current_configuration not in previous_configurations:
    previous_configurations.append(list(current_configuration))
    # print(current_configuration)
    bank = determine_most_blocks(current_configuration)
    # print(bank)
    current_configuration = redistribute(current_configuration, bank)
    cycles += 1

print(cycles)

cycles = 0
day2 = list(current_configuration)
while True:
    bank = determine_most_blocks(current_configuration)
    current_configuration = redistribute(current_configuration, bank)
    cycles += 1
    if current_configuration == day2:
        break

print(cycles)

