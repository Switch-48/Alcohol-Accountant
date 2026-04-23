import project.event as e
import project.consumed_drink as drink
from datetime import datetime

def test_string_no_drinks():
    event = e.Event()
    assert len(event._dictionary) == 0
    assert event.__str__() == ''


def test_string_one_drink():
    event = e.Event()
    t = datetime.now()
    dr = drink.ConsumedDrink('something', 500, 3)
    assert event._consumed(dr) != {t: [drink, [0]]}
    assert len(event._dictionary) == 1
    assert event.__str__() == f'Drink: something, drank at {t.hour}:{t.minute}:{t.second} on {t.day}/{t.month}/{t.year}\nBAC: 0\n'


def test_string_multiple_drinks():
    event = e.Event()
    x = datetime(2019, 1, 5, 10, 15, 18)
    y = datetime(2019, 1, 5, 10, 42, 27)
    z = datetime(2019, 1, 5, 11, 5, 56)
    event._consumed(drink.whiskey, x)
    event._consumed(drink.whiskey, y)
    assert len(event._dictionary) == 2
    event._consumed(drink.whiskey, z)
    assert len(event._dictionary) == 3
    assert event.__str__() == 'Drink: Whiskey, drank at 10:15:18 on 05/01/2019\nBAC: 0\nDrink: Whiskey, drank at 10:42:27 on 05/01/2019\nBAC: 0\nDrink: Whiskey, drank at 11:05:56 on 05/01/2019\nBAC: 0\n'