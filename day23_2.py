import functools

def factors(n):    
    return set(functools.reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# 902 is too low, 1000 too high
h = 0
b = 108400
    
for n in range(1001):
    """
    f = 1
    for d in range(2, b):
        if b%d == 0 and b/d >= 2 and b/d < b:
            f = 0
            break

    if f == 0:
        h += 1
    """
    f = factors(b)
    f.remove(1)
    f.remove(b)
    if len(f) >= 2:
        h += 1

    b += 17

print(h)

"""
b = 108400
c = b + 17000

start: 
    set f 1
    set d 2

    outer: 
        set e 2

        inner: 
            set g d
            mul g e
            sub g b
            jnz g 2
            set f 0
            sub e -1
            set g e
            sub g b
            jnz g inner

        sub d -1
        set g d
        sub g b
        jnz g outer

    jnz f 2
    sub h -1
    set g b
    sub g c
    jnz g 2
    goto end
    sub b -17
    goto start
end:
"""