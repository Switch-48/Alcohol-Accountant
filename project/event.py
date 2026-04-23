from datetime import datetime, timedelta
from project.bac_calculator import bac
from project.consumed_drink import ConsumedDrink, beer_25, beer_30, beer_33, beer_50, mix, shot, wine, whiskey

class Event:
    def __init__(self):
        self._dictionary = {}

    def __str__(self):
        to_print = str()
        for m in self._dictionary:
            to_print += f'Drink: {self._dictionary[m][0]}, drank at {m.hour:02d}:{m.minute:02d}:{m.second:02d} on {m.day:02d}/{m.month:02d}/{m.year}\nBAC: {round(self._dictionary[m][1][-1], 3)}\n'
        return to_print

    def _consumed(self, drink, time=None):
        if time is None:
            time = datetime.now()

        self._dictionary[time] = [drink, bac.add(drink)]
        return self._dictionary
