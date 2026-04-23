def hasNotification(alcohol, prev=0):
    if alcohol <= 0.5 and prev > 0.5:
        prev = alcohol
        return prev, 'You are now below the legal limit of alcohol content in your blood with which it is still allowed to drive'
    if alcohol >= 4 and prev < 4:
        prev = alcohol
        return prev, 'The alcohol content in your blood is now dangerously high. You should stop drinking alcohol for your own safety.'
    elif alcohol >= 2 and prev < 2:
        prev = alcohol
        return prev, 'The alcohol content in your blood is somewhat high. Consider drinking something without any alcohol.'
    else:
        prev = alcohol
        return prev, ''

print(hasNotification(2.1)[1])
print(hasNotification(4, hasNotification(2.1)[0])[1])
print(hasNotification(0.3, hasNotification(4)[0])[1])
print(hasNotification(0.3, hasNotification(0.3)[0])[1])
print(hasNotification(4, hasNotification(0.3)[0])[1])
print(hasNotification(2.1, hasNotification(0.3)[0])[1])
