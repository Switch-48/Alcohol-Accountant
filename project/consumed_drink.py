class ConsumedDrink:
    def __init__(self, name, volume, percentage):
        self._volume = volume
        # Assuming people fill in percentages instead of fractions
        self._percentage = percentage/100
        self._alcohol_volume = volume * self._percentage
        # There's 10 g of alcohol in a standard glass, the density of alcohol is 0.789 g/mL
        self._standard_units = (self._alcohol_volume*0.789)/10
        self._name = name

    def __repr__(self):
        return self._name
        # return f'\nDrink: {self._name}, drank at {self._time}'


beer_25 = ConsumedDrink('Standard beer glass', 250, 5)
beer_30 = ConsumedDrink('Beer bottle', 300, 5)
beer_33 = ConsumedDrink('Beer can', 330, 5)
beer_50 = ConsumedDrink('Large beer bottle or can', 500, 5)
mix = ConsumedDrink('Mix drink', 250, 5)
wine = ConsumedDrink('Wine', 100, 12)
whiskey = ConsumedDrink('Whiskey', 35, 40)
shot = ConsumedDrink('Shot', 20, 40)

drink_list = [
    ('beer_25', beer_25),
    ('beer_30', beer_30),
    ('beer_33', beer_33),
    ('beer_50', beer_50),
    ('mix', mix),
    ('wine', wine),
    ('whiskey', whiskey),
    ('shot', shot),
]
