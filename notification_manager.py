from twilio.rest import Client
mail1 = 'https://api.sheety.co/eaba58af987cb300cc3aa4e81a1bc83c/flightDeal/users'
import requests
import smtplib
class NotificationManager:
    def notification(self, price, arrival, departure, arrival_iata, departure_iata, date_, to_date):
        message = f'Low price alert! Only, ₹{int(price * 100.83)} to fly from {departure}-{departure_iata} to {arrival}-{arrival_iata} from {date_} to {to_date}'
        account_id = 'AC924b47a2ebc71d5f1ebe8bda97013d88'
        authonicated = 'bf6deb4d3aa75bed81859bb0f35d2098'
        authonication = {'Authorization': 'Bearer harsha'}
        con = Client(account_id, authonicated)
        mess = con.messages.create(body=message, from_='+15074787107', to='+918309197541')
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com') as connection:
                mail = 'rudraprathap851@gmail.com'
                password = 'harsha13062002@'
                data = requests.get(mail1).json()['users']
                names = [f"{row['firstName']} {row['lastName']}" for row in data]
                emails = [f"{row['email']}" for row in data]
                connection.login(user=mail, password=password)
                if len(names) == len(emails):
                    for i in range(len(names)):
                        connection.sendmail(from_addr=mail, to_addrs=emails[i], msg=f"subject:low price drop!\nmain body:Hey harsha,\n {message}")
                        print('message sent')
        except:
            pass


