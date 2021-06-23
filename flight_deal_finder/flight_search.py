import requests
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = 'BOqwdmxWFCBqflG5JMlVXpEsTaCJ1FZG'

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_search(self)

    def flight_search(self, city):
        # parameters = {
        #     "term": city
        # }        # headers = {
        #         #     "apikey": TEQUILA_API_KEY
        #         # }

        # response = requests.get(url=TEQUILA_ENDPOINT, params=parameters, headers=headers)
        # response.raise_for_status()
        # flight_data = response.json()
        # pprint(flight_data)
        # return flight_data
        return "TESTING"
