from flask import Flask
from actions import bp as actionsbp
from filters import bp as filtersbp
from android import bp as androidbp


app = Flask(__name__)
app.secret_key = 'SECRET_KEY'


app.register_blueprint(actionsbp)
app.register_blueprint(filtersbp)
app.register_blueprint(androidbp)