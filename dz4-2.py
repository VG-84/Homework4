#dz4-2

def run_up(*args):
    up = float('test')
    for num in args:
        if num > up:
            yield num
        up = num
