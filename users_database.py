mail = 'https://api.sheety.co/eaba58af987cb300cc3aa4e81a1bc83c/flightDeal/users'
import requests
class Users:
    def users(self):
        first_name = input('Enter your first name:')
        last_name = input('Enter your Last Name:')
        email = input('enter your mail:')
        a_email = input('enter mail other time:')
        if email == a_email:
            authonication = {'Authorization': 'Bearer harsha'}
            query = {
                'user': {
                    'firstName': first_name,
                    'lastName': last_name,
                    'email': email
                }
            }
            message = requests.post(mail, json=query, headers=authonication)
        else:
            print('invalid mail')
    def data_update(self, price, i):
        api_website = 'https://api.sheety.co/eaba58af987cb300cc3aa4e81a1bc83c/flightDeal/prices'
        authonication = {'Authorization': 'Bearer harsha'}
        query = {
            'price': {
                'lowestPrice': price
            }
        }
        response = requests.put(f'{api_website}/{i}', json=query, headers=authonication)