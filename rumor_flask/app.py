from database import database_config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = b'rumor_killer'
app.config.from_object(database_config)
db = SQLAlchemy(app)
# db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




