from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://bora:password@localhost:3306/Book"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/dummmm1.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from application import routes