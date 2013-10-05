from collections import defaultdict

"""
The first argument provides the initial value for the default_factory attribute; it defaults to None. All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
"""

print('list factory:')
d = defaultdict(list)
for i in range(10):
    d['newlist'].append(i)

print(d['newlist'])
print

print('int factory:')
important_string = "finnigilligan"
d = defaultdict(int)
for letter in important_string:
    d[letter] += 1
for count, letter in d.iteritems():
    print('({}) {}'.format(count, letter))
print

print('set factory:')
d = defaultdict(set)
for letter in important_string:
    d['letters'].add(letter)
print(d['letters'])
print
