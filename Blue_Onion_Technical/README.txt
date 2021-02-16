# Blue Onion Labs Take Home Test

Hey! We are stoked that you are interested in joining the team at Blue Onion Labs.

We have crafted the following test to see how you approach pulling and manipulating of data. We want to get a general idea of how you approach some common types of problems that we encounter here at Blue Onion (we are really proficient at integrations!)

## Background
[spacexdata.com](https://docs.spacexdata.com/) provides an API to query attributes about SpaceX launches (https://github.com/r-spacex/SpaceX-API/blob/master/docs/v4/README.md). For this exercise we are going to be working with one resource in particular:
- The [Starlink Schema](https://github.com/r-spacex/SpaceX-API/blob/master/docs/v4/starlink/schema.md)

*For this exercise, no need to pull directly from the API as we have a pull of historical data here in this repo in the starlink_historical_data.json*

## The Problem:
We want to be achieve a few goals:
  - To import the SpaceX Satellite data _as a time series_ into a database
  - To be able to query the data to determine the last known latitude/longitude of the satellite for a given time

## The Task (Part 1):

Stand up your favorite kind of database (and ideally it would be in a form that would be runnable by us, via something like docker-compose).

## The Task (Part 2):

Write a script (in whatever language that you prefer, though Ruby, Python, or Javascript would be ideal for us) to import the relevant fields in starlink_historical_data.json as a time series. The relevant fields are:
    - spaceTrack.creation_date (represents the time that the lat/lon records were recorded)
    - longitude
    - latitude
    - id (this is the starlink satellite id)
Again, the goal is that we want to be able to query the database for the last known position for a given starlink satellite.
Don't hesitate to use any tools/tricks you know to load data quickly and easily!

## The Task (Part 3):

Write a query to fetch the the last known position of a satellite (by id), given a time T. Include this query in your README or somewhere in the project submission

## Bonus Task (Part 4):

Write some logic (via a combination of query + application logic, most likely) to fetch from the database the _closest_ satellite at a given time T, and a given a position on a globe as a (latitude, longitude) coordinate.

No need to derive any fancy match for distances for a point on the globe to a position above the earth. You can just use the Haversine formula. Example libraries to help here:

For Python: https://github.com/mapado/haversine

For Ruby: https://github.com/kristianmandrup/haversine



TO RUN

Requirements
- Python3
- psycopg2
- Docker

1. Pull Postgres Docker image
docker pull postgres

2. Setup postgres database named dev-postgres to run locally on port 5432
docker run -d --name dev-postgres -p 5432:5432 -e POSTGRES_PASSWORD=admin123 postgres

3. Open the instances bash shell and then connect to the database using psql
docker exec -it dev-postgres bash
psql -h localhost -U postgres

4. Using the psql shell, create a table named starlink to store all of our data
CREATE TABLE starlink (id serial PRIMARY KEY, creation_date TIMESTAMP, satellite_id VARCHAR(50), longitude INT, latitude INT);

5. Run the python script starlink.py to parse the starlink historical data and insert it into the starlink db.
python startlink.py

6. Using the psql terminal again, use this query to find the long and lat of a specific satellite at a given time
SELECT longitude, latitude FROM starlink WHERE satellite_id = '60106f1fe900d60006e32cb2' AND creation_date = '2020-08-19 06:26:10';


         (__)   (Have a nice day!) 
         (oo)    
  /-------\/     
 / |     ||
*  ||----||
   ^^    ^^   
