import project.event_database as e
import project.event as event_ob

def test_one_event():
    event=e.EventDatabase()
    event.add_events(0, 5, event_ob.Event())

    assert event.past_events
    assert event.size <= 10
    assert event.past_events[0] != None

def test_multiple_events():
    event=e.EventDatabase()
    for i in range(0, 8):
        event.add_events(7, 0, event_ob.Event())
    assert event.size == 8
    assert event.past_events[0] != None
    assert len(event.past_events) == 8

def test_events():
    event=e.EventDatabase()
    for i in range(0,15):
        event.add_events(2.1, 4, event_ob.Event())
    assert event.size == 10
    assert event.past_events[0] != None