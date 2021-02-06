from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://bora:password@localhost:3306/Book"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/book.db"


db = SQLAlchemy(app)

from application import routes