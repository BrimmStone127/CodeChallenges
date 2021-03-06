import requests

def test_post():
    sent_data = {
        "inspection_id": 34078,
        "inspection_date": "2018-06-02",
        "score": 88,
        "comments": "Discussed employee illness policy with PIC. Discussed clean up procedures with PIC.",
        "violations": [{
            "violation_id": 1004,
            "is_critical": True,
            "code": "5",
            "description": "Hands clean and properly washed",
            "comments": "Observed BOH employee handle raw chicken, rinse hands w/ water only, then handle non-food-contact surfaces and money. Corrected on site with notice to PIC."
        }, {
            "violation_id": 1005,
            "is_critical": True,
            "code": "6",
            "description": "Proper hot holding temperatures",
            "comments": "Chicken @145f, beef @138f"
        }, {
            "violation_id": 1006,
            "is_critical": False,
            "code": "27",
            "description": "Gloves used properly",
            "comments": ""
        }, {
            "violation_id": 1007,
            "is_critical": True,
            "code": "8",
            "description": "Toxic substances properly identified, stored, and used",
            "comments": "Sanitizer stored above produce (COS)"
        }],
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
    assert response.status_code == 200

