from .user import User

class Notification:
    def __init__(self, notification_id: int, message: str, recipient: User):
        self.notification_id = notification_id
        self.message = message
        self.recipient = recipient

    def send(self):
        print(f"Message for {self.recipient.username}: {self.message}")