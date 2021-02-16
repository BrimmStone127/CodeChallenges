import requests

def test_post():
    sent_data = {
        "inspection_id": 34078,
        "score": -1,
        "comments": "multiple types of invalid behavior",
        "violations": [{
            "is_critical": "true",
            "code": "5",
            "description": None,
            "comments": ""
        }],
        "restaurant": {
            "restaurantID": 201,
            "name": "",
            "street_address": "SKINNER HOLLOW RD",
            "city": "HAINES",
            "state": "ORR",
            "postal_code": "97833-022"
        }
    }

    response = requests.post('http://127.0.0.1:5000/api/v1/inspections/post', json=sent_data)
    assert response.status_code == 400

