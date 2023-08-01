import random
import string

from flask import Flask, jsonify, request
from sub1_restful import sub1_restful_api
from sub2_restful import sub2_restful_api

app = Flask(__name__)

# 蓝图
app.register_blueprint(sub1_restful_api)
app.register_blueprint(sub2_restful_api)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)
