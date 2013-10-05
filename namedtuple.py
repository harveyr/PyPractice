from collections import namedtuple


PersonnelRecord = namedtuple('PersonnelRecord', 'name, age, title, sucklevel')

print('simple instantiation')
record = PersonnelRecord('Billy', 47, 'Senior Managerishtype', 3)
print(record)
print(record.name)
print


print('_make() and _asdict() example')
personnel = []
personnel_raw = [
    ('Hoolihan', 17, 'Farmboy', 1),
    ('Slappy', 27, 'Junior Dude', 9)
]

for data in personnel_raw:
    personnel.append(PersonnelRecord._make(data))

for p in personnel:
    print(p._asdict())
print

print('_fields')
print(personnel[0]._fields)
print

print('dict to named tuple')
d = {
    'name': 'Sir Johnald',
    'age': 52,
    'title': 'Occasional Knight',
    'sucklevel': 7
}
record = PersonnelRecord(**d)
print('record: {0}'.format(record))
