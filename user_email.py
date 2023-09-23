import requests
from keys import *

class UserEmail:
    def __init__(self, first_name, last_name, email):
        self.sheety_url = google_sheet_url_flight
        self.SHEETY_header = {"Authorization": sheety_auth_key}
        self.f_name = first_name
        self.l_name = last_name
        self.email = email
        self.body = {
            "user": {
                "firstName": self.f_name,
                "lastName": self.l_name,
                "email": self.email
            }
        }
        self.response = requests.post(url=self.sheety_url, json=self.body, headers=self.SHEETY_header)
        self.data = self.response.json()





