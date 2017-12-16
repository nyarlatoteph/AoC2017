import csv
import itertools

r = csv.reader(open('input2.txt', newline=''), delimiter=' ')
# r = csv.reader(open('test.txt', newline=''), delimiter=' ')

total = 0
for row in r:
    row = ''.join(row).split('\t')

    # part 1
    # checksum_max = -1
    # checksum_min = -1
    # for entry in row:
    #     number = int(entry)
    #     if checksum_max == -1 or number > checksum_max:
    #         checksum_max = number
    #     if checksum_min == -1 or number < checksum_min:
    #         checksum_min = number
    # diff = checksum_max - checksum_min
    # total += diff
    
    # part 2
    perms = itertools.permutations(row, 2)
    for (a, b) in perms:
        a = int(a)
        b = int(b)
        if a % b == 0:
            total += int(a/b)
            break

print(total)
