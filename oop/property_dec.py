# https://www.youtube.com/watch?v=upmOAPk2cK8
# See 'classes/classes.py' for a more in depth analysis
# @property allows us to call class methods without (). Used primarily for getters so that users can access the attribute without () and then we can use @attribute.setter. @attribute.setter decorates 'def name(self, name):' to set a new name. So when we do 'obj.name = 'new name' we are calling 'def name(self, name):'.
# Using custom getters and setters is usually not necessary but Python is different than other languages because it makes it easy to change them after being in use (to avoid backwards compatibility issues).

HEROES = [
    'Richard Feynman',
    'Elon Musk',
    'Albert Einstein'
]

class Heroes:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name in HEROES:
            self._name = name
        else:
            raise ValueError(f'{name} is not a hero.')

hero = Heroes('Richard Feynman')
hero.name = 'walter white'
