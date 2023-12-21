class HouseCat:
    ''' Models a standard house cat. '''
    says = 'meow'

    def __init__(self, name, age, weight_kg):
        self.name = name
        self.age = age
        self.weight_kg = weight_kg

    @classmethod
    def from_pounds(cls, name, age, weight):
        return cls(name, age, weight / 2.2046)

    def play(self, *others):
        if others:
            players = ', '.join([o.name for o in others])
            players = f'with {players}'
