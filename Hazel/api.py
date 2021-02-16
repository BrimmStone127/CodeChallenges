import flask
from flask import request, jsonify
import json
import datetime
import os.path
from os import path
import re

# 11/15/2020 Hazel Analytics Code Challenge
# Author: Clay Brimm
# REQUIREMENTS: 
# [X] Receive a JSON payload representing a public health inspection at a restaurant. The payload should be validated, then stored if valid. Whether
#     the payload is valid or invalid, an appropriate response should be returned.
# [X] Given an inspection ID, return the associated record.
# [X] [If time permits] Given a restaurant ID, return a summary of its inspection history based on all stored inspections. The summary should contain
#     dates and IDs of the restaurant's inspections, the average inspection score, and the average number of violations per inspection
# [X] In addition to these endpoints, write basic unit tests that support your validation logic.

# This application was made with Python 3.9.0 and Python Flask 1.1.2

# Records are saved in a json object stored in a text file named data.txt. When first running the application the data.txt file should be 
# automatically created. 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Check to make sure data.txt exists
if(not path.exists('data.txt')):
    # If data.txt does not exist: create it with an empty inspections array
    new_data = {}
    new_data['inspections'] = []
    with open('data.txt', 'w') as outfile:
        json.dump(new_data, outfile)

# This is the GET endpoint for the restaurant summary. It should accept a restaurant_id argument and then go through the stored JSON file
# and return all inspection IDs and inspection dates that have a matching restaurant_id, it will also return the restaurant's average 
# inspection score and the average violations per inspection
@app.route('/api/v1/restaurant/summary', methods=['GET'])
def get_restaurant_summary():
    if 'restaurant_id' in request.args:
        with open('data.txt') as json_file:
            stored_data = json.load(json_file)
            arg_id = int(request.args['restaurant_id'])
            summary_string = 'Restaurant Summary: '
            inspection_ids = []
            inspection_dates = []
            inspection_count = 0
            inspection_score_sum = 0
            violation_sum = 0
            for p in stored_data['inspections']:
                if(p['restaurant']['restaurant_id'] == arg_id):
                    inspection_count += 1
                    inspection_score_sum += int(p['score'])
                    violation_sum += len(p['violations'])
                    inspection_ids.append(str(p['inspection_id']))
                    inspection_dates.append(str(p['inspection_date']))
            if(inspection_count > 0):
                inspection_score_avg = str(inspection_score_sum / inspection_count)
                violation_avg = str(violation_sum / inspection_count)
                summary = {
                    "inspection_ids":inspection_ids,
                    "inspection_dates":inspection_dates,
                    "inspection_score_average": inspection_score_avg,
                    "violations_average": violation_avg
                }
                return(summary)
            else:
                error_msg = {'request_status'}
                return({'Error': 'There are no inspections with that restaurant_id'}, 400)

# GET method that returns the associated method to the given inspection_id
@app.route('/api/v1/inspections/get', methods=['GET'])
def get_inspection():
    if 'inspection_id' in request.args:
            with open('data.txt') as json_file:
                stored_data = json.load(json_file)
                arg_id = int(request.args['inspection_id'])
                for p in stored_data['inspections']:
                    if(p['inspection_id'] == arg_id):
                        return(str(p))
                return({'error': 'given inspection_id does not exist'}, 400)
    else:
        error_msg = {'error': 'inspection_id not provided. Please provide an inspection_id in the arguments of the GET request.'}
        return (error_msg, 400)

# POST method that will take in a inspection json and validate it and if valid will store it in data.txt.
@app.route('/api/v1/inspections/post', methods=['POST'])
def inspection_post():
    req_data = request.get_json()
    # validate_json will return an array of errors
    error_array = validate_json(req_data)

    # If there are no errors then write to data.txt and return a success message
    if not error_array:
        with open('data.txt') as json_file:
            data = json.load(json_file)
            temp = data['inspections']
            temp.append(req_data)
        write_json(data)
        return({'success':'JSON successfully posted'},200)
    else:
        error_json = {'errors': error_array}
        return(error_json, 400)

# This separate function will take in the posted json and validate it based off the requirements I gathered from the example valid
# and invalid inspections.  
def validate_json(json_data):
    req_data = json_data
    error_array = []

    try:
        # From looking through the given invalid inspections, these variables should represent what I believe to be the required 
        # fields for a post to be valid. The try-except will look for a key error to make sure all necessary fields exist.
        inspection_id = req_data['inspection_id']
        inspection_date = req_data['inspection_date']
        score = req_data['score']
        comments = req_data['comments']
        violations = req_data['violations']
        restaurant = req_data['restaurant']
        state = restaurant['state']
        city = restaurant['city']
        street_address = restaurant['street_address']
        postal_code = restaurant['postal_code']

        # Iterate over stored data to see if the new inspection_id already exists
        with open('data.txt') as json_file:
                stored_data = json.load(json_file)
                for p in stored_data['inspections']:
                    if(p['inspection_id'] == inspection_id):
                        error_array.append('inspection_id already exists')        

        # Try - Except that will check if the date is formatted to YYYY-MM-DD
        try:
            inspection_datetime = datetime.datetime.strptime(inspection_date, '%Y-%m-%d')
            current_datetime = datetime.datetime.now()
            # Check to make sure the inspection date is not greater then the current datetime
            if(inspection_datetime > current_datetime):
                error_array.append('inspection_date is not possible')
        except ValueError:
            error_array.append( 'inspection_date needs to be formatted YYYY-MM-DD')

        # Check that the score is in between 0-100
        if(score < 0 or score > 100):
            error_array.append('Inspection score must be 0-100')

        #Check if state has a length of 2 and is only made of letters (this should be faster then a regex)
        if(len(state) != 2 and state.isalpha() != True):
            error_array.append('Restaurant state needs to abbreviated to two characters')

        #Regex to check for 4 digit house number with optional apartment number or letters followed by street name
        address_regex = re.compile(r'\d{1,4}(-\w+)?\s.*')
        match_object = address_regex.match(street_address)
        if(not match_object):
            error_array.append('Street Address is not formatted properly')

        #Regex to check city name
        city_regex = re.compile(r'^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$')
        match_object = city_regex.match(city)
        if(not match_object or len(city) < 2):
            error_array.append('City name is not formatted properly')

        #Postal code is not required but if it is given it should be 5 digits
        if(len(postal_code) != 5 and len(postal_code) != 0):
            error_array.append('Postal code must be 5 digits long')

    #Key error should catch any required json fields that are missing
    except KeyError as e:
        error_array.append('Required key is missing: "%s"' % str(e))
    
    return error_array

# Function to write to the stored data - data.txt
def write_json(data):
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

app.run()