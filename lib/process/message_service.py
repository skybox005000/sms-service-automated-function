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
            name = client_info['clientName']
            contact_number = str(client_info['contactNumber'])
            billing_due = str(client_info['dueDate'])
            billing_amount = client_info['amount']

            # Create and retrieve billing message
            billing_prompt = self.utils.create_billing_due_prompt(name, billing_due, billing_amount)

            if len(contact_number) == 10:
            # Send sms using Semaphore API and retrieve the status
                if self.utils.is_due_date_alert(billing_due):
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

        
