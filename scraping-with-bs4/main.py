import json
from flask import Flask, request, jsonify
from demo import Wikipedia
from datetime import datetime
import logging

logging.basicConfig(filename='app.log',
                level=logging.DEBUG, 
                format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)

@app.get('/get_data')
def get_data_from_wikipedia():
    try:    
        filter = request.args.get("filter", None)
        result = {}

        start_time = datetime.now()
        print(f"the function of scraping started by {start_time} ")
        if filter is not None:
            wk = Wikipedia(filter)
            result = wk.get_data()
        
        end_time = datetime.now()
        print(f"the function of scraping started by {end_time} ")
        
        response = {"data" : result, "status":200, "message":"Successfull."} 
        
        # total time taken in whole the process.
        print(f"the time take in getting data from the web app. => {end_time-start_time}")
        return jsonify(response)
    
    except Exception:
        raise("Getting error in finding result inside the wikipedia")

# run the app
if __name__ == '__main__':
    app.run(debug=True)