from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='../templates')

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/Book"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/book1d52.db"
#app.config["SQLALCHEMY_DATABASE_URI"]= "mysql + mysqldb://root:root@34.105.221.30/Book/red-alloy-301014:europe-west2:sakila"


db = SQLAlchemy(app)

from application import routes