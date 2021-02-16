import requests

def test_post():
    sent_data = {
        "inspection_id": 59980,
        "inspection_date": "2019-10-28",
        "score": 100,
        "comments": "No issues noted at time of inspection. License delivered at time of inspection.",
        "violations": [],
        "restaurant": {
            "restaurant_id": 378,
            "name": "Duke of Yorkshire Pub  ",
            "street_address": "2536 Yorkshire Circle",
            "city": "Wilson",
            "state": "NC",
            "postal_code": ""
        }
    }

    response = requests.post('http://127.0.0.1:5000/api/v1/inspections/post', json=sent_data)
    assert response.status_code == 200

