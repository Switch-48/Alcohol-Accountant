from project.bac_calculator import bac
import project.consumed_drink as Consumption
import project.UserProfile as Profile
from datetime import datetime

def test_bac_add_1():
    b = bac
    assert b.ingested == []
    assert b.bac == []
    assert b.con == []
    bac.reset()

def test_bac_add_2():
    b = bac
    x = datetime(2019, 5, 1, 10, 16, 15)
    y = datetime(2019, 5, 1, 10, 21, 36)
    bac.add(Consumption.beer_25, x)
    bac.add(Consumption.beer_33, y)
    b.ingested[1] = round(b.ingested[1], 4)
    assert b.ingested == [9.8625, 13.0185]
    assert b.con == [datetime(2019, 5, 1, 10, 16, 15), datetime(2019, 5, 1, 10, 21, 36)]
    assert b.bac == [0, 0]
    bac.reset()

def test_bac_reset():
    b = bac
    drink = Consumption.whiskey
    b.add(drink)
    b.reset()
    assert bac.bac == []
    assert bac.con == []
    assert bac.ingested == []

def test_bac_calculate_1():
    b = bac
    drink = Consumption.whiskey
    b.add(drink)
    a = b.calculate()
    assert a == 0
    b.reset()

def test_bac_calculate_2():
    b = bac
    user = Profile.UserProfile(189, 87, 38, 'male')
    drink = Consumption.beer_25
    x = datetime(2019, 5, 1, 10, 16, 15)
    y = datetime(2019, 5, 1, 11, 56, 15)
    b.add(drink, x)
    a = b.calculate(y, user)
    assert round(a, 6) == 0.140964
    b.reset()

def test_bac_calculate_3():
    b = bac
    user = Profile.UserProfile(173, 61, 25, 'Female')
    drink = Consumption.beer_25
    x = datetime(2019, 5, 1, 10, 16, 15)
    y = datetime(2019, 5, 1, 10, 26, 15)
    z = datetime(2019, 5, 1, 11, 5, 27)
    b.add(drink, x)
    b.add(drink, y)
    a = b.calculate(z, user)
    assert round(a, 6) == 0.563637
    b.reset()

def test_bac_calculate_4():
    b = bac
    user = Profile.UserProfile(173, 61, 25, 'Female')
    drink = Consumption.beer_25
    x = datetime(2019, 5, 1, 10, 16, 15)
    y = datetime(2019, 5, 1, 10, 26, 15)
    z = datetime(2019, 5, 2, 11, 5, 27)
    b.add(drink, x)
    b.add(drink, y)
    a = b.calculate(z, user)
    assert round(a, 6) == 0
    b.reset()

def test_bac_calculate_5():
    b = bac
    drink = Consumption.beer_25
    x = datetime(2019, 5, 1, 10, 16, 15)
    y = datetime(2019, 5, 1, 10, 26, 15)
    z = datetime(2019, 5, 1, 10, 59, 27)
    b.add(drink, x)
    b.add(drink, y)
    a = b.calculate(z)
    assert round(a, 6) == 0.314119
    b.reset()

def test_bac_calculate_6():
    b = bac
    drink = Consumption.beer_25
    x = datetime(2019, 5, 1, 10, 16, 15)
    y = datetime(2019, 5, 1, 10, 26, 15)
    b.add(drink, y)
    a = b.calculate(x)
    assert round(a, 6) == 0
    b.reset()

def test_bac_max_bac_1():
    b = bac
    drink = Consumption.beer_25
    b.add(drink)
    a = b.get_max_bac()
    assert a == 0
    b.reset()

def test_bac_max_bac_2():
    b = bac
    drink = Consumption.beer_25
    x = datetime(2019, 5, 1, 10, 16, 15)
    y = datetime(2019, 5, 2, 10, 16, 15)
    b.add(drink, x)
    a = b.get_max_bac(y)
    assert round(a, 5) == 0.15747
    b.reset()

def test_bac_max_bac_3():
    b = bac
    user = Profile.UserProfile(189, 87, 38, 'male')
    drink = Consumption.beer_25
    x = datetime(2019, 5, 1, 10, 16, 15)
    y = datetime(2019, 5, 1, 11, 56, 15)
    b.add(drink, x)
    a = b.get_max_bac(y, username = user)
    assert round(a, 5) == 0.15678
    b.reset()
