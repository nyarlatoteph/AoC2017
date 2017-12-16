def calcsum(input_string, pos):
    result = 0
    n = 0
    for c in input_string:
        if c == input_string[(n + pos) % len(input_string)]:
            result += int(c)
        n += 1

    return result


f = open('input1.txt')

for line in f.readlines():
    line = line.rstrip()

    # print(calcsum('1122', 1))
    # print(calcsum('1111', 1))
    # print(calcsum('1234', 1))
    # print(calcsum('91212129', 1))
    # print(calcsum(line, 1))

    print(calcsum('1212', 2))
    print(calcsum('1221', 2))
    print(calcsum('123425', 3))
    print(calcsum('123123', 3))
    print(calcsum('12131415', 4))

    print(calcsum(line, int(len(line)/2)))
