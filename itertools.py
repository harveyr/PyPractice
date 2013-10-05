import itertools
from itertools import chain

# Lazy Fibonacci slice
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

sliced = itertools.islice(fib(), 0, 20)
print(", ".join(map(str, sliced)))

print('\n---\n')

# Lazy filtering
def is_awesome_num(num):
    """Everyone knows such numbers are pretty great."""
    return num % 9 == 0

some_awesome_nums = itertools.ifilter(is_awesome_num, xrange(1, 100))
for i in itertools.islice(some_awesome_nums, 0, 3):
    print(i)

print('\n---\n')

# groupby
def even_odd_groups(items):
    f = lambda x: 'even' if x % 2 == 0 else 'odd'
    consecutives = sorted(items, key=f)
    grouped = itertools.groupby(consecutives, f)
    return grouped

for group, vals in even_odd_groups(range(1, 20)):
    print('{}: {}'.format(group, ", ".join(map(str, vals))))

print('\n---\n')

# flatmap
def spectrum_of_stuffs(item):
    return [
        "awesome {}".format(item),
        "middlin' {}".format(item),
        "baddish {}".format(item)
    ]

def flatmap(f, items):
    # http://docs.python.org/2/library/itertools.html#itertools.chain
    return chain.from_iterable(itertools.imap(f, items))

items = [
    'dish soap',
    'chicken nuggets',
    'whittling skills',
    'hits of the 90s'
]

# not flattened:
stuffs = map(spectrum_of_stuffs, items)

# flattened:
for i in flatmap(spectrum_of_stuffs, items):
    print(i)

print('\n---\n')

# factor grabbing with ifilter, takewhile, count, and flatmap
def factors(n):
    return itertools.ifilter(
        lambda x: n % x == 0,
        itertools.takewhile(lambda y: y <= n / 2 + 1, itertools.count(1))
    )

unique_factors = set(flatmap(factors, [14, 72, 193]))
print('unique_factors: {0}'.format(unique_factors))

