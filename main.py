import os
import requests
from lib.utils.utilities import Utilities
from lib.process.message_service import MessageService

messaging_service = MessageService()
utils = Utilities()

def main():
    billing_cycle = utils.check_billing_cycle()
    base_url = 'http://127.0.0.1:5000/api/billing/sms'  
    params = {'billingCycle': billing_cycle}  
  
    response = requests.get(base_url, params=params)  
  
    if response.status_code == 200:  
        print(response.json())
    else:  
        print("ERROR")
    status = messaging_service.send_billing_due(response.json())
    print(status)


main()