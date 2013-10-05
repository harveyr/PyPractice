from collections import deque

# Recipes: http://docs.python.org/2/library/collections.html#deque-recipes

"""
Deques are a generalization of stacks and queues (the name is pronounced "deck" and is short for "double-ended queue"). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction."""


ingreds = [
    'water',
    'barley',
    'hops',
    'bath salts'
]

consumables = [
    'preexisting beer',
    'fancy feast',
    'dog'
]

activities = [
    'nose picking',
    'interpretive beer dancing',
    "thumb twiddlin'"
]

# iterable
d = deque(ingreds)
for i in d:
    print(i)

print('append, appendleft')
d.append('time')
d.appendleft('romance novel')
print(d)
print


print('extend, extendleft')
d.extend(consumables)
d.extendleft(activities)
print(d)
print

print('reverse()')
d.reverse()
print(d)
print


print('rotate()')
d.rotate(3)
print(d)
print


print("poppin' like it's hot")
print('d.pop(): {0}'.format(d.pop()))
print('d.popleft(): {0}'.format(d.popleft()))
print
