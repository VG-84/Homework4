# dz4-7

def in_fact(n: int):
    up = 1
    result = 1
    while up <= n:
        yield result
        up += 1
        result *= up

for idx, itm in enumerate(in_fact(99), 1):
    print(idx, itm)