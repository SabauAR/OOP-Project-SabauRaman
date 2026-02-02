from datetime import date
from .event import Event, EventLog
from .property import Property

class MaintenanceRequest:
    def __init__(self, request_id: int, property: "Property", request_date: date, description: str):
        self.request_id = request_id
        self.property = property
        self.request_date = request_date
        self.description = description
        self.status = "pending"

    def approve(self, event_log: EventLog):
        if self.status != "pending":
            return
        self.status = "approved"

        message = f"Request {self.request_id} approved for property {self.property.address}."
        event = Event(opened=True, type="MaintenanceRequestApproved", text= "It has been solved")
        event_log.record_event(event)

        note = f"Maintenance approved on {date.today().isoformat()}"
        self.property.history.append(note)

    def reject(self, event_log: EventLog):
        if self.status != "pending":
            return
        self.status = "rejected"

        message = f"Request {self.request_id} rejected for property {self.property.address}."
        event = Event(opened=True, type="MaintenanceRequestRejected", data=message)
        event_log.record_event(event)
        
        
        
        
