import requests

def test_post():
    sent_data = {
        "inspection_id": 34078,
        "inspection_date": "2018-06-02",
        "score": 94,
        "comments": "violations array must exist",
        "restaurant": {
            "restaurant_id": 201,
            "name": "SKINNER'S DINNERS",
            "street_address": "3325-A SKINNER HOLLOW RD",
            "city": "HAINES",
            "state": "OR",
            "postal_code": "97833"
        }
    }

    response = requests.post('http://127.0.0.1:5000/api/v1/inspections/post', json=sent_data)
    assert response.status_code == 400

