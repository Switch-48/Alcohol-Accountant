from datetime import datetime, timedelta
from project.UserProfile import user
from project.consumed_drink import ConsumedDrink
import math


class bac:
    def __init__(self):
        # Sets the initial variables BAC, time of consumption and maximal BAC as 0
        self.ingested = []
        self.bac = []
        self.con = []

    def add(self, drink, drink_time=None):
        if drink_time is None:
            drink_time = datetime.now()

        self.con.append(drink_time)
        self.ingested.append(drink._standard_units*10)
        self.bac.append(0)
        return self.bac

    def calculate(self, time=None, username=None):
        if time is None:
            time = datetime.now()

        if username is None:
            username = user

        value = 0
        while value < len(self.bac):
            if (time - self.con[value]).total_seconds() >= 0:  # Only if the drink was drunk in the past
                self.bac[value] = (self.ingested[value]*(1-math.e**-(6.5*((time-self.con[value]).total_seconds()/3600))))/(username.r_value*username._weight) - 0.018*((time-self.con[value]).total_seconds()/3600)
            else:
                self.bac[value] = 0

            if self.bac[value] < 0:
                self.bac[value] = 0
            value += 1

        return sum(self.bac)

    def get_max_bac(self, time=None, username=None):
        if time is None:
            time = datetime.now()

        if username is None:
            username = user

        max_bac = 0
        while (time-min(self.con)).total_seconds() >= 0:
            if self.calculate(time, username) > max_bac:
                max_bac = self.calculate(time, username)
            time -= timedelta(minutes=1)
        return max_bac

    def reset(self):
        self.bac = []
        self.con = []
        self.ingested = []


bac = bac()
