class User:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def Name(self):
        return self._name

    @property
    def Age(self):
        return self._age

    @property
    def Gender(self):
        return self._gender