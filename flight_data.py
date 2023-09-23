from data_manager import DataManager
from flight_search import FlightSearch

class FlightData:
    def __init__(self):
        self.data = DataManager()
        self.code = self.data.dict["IATA Code"]
        self.prices = {
            "loc":[],
            "price":[]
        }
        for x in self.code:
            self.flights= FlightSearch(x)
            self.prices["loc"].append(self.flights.kiwi_params["fly_to"])
            self.prices["price"].append(self.flights.data_price)



