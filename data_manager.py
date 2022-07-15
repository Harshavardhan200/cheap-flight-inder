import requests
from flight_search import FlightSearch
authonication = {'Authorization': 'Bearer harsha'}
api_website = 'https://api.sheety.co/eaba58af987cb300cc3aa4e81a1bc83c/flightDeal/prices'
class DataManager:
    def __init__(self):
        self.destination = {}
    def data_of_sheets(self):
        self.destination = requests.get(url=api_website).json()
        return self.destination
    def destination_codes(self):
        flight = FlightSearch()
        for i in self.destination['prices']:
            print('hello')
            data = {'price': {'iataCode': flight.search(i['city'])}}
            response = requests.put(url=f'{api_website}/{i["id"]}', json=data, headers=authonication)
            self.destination = response.json()