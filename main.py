from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from users_database import Users
flight = FlightSearch()
account = input('Do you want to create the account, Type yes or no:')
dat = Users()
if account == 'yes':
    dat.users()
data = DataManager()
sheets = data.data_of_sheets()
for i in sheets['prices']:
    if i['iataCode'] == '':
        data.destination = sheets
        data.destination_codes()
        sheets = data.data_of_sheets()
date_from = (datetime.now() + timedelta(days=1)).strftime('%d/%m/%Y')
date_to = (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y")
for i in sheets['prices']:
    da = flight.flight_search(date_from, date_to, 'IND', i['iataCode'], price=i['lowestPrice'], city=i['city'])
    if da:
        dat.data_update(da, i['id'])