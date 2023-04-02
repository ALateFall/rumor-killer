from database import database_config
from flask import Flask
from api import init_view
from flask_cors import CORS
from database.database import db
import time
import threading
import requests


last_time = 0
app = Flask(__name__)
app.secret_key = b'rumor_killer'
app.config.from_object(database_config)
db.init_app(app)
CORS(app)
init_view(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.before_request
def before_request():
    global last_time
    if time.time() - last_time > 300:
        last_time = time.time()
        thread = threading.Thread(target=visit_url)
        thread.start()


def visit_url():
    requests.get('http://localhost:5000/tweets/makeScrape')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




