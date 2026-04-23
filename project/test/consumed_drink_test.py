import project.consumed_drink as c

def test_consumed_drink_1():
    a = c.ConsumedDrink('beer_25', 250, 5)
    assert a._volume == 250
    assert a._alcohol_volume == 12.5
    assert round(a._standard_units, 5) == 0.98625
    assert a._name == 'beer_25'

def test_consumed_drink_2():
    a = c.ConsumedDrink('whiskey', 35, 40)
    assert a._volume == 35
    assert a._alcohol_volume == 14
    assert round(a._standard_units, 5) == 1.1046
    assert a._name == 'whiskey'

def test_consumed_drink_name():
    a = c.ConsumedDrink('beer_25', 250, 5)
    assert a.__repr__() == 'beer_25'
