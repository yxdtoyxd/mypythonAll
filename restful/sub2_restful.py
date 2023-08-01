import random
import string

from flask import Flask, jsonify, request

from flask import Blueprint

app = Flask(__name__)

sub2_restful_api = Blueprint('sub2_api', __name__)

@sub2_restful_api.route('/api/num2', methods=['GET'])
def get_num():
    """
    无参
    curl -X GET 'http://192.168.1.110:8001/api/num'
    """
    return {'number': random.randint(100, 5000)}


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8001, debug=True)
