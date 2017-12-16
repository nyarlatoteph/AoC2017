def knot_hash(knot_list, length, position):
    if position + length < len(knot_list):
        sublist = knot_list[position : position + length]
        knot_list[position : position + length] = reversed(sublist)
    else:
        sublist = knot_list[position : len(knot_list)] + knot_list[0 : (position + length - len(knot_list))]
        sublist = list(reversed(sublist))
        knot_list[position : len(knot_list)] = sublist[0 : len(knot_list) - position]
        knot_list[0 : (position + length - len(knot_list))] = sublist[(len(knot_list) - position) : len(sublist)]

    return knot_list

def knot_hash2(input):
    position = 0
    skip = 0
    sparse_hash = list(range(0, 256))
    lengths = [ord(c) for c in input] + [ 17, 31, 73, 47, 23 ]

    for _ in range(64):
        for length in lengths:
            sparse_hash = knot_hash(sparse_hash, length, position)
            position = (position + length + skip) % len(sparse_hash)
            skip += 1
        
    dense_hash = ''
    for i in range(0, 16):
        val = sparse_hash[i*16]
        for n in range(1, 16):
            val ^= sparse_hash[i*16 + n]
        dense_hash += ('0' if len(hex(val)[2:]) < 2 else '') + hex(val)[2:]

    return dense_hash

assert knot_hash2('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert knot_hash2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert knot_hash2('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert knot_hash2('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

print(knot_hash2('147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70'))