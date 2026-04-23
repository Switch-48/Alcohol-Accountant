from project.UserProfile import UserProfile
from project.UserProfile import create_profile
from project.test.tud_test_base import set_keyboard_input, get_display_output

def test_UserProfile_1():
    a = UserProfile(194, 79, 21, 'male')
    assert a._height == 1.94
    assert a._weight == 79
    assert a._age == 21
    assert a._gender == 'male'
    assert round(a.r_value, 6) == 0.693109

def test_UserProfile_2():
    a = UserProfile(165, 54, 41, 'Female')
    assert a._height == 1.65
    assert a._weight == 54
    assert a._gender == 'female'
    assert a._age == 41
    assert round(a.r_value, 6) == 0.547370

def test_create_profile():
    set_keyboard_input([180, 73, 21, 'male'])
    a = create_profile()
    assert a._weight == 73
    assert a._height == 1.80
    assert a._age == 21
    assert a._gender == 'male'