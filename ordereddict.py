from collections import OrderedDict

unsorted = {
    'bling': 'blang',
    'thring': 'thrang',
    'potatoes': 'boring',
    'elastic': 'waist'
}

sorted_ = OrderedDict(sorted(unsorted.items(), key=lambda t: t[0]))
print('sorted_: {0}'.format(sorted_))
