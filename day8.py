import re

registers = dict()

current_max = 0

with open('input8.txt') as f:
# with open('test3.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        p = re.compile(r'(\w+)\s*(inc|dec)\s*(-?\d+)\sif\s(\w+)\s([^\d]+)\s*(\d+)')
        m = re.match(p, line)
        if m is None:
            print("Unmatched line: ", line)
            break

        register = m.groups()[0]
        increase = (m.groups()[1] == 'inc')
        amount = int(m.groups()[2])
        check = m.groups()[3]
        operator = m.groups()[4].strip()
        size = m.groups()[5]
        # print(register, increase, amount, check, operator, size)

        register_to_check = 0 if check not in registers else registers[check]
        to_eval = "%s %s %s" % (register_to_check, operator, size)
        if eval(to_eval):
            current_amount = 0 if register not in registers else registers[register]
            current_amount += amount if increase else -amount
            registers[register] = current_amount
            current_max = max(current_max, current_amount)

print(max(registers.values()))
print(current_max)