
import requests
from requests_oauthlib import OAuth1

# Authentication details
auth = OAuth1('consumer_key', 'consumer_secret', 'token_key', 'token_secret')

# Vendor Bill payload
payload = {
    "entity": {"id": "1234"},  # Vendor ID
    "trandate": "2024-09-01",  #// Transaction Date
    "duedate": "2024-09-15",  #// Due Date
    "currency": {
    "id": "1"  #// Currency ID (e.g., USD)
  },
    "terms": {"id": "1"},  # Payment terms
    "item": [
        {
            "item": {"id": "5678"},  # Item ID
            "quantity": 10,  # Quantity of the item
            "rate": 20.00  # Unit price of the item
        }
    ],
    "memo": "Vendor Bill for office supplies"  # Optional memo field
}

def create_vendor_bill(auth, payload):
    url = "https://<account_id>.suitetalk.api.netsuite.com/services/rest/record/v1/vendorBill"
    
    headers = {"Content-Type": "application/json"}
    
    # Send POST request to create the vendor bill
    response = requests.post(url, json=payload, headers=headers, auth=auth)

    return response

# Send the vendor bill creation request
response = create_vendor_bill(auth, payload)

# Response Handling
if response.status_code == 200:
    print("Vendor Bill created successfully:", response.json())
else:
    print("Error creating Vendor Bill:", response.status_code, response.text)