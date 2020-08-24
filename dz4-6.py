#dz4-6

from itertools import count

for itm in count(int(input('Первое число'))):
    print(itm)

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for itm in cycle(my_list):
    print(itm)