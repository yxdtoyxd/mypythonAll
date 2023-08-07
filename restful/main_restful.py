import random
import string

from flask import Flask, jsonify, request
from sub1_restful import sub1_restful_api
from sub2_restful import sub2_restful_api

app = Flask(__name__)

# blueprint
app.register_blueprint(sub1_restful_api)
app.register_blueprint(sub2_restful_api)

@app.route('/api/num', methods=['GET'])
def get_num1():
    return {'number': random.randint(100, 5000)}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
