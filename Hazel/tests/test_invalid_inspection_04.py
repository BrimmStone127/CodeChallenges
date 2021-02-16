import requests

def test_post():
    sent_data = {
        "inspection_id": 34078,
        "inspection_date": "2018-06-02",
        "score": 94,
        "comments": "restaurant address components must be well-formed",
        "violations": [{
            "violation_id": 1004,
            "is_critical": True,
            "code": "5",
            "description": "Hands clean and properly washed",
            "comments": ""
        }],
        "restaurant": {
            "restaurant_id": 201,
            "name": "SKINNER'S DINNERS",
            "street_address": "3325-A",
            "city": "",
            "state": "OREGON",
            "postal_code": "9783"
        }
    }

    response = requests.post('http://127.0.0.1:5000/api/v1/inspections/post', json=sent_data)
    assert response.status_code == 400

