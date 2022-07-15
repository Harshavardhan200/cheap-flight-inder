from notification_manager import NotificationManager
from flight_data import FlightData
import requests
website = "https://tequila-api.kiwi.com"
api_key = "7MemlqWT89YkakDo7I6-tsTnC4ZkN07i"
class FlightSearch:
    def search(self, city):
        query = {'term': city, 'location_types': 'city'}
        headers = {'apikey': api_key}
        result = requests.get(url=f'{website}/locations/query', params=query, headers=headers)
        return result.json()['locations'][0]['code']
    def flight_search(self, from_, to_, from_iata, to_iata, price, city):
        search = f'{website}/v2/search'
        query = {
            'fly_from': from_iata,
            'fly_to': to_iata,
            'date_from': from_,
            'date_to': to_,
            'curr': 'GBP'
        }
        headers = {'apikey': api_key}
        try:
            data = requests.get(search, params=query, headers=headers).json()['data'][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            if min(price, flight_data.price) == flight_data.price:
                notify = NotificationManager()
                notify.notification(price=flight_data.price, arrival=flight_data.destination_airport, departure=flight_data.origin_airport, departure_iata=from_iata, arrival_iata=to_iata, date_=from_, to_date=to_)
                return flight_data.price
        except IndexError:
            print(f'no flights for {city}')
            return 0