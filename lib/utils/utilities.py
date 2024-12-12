import pandas as pd
from datetime import datetime, timedelta 

class Utilities():

    def __init__(self) -> None:
        pass

    def create_billing_due_prompt(self, client_name, billing_due, billing_amout) -> str:
        
        prompt = f"""Hi {client_name},
        This is a friendly reminder about an outstanding balance of P{billing_amout} for your internet bill, due every {billing_due}th of the month.
        Kindly disregard this message if already paid.
        
        You can pay through GCash or by visiting our office.
        
        Thank you!

        G-NET San Miguel"""

        return prompt
    
    def read_csv(self, file_name):
        df = pd.read_csv(file_name, encoding='latin-1')
        data = df.to_dict(orient='records')
        # print(data)
        return data
    
    def check_billing_cycle(self):
        # Get the current date  
        current_date = datetime.now()  
        
        # Add 7 days to the current date  
        new_date = current_date + timedelta(days=7)  
        
        # Convert the new date to the desired format  
        formatted_date = new_date.strftime('%B %Y')

        return formatted_date 

    def is_due_date_alert(self, due_date_str):    
        
        # Convert the due date string to a datetime object  
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')  
        
        # Calculate the difference between the due date and the current date  
        days_till_due = (due_date - datetime.now()).days  
        print(f"DAYS TIL DUE: {days_till_due}")
        # Check if the difference is 7 days or less  
        if days_till_due == 7:  
            return True 
        else:
            return False