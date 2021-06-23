import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/aa4d1bc6b9a52d5ae93174997b4fe413/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_response = requests.get(url=SHEETY_ENDPOINT)
        sheety_response.raise_for_status()
        data = sheety_response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def add_iata_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)
