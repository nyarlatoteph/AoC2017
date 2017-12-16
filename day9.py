def score(stream):
    garbage_characters, score, c, group = (0, 0, 0, 0)
    garbage = False

    while c < len(stream):
        if garbage:
            if stream[c] == '!':
                c += 1
            elif stream[c] == '>':
                garbage = False
            else:
                garbage_characters += 1
        else:
            if stream[c] == '{':
                group += 1
            elif stream[c] == '}':
                score += group
                group -= 1
            elif stream[c] == '<':
                garbage = True
        c += 1

    return (score, garbage_characters)


with open('input9.txt') as f:
    stream = f.readline()


assert score('{}')[0] == 1
assert score('{{{}}}')[0] == 6
assert score('{{},{}}')[0] == 5
assert score('{{{},{},{{}}}}')[0] == 16
assert score('{<a>,<a>,<a>,<a>}')[0] == 1
assert score('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0] == 9
assert score('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0] == 9
assert score('{{<a!>},{<a!>},{<a!>},{<ab>}}')[0] == 3

print(score(stream))