from project.Notification import hasNotification

def test_notifications_1():
    assert hasNotification(0.5, 0.5) == (0.5, '')
    assert hasNotification(0.5, 0.6) == (0.5, 'You are now below the legal limit of alcohol content in your blood with which it is still allowed to drive')
    assert hasNotification(0.6, 0.6) == (0.6, '')
    assert hasNotification(0.6, 0.4) == (0.6, '')

def test_notifications_2():
    assert hasNotification(4, 4) == (4, '')
    assert hasNotification(4, 3.9) == (4, 'The alcohol content in your blood is now dangerously high. You should stop drinking alcohol for your own safety.')
    assert hasNotification(3.9, 4) == (3.9, '')
    assert hasNotification(3.9, 3.9) == (3.9, '')

def test_notifications_3():
    assert hasNotification(2, 2) == (2, '')
    assert hasNotification(2, 1.9) == (2, 'The alcohol content in your blood is somewhat high. Consider drinking something without any alcohol.')
    assert hasNotification(1.9, 2) == (1.9, '')
    assert hasNotification(1.9, 1.9) == (1.9, '')
