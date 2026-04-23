class UserProfile:
    def __init__(self, height, weight, age, gender):
        self._height = height/100
        self._weight = weight
        self._gender = gender.lower()
        self._age = age
        if self._gender == 'male':
            self.r_value = 0.62544 + 0.13664*self._height - self._weight*(0.00189 + 0.002425/self._height**2) + 1/(self._weight*(0.057986 + 2.545*self._height - 0.02255*self._age))
        elif self._gender == 'female':
            self.r_value = 0.50766 + 0.11165*self._height - self._weight*(0.001612 + 0.0031/self._height**2)-1/(self._weight*(0.62115-3.1665*self._height))


def create_profile():
    height = int(input('Height: '))
    weight = int(input('Weight: '))
    age = int(input('Age: '))
    gender = input('Gender: ').lower()
    user = UserProfile(height, weight, age, gender)
    return user

user = UserProfile(183, 89, 23, 'male')