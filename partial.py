from functools import partial

for i in xrange(2, 2):
    print(i)
def sing_song(verses, encore=False, *args, **kwargs):
    for i in xrange(1, verses + 1):
        if i % 4 == 0:
            print("Fra la mah")
        elif i % 3 == 0:
            print("Kah Nee Tah")
        elif i % 2 == 0:
            print("Shish boom bah")
        else:
            print("Tra la la")
    if encore:
        print("... Freebird!")
    if len(args) > 0:
        print("Special thanks to {}!".format(", ".join(args)))
    if len(kwargs) > 0:
        print("And we wouldn't be here without the help of our crew:")
        for name, nickname in kwargs.iteritems():
            print('\t{} ({})'.format(name, nickname))

sing_song(6)
print

print("[partial with encore]")
with_encore = partial(sing_song, encore=True)
with_encore(2)
print

print("[partial with extra args and kwargs]")

with_extra_arg = partial(
    sing_song,
    3,
    False,
    "Tommy",
    benjamin="The Button",
    tommy="The Mommy"
)
with_extra_arg()
print

print('[partial properties]')
print('partial.func: {0}'.format(with_extra_arg.func))
print('partial.args: {0}'.format(with_extra_arg.args))
print('partial.keywords: {0}'.format(with_extra_arg.keywords))
