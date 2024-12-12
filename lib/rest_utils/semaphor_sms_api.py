import os
import requests

class Semaphore():

    def __init__(self) -> None:
        self.api_key = os.getenv("SEMAPHORE_SMS_SERVICE_API_KEY")
        self.endpoint = os.getenv("SEMAPHORE_SMS_SERVICE_ENDPOINT")
    
    def send_message_service(self, message, contact_number):
        
        print(f'Sending Message to {contact_number}...')
        return f"<Response [200]>"
        # Intialize post parameters
        # params = (
        #     ('apikey', self.api_key),
        #     ('number', contact_number),
        #     ('message', message)
        #     )
        # # Send post request to Semaphore SMS API and return the status
        # status = requests.post(self.endpoint, params=params)
        # print(status)
        
        
        
# Semaphore().send_message_service("EYYY", "9457416921")