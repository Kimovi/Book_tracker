from application import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(30))
    author = db.Column(db.String(30))    
    users_data = db.relationship('Users', backref='book')


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30))
    user_email = db.Column(db.String(30))
    start_date = db.Column(db.String(30))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

