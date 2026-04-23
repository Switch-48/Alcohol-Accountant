class EventDatabase:
    def __init__(self):
        self.past_events=[]
        self.size=0

    def add_events(self, max_bac, hangover_rating, event):

        if self.size >= 10:
            # reorder the events
            del self.past_events[0]
            self.size-=1
            i = 0
            while i < len(self.past_events)-1:
                self.past_events[i] = self.past_events[i + 1]
                i += 1

        #create and add event
        self.past_events.append({"max bac": max_bac, "hangover_rating": hangover_rating, "event": event})
        self.size+=1

