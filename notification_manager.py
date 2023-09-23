from twilio.rest import Client
from keys import *


# -----------Working--------------------------------------

class NotificationManager:
    def __init__(self, body):
        self.account_sid = not_acc
        self.auth_token = not_auth_token
        self.client = Client(self.account_sid, self.auth_token)
        self.my_number = not_my_number
        self.body = body
        self.message = self.client.messages.create(
            from_=not_virtual_number,
            body=self.body,
            to=not_my_number

        )

    pass
