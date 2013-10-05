from collections import OrderedDict

unsorted = {
    'bling': 'blang',
    'thring': 'thrang',
    'potatoes': 'boring',
    'elastic': 'waist'
}

# sorted by key
sorted_ = OrderedDict(sorted(unsorted.items(), key=lambda t: t[0]))
print('sorted_: {0}'.format(sorted_))

# sorted by value
sorted_ = OrderedDict(sorted(unsorted.items(), key=lambda t: t[1]))
print('sorted_: {0}'.format(sorted_))
