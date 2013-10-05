import inspect


class ParentClass(object):
    pass

class ClassyClass(ParentClass):
    """
    It's got class. You know - because it's a class.
    But seriously, folks ...
    """
    classy_factor = 9


def header(text):
    print
    print('--- {} ---'.format(text))

def example(text):
    print('[{}]'.format(text))


header('Basic Class Attributes')

example('__name__')
print("\t{}".format(ClassyClass.__name__))

example('__doc__')
print("\t{}".format(ClassyClass.__doc__))

example('inspect.getdoc()')
print('{}'.format(inspect.getdoc(ClassyClass)))
print

example('__module__')
print("\t{}".format(ClassyClass.__module__))
print


header('Determining Object Types')
instance = ClassyClass()

# Use type, for example, for output or feedback (e.g., to a log file).
# Generally not recommended for legit introspection.
example('type')
print('\ttype(instance): {0}'.format(type(instance)))

example('issubclass')
print('\tissubclass(ClassyClass, ParentClass): {0}'.format(
    issubclass(ClassyClass, ParentClass))
)

example('isinstance')
print('\tisinstance(instance, ClassyClass): {0}'.format(isinstance(instance, ClassyClass)))
print('\tisinstance(instance, ParentClass): {0}'.format(isinstance(instance, ParentClass)))

header("Function Signatures")

def cookies(count, extra_love=False, *args, **kwargs):
    cookie_pile = "cookies! ".join(['' for i in range(count)])
    if extra_love:
        cookie_pile += "COOKIES!!!"
    return cookie_pile

example('inspect.getargspec()')
argspec = inspect.getargspec(cookies)
# list of all argument names specified for the function:
print('\targspec.args: {0}'.format(argspec.args))
# varargs and keywords are the names of the * and ** arguments or None
print('\targspec.varargs: {0}'.format(argspec.varargs))
print('\targspec.keywords: {0}'.format(argspec.keywords))
# defaults is a tuple of default/optional argument values or None
print('\targspec.defaults: {0}'.format(argspec.defaults))
print
print('\t[example inspection of defaults]')
defaults_index = len(argspec.args) - len(argspec.defaults)
defaults = dict(zip(argspec.args[defaults_index:], argspec.defaults))
print("\t\t{}".format(defaults))

