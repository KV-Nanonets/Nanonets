
import requests
from requests_oauthlib import OAuth1

# Authentication details
auth = OAuth1('consumer_key', 'consumer_secret', 'token_key', 'token_secret')

#sales order payload
payload = {
    "entity": {"id": "1234"},  # Customer ID
    "trandate": "2024-09-01",  # Transaction Date
    "duedate": "2024-09-15",  # Due Date
    "currency": {"id": "1"},  # Currency ID (USD)
    "terms": {"id": "1"},  # Payment terms
    "item": [
        {
            "item": {"id": "5678"},  # Item ID
            "quantity": 10,  # Quantity
            "rate": 20.00  # Unit price
        }
    ],
    "memo": "Sales order for office supplies"
}

def create_sales_order(auth, payload):
    url = "https://<account_id>.suitetalk.api.netsuite.com/services/rest/record/v1/salesOrder"
    
    headers = {"Content-Type": "application/json"}
    
    # Send POST request to create the sales order
    response = requests.post(url, json=payload, headers=headers, auth=auth)

    return response


# Send the sales order creation request
response = create_sales_order(auth, payload)

# Response Handling
if response.status_code == 200:
    print("Sales Order created successfully:", response.json())
else:
    print("Error creating Sales Order:", response.status_code, response.text)