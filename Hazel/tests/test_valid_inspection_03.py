import requests

def test_post():
    sent_data = {
        "inspection_id": 193875,
        "inspection_date": "2020-01-15",
        "score": 99,
        "comments": "",
        "type": "routine",
        "violations": [{
            "violation_id": 4981,
            "is_critical": False,
            "is_repeat": False,
            "is_corrected_on_site": True,
            "code": "25",
            "description": "Personal cleanliness",
            "comments": ""
        }],
        "restaurant": {
            "restaurant_id": 201,
            "details": {
            "cuisine_type": "fast casual"
            },
            "name": "SKINNER'S DINNERS",
            "street_address": "3325-A SKINNER HOLLOW RD",
            "city": "HAINES",
            "state": "OR",
            "postal_code": "97833"
        }
    }

    response = requests.post('http://127.0.0.1:5000/api/v1/inspections/post', json=sent_data)
    assert response.status_code == 200

