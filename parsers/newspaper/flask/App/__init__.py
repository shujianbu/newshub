from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://newshub:columbiacuj@newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com/Newshub'
db = SQLAlchemy(app)

from app import models
