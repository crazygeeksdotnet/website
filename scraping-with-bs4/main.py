import json
from flask import Flask, request, jsonify
from demo import Wikipedia

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

        if filter is not None:
            wk = Wikipedia(filter)
            result = wk.get_data()
        
        
        response = {"data" : result, "status":200, "message":"Successfull."} 
        return jsonify(response)
    except Exception:
        raise("Getting error in finding result inside the wikipedia")

# run the app
if __name__ == '__main__':
    app.run(debug=True)