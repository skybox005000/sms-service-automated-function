from lib.utils.utilities import Utilities
from lib.rest_utils.semaphor_sms_api import Semaphore

class MessageService():

    def __init__(self) -> None:
        self.utils = Utilities()
        self.semaphore = Semaphore()

    def send_billing_due(self, data):
        
        # Initialize total messages counter
        sent_message_counter = 0
        failed_message_counter = 0

        # Client information extraction
        for client_info in data:
            name = client_info['client_name']
            contact_number = str(client_info['contact_number'])
            billing_due = str(client_info['due'])
            billing_amount = client_info['billing_due']
            billing_due = billing_due.replace('.0', '')
            contact_number = contact_number.replace('.0', '')

            # Create and retrieve billing message
            billing_prompt = self.utils.create_billing_due_prompt(name, billing_due, billing_amount)

            if len(contact_number) == 10:
            # Send sms using Semaphore API and retrieve the status
                sms_status = self.semaphore.send_message_service(billing_prompt, contact_number)
            else:
                sms_status = "Failed"
                print("Invalid Contact Number")
            # Check the status and summarize the total count
            if sms_status == "<Response [200]>":
                print(f'Message Sent!\nClient Name: {name}\nContact Number: {contact_number}')
                sent_message_counter += 1
            else:
                print(f'Message Sending Failed!\nClient Name: {name}\nContact Number: {contact_number}')
                failed_message_counter += 1
                
        # Create return object for message summary
        summary = {
            "total_sent": sent_message_counter,
            "total_failed": failed_message_counter
        }
        
        return summary

        
