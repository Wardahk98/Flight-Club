import requests
from datetime import datetime as dt
from dateutil.relativedelta import *
from keys import *


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, loc):
        self.KIWI_KEY = kiwi_key
        self.kiwi_url_loc = "https://api.tequila.kiwi.com/locations/query"
        self.kiwi_url_search = "https://api.tequila.kiwi.com/v2/search"
        self.date_today = dt.now()
        self.date_later = self.date_today + relativedelta(months=+6)
        self.date_from = self.date_today.strftime("%d/%m/%Y")
        self.date_to = self.date_later.strftime("%d/%m/%Y")
        self.loc = loc
        # self.data = "TESTING"
        self.kiwi_params_loc = {
            "term": self.loc,
        }
        self.kiwi_params = {
            "fly_from": "PK",
            "fly_to": self.loc,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "curr": "PKR"

        }
        self.header = {
            "apikey": kiwi_api_key
        }
        # self.add_code()
        # self.find_price()
        self.data_iata = ""
        self.data = ""
        # self.data_price = self.data["data"][4]['price']
        self.add_code()
        self.c_data = {
            "price": [],
            "departure city": [],
            "departure iata": [],
            "arrival city": [],
            "arrival iata": [],
            "date": []

        }

    def add_code(self):
        response1 = requests.get(url=self.kiwi_url_loc, params=self.kiwi_params_loc, headers=self.header)
        response1.raise_for_status()
        data_2 = response1.json()
        self.data_iata = data_2["locations"][0]["code"]

    def find_price(self):
        response2 = requests.get(url=self.kiwi_url_search, params=self.kiwi_params, headers=self.header)
        response2.raise_for_status()
        self.data = response2.json()
        length = len(self.data)
        min_price = ""
        date = ""
        for x in range(length):
            if x == 0:
                min_price = self.data["data"][x]["price"]
                date = self.data["data"][x]["local_departure"]
            else:
                if min_price > self.data["data"][x]["price"]:
                    min_price = self.data["data"][x]["price"]
                    date = self.data["data"][x]["local_departure"]
        date_listed = date.split("T")
        date_formatted = date_listed[0]
        self.c_data["arrival city"] = self.data["data"][0]["cityTo"]
        self.c_data["arrival iata"] = self.data["data"][0]["flyTo"]
        self.c_data["departure iata"] = self.data["data"][0]["flyFrom"]
        self.c_data["departure city"] = self.data["data"][0]["cityFrom"]
        self.c_data["price"] = min_price
        self.c_data["date"] = date_formatted


