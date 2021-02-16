Hazel Code Challenge 11/15/2020
Clay Brimm

TO RUN:
In a terminal move into the /api directory with 'cd /api'. Make sure Python3 is installed and use pip to install the requirements to run the flask app
'pip install -r requirements.txt' (This can be done in a python virtual environment). To run the server just type 'python api.py' and the development
server will run at http://127.0.0.1:5000/
The REST endpoints are:
    GET restaurant summary: http://127.0.0.1:5000//api/v1/restaurant/summary' 
    GET inspection: http://127.0.0.1:5000//api/v1/inspections/get' 
    POST inspection: http://127.0.0.1:5000//api/v1/inspections/post' 

TO RUN UNIT TESTS USING pytest: 
- Stop the api.py server with CTRL+C and delete data.txt from the /api directory. Restart the server with 'python api.py' and an empty data.txt 
should be created.
- In a separate terminal go to the /api directory and type pytest to run through the test files in the /tests directory.








          (__)            
          (oo)  (Have a nice day!)
   /-------\/      
  / |     ||
 *  ||----||
    ^^    ^^   