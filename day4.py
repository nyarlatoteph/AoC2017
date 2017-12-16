def is_passphrase(passphrase):
    words = {}
    for word in passphrase.split(" "):
        if word in words:
            return False
        words[word] = True
    return True


import collections

def is_passphrase2(passphrase):
    words = {}
    for word in passphrase.split(" "):
        counter = collections.Counter(word)
        if counter in words.values():
            return False
        words[word] = counter
    return True


count = 0
with open('input4.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        if is_passphrase2(line):
            count += 1

# print(is_passphrase('aa bb cc dd ee'))
# print(is_passphrase('aa bb cc dd aa'))
# print(is_passphrase('aa bb cc dd aaa'))

print(is_passphrase2('abcde fghij'))
print(is_passphrase2('abcde xyz ecdab'))
print(is_passphrase2('a ab abc abd abf abj'))
print(is_passphrase2('iiii oiii ooii oooi oooo'))
print(is_passphrase2('oiii ioii iioi iiio'))

print(count)