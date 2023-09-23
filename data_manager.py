import requests
from datetime import datetime as dt
from keys import *

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_url = google_sheet_url_user
        self.auth = sheety_auth_key
        self.SHEETY_header = {
            "Authorization": self.auth
        }
        self.response = requests.get(url=self.sheety_url, headers=self.SHEETY_header)
        self.response.raise_for_status()
        self.data = self.response.json()['sheet1']
    pass

    def put_request(self, data, id):
        body = {
            "sheet1": {
                "iataCode": data,
            }
        }
        put = requests.put(url=f"{self.sheety_url}/{id}", json=body, headers=self.SHEETY_header)
        put.raise_for_status()


# datas = DataManager()
# # # print(datas.put_request("L"))
# print(datas.data)
