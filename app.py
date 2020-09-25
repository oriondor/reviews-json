import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello():
	prods = Products.query.all()
	print(prods)
	return {'products':'prods'}

if __name__ == '__main__':
	app.run()