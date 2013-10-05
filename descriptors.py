import datetime


class CurrentDate(object):
    def __get__(self, instance, owner):
        """
        If instance is None, attribute was accessed from the class rather than
        an instance.
        """
        return datetime.date.today()

    def __set__(self, instance, value):
        """
        Return value is irrelevant. Method is solely responsible for storing
        the value.

        Don't use setattr here unless you like infinity. Use __dict__, which
        bypasses Python's standard handling of attributes and such.

        Django has a workaround for the fact that you need the attribute's name
        to set its value in __dict__.
        """
        raise NotImplementedError(
            "'{}'? Who do you think you are? Father Time?".format(value)
        )


class ThingWithDate(object):
    now = CurrentDate()


this_one_thing = ThingWithDate()
print('this_one_thing.now: {0}'.format(this_one_thing.now))
this_one_thing.now = "later"
