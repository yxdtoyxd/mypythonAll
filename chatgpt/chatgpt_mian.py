
from flask import Flask
from chatgpt_init import chatgpt_init_app
from chatgpt_plus import chatgpt_plus_app

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# blueprint
app.register_blueprint(chatgpt_init_app)
app.register_blueprint(chatgpt_plus_app)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
