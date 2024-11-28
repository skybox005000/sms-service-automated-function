import pandas as pd

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