class Event:
     def __init__(self, opened: bool, type: str, text: str):
         self.opened = opened
         self.text = text
 
 
class EventLog:
     def __init__(self):
         self.events = list()
 
     def record_event(self, event: Event):
         if isinstance(event, Event):
             self.events.append(event)
 
     def read_all_messages(self):
         return [event.data for event in self.events]
 
     def read_last_message(self):
         return self.events[-1].data if self.events else "No events available."