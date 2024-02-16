import requests
import json

URL = "http://127.0.0.1:8000/delivery_cost/"
# ********************* get total of delivery_cost **************** 
def get_data(id = None):
    data = {'zone': "central", 
            'organization_id': "3",
            'total_distance': 100, 
            'item_type': "Perishable" # Non-Perishable / Perishable
    }

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

get_data()