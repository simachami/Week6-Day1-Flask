from flask import Flask
from Config import Config


app = Flask(__name__)
app.config.from_object(Config)


#Must be at bottom of file prevent circular import
from app import routes