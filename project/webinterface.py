from datetime import timedelta, datetime
from flask import Flask, request, render_template, redirect, url_for, jsonify

from project import event_database
from project.Notification import hasNotification
from project.UserProfile import user
from project.bac_calculator import bac
from project.consumed_drink import drink_list
from project.event import Event

app = Flask(__name__)
events = event_database.EventDatabase()
current_event = Event()
prev_event = None


@app.route('/')
def index():
    return render_template('index.html', drinklist=drink_list, prev_event=prev_event)


@app.route('/events')
def events_page():
    return render_template('events.html', events=events)


@app.route('/settings')
def settings():
    return render_template('settings.html', user=user)


@app.route('/sw.js')
def get_serviceworker():
    return app.send_static_file('js/sw.js')


@app.route('/api/bac')
def get_bac():
    return f'{bac.calculate():.4f}'


@app.route('/api/graph')
def graph():
    def label_for(now, delta=timedelta(0)):
        newdate = now + delta
        if now.day != newdate.day:
            return newdate.strftime('%a %d %b %H:%M')
        else:
            return newdate.strftime('%H:%M')

    now = datetime.now()
    labels = []
    past_values = []
    future_values = []

    # Retrieve the past
    # TODO
    for i in range(-120, 0, 10):
        t = timedelta(minutes=i)
        time = label_for(now, t)
        my_bac = bac.calculate(now + t)
        labels.append(time)
        past_values.append({
            'x': time,
            'y': my_bac,
        })
    past_values.append({
        'x': label_for(now),
        'y': bac.calculate(now),
    })

    # Predict the future
    i = 0
    my_bac = 1000
    while my_bac > 0:
        t = timedelta(minutes=i)
        time = label_for(now, t)
        my_bac = bac.calculate(now + t)
        labels.append(time)
        if my_bac != 0:
            future_values.append({
                'x': time,
                'y': my_bac,
            })
        i += 10  # advance 30 minutes
    return {'labels': labels, 'future_values': future_values, 'past_values': past_values}


@app.route('/api/add_drink', methods=['POST'])
def add_drink():
    drink_name = request.form['drink']
    drink = None

    for key, value in drink_list:
        if drink_name == key:
            drink = value
            break

    if drink is not None:
        current_event._consumed(drink, datetime.now())
        return 'OK'
    else:
        return 'FAIL'


@app.route('/api/submit_rating', methods=['POST'])
def submit_rating():
    global prev_event
    rating = float(request.form['rating'])
    if prev_event is not None:
        prev_event.hangover_rating = rating
        events.add_events(prev_event.max_bac, rating, prev_event)
        prev_event = None
    return redirect(url_for('index'))


@app.route('/api/settings', methods=['POST'])
def set_settings():
    try:
        height = int(request.form['height'])
    except ValueError:
        height = user._height*100  # If an invalid value is supplied, don't change it
    try:
        weight = int(request.form['weight'])
    except ValueError:
        weight = user._weight
    try:
        age = int(request.form['age'])
    except ValueError:
        age = user._age
    gender = request.form['gender']
    if gender not in ['male', 'female']:
        gender = user._gender  # If an invalid gender is supplied, don't change it

    user.__init__(height, weight, age, gender)  # Reinitialize object with new values
    if 'reset' in request.form.keys():
        bac.reset()

    return redirect(url_for('settings'))


@app.route('/api/pollnotifications')
def notifications():
    global current_event, prev_event
    now_bac = bac.calculate()
    refresh_page = False
    if notifications.last_bac != 0 and now_bac == 0 and prev_event is None:
        current_event.max_bac = bac.get_max_bac()
        prev_event = current_event
        current_event = Event()
        bac.reset()
        refresh_page = True
    notifications.last_bac, notif = hasNotification(now_bac, notifications.last_bac)
    return jsonify([notif, refresh_page])


notifications.last_bac = 0

