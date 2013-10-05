
# Simple decorator

def decoratress(func):
    def wrapped(*args, **kwargs):
        print("You called {} with args, kwargs: {}, {}".format(
            func, args, kwargs)
        )
        return func(*args, **kwargs)
    return wrapped


@decoratress
def decorated_func(number, bingo=False):
    s = "The next number is ... {}.".format(number)
    if bingo:
        s += "\nI WIN!!!"
    return s

print(decorated_func(5))
print
print(decorated_func(8, True))
print

print('---')
print


# Decorator with arguments

def magic_word(word="celery"):
    def decorator(func):
        def wrapped_f(*args, **kwargs):
            if word.lower() == "please":
                return "Please? Well, okay.\n{}".format(func(*args, **kwargs))
            else:
                return "{}? You get nothing!".format(word.title())
        return wrapped_f
    return decorator


# Need the parens after the decorator!
@magic_word()
# @magic_word("please")
def gimme_pizza(count, pie_type="muddled broccoflower"):
    if count > 1:
        pie_type += 's'
    return "{} xtra-hugeish {}, coming right up!".format(
        count, pie_type
    )

print(gimme_pizza(3))


