import unittest 
from flask_testing import TestCase
from flask import url_for
from application import app, db
from application.models import Book, Users

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLAlCHEMY_DATABASE_URI= "sqlite:////")
        return app

    def setUp(self):
        db.create_all()
        sample = Book(book_title="Shark", author="James")
        sample1 = Users(user_name="bora", user_email="borakim@gmail.com")
        db.session.add(sample)
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestAccess(TestBase):
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_access_user(self):
        response = self.client.get(url_for('user_home'))
        self.assertEqual(response.status_code, 200)

    def test_access_user_home(self):
        response = self.client.get(url_for('user_home', Title="Users"), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data = dict(book_title="Shark")
        )
        self.assertIn(b'MrMan',response.data)
            
    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data = dict(book_title="Shark")
        )
        self.assertIn(b'Shark',response.data)

    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data = dict(author="James")
        )
        self.assertIn(b'James',response.data)

class TestUpdate(TestBase):
    def test_data_update_book_title(self):
        response = self.client.post(
            url_for('update'),
            data = dict(current_book_title="Shark", newname="bad"),
            follow_redirects= True
            )
        self.assertEqual(response.status_code, 200)

    def test_data_update_name(self):
        response = self.client.post(
            url_for('update_user'),
            data = dict(id=1, newname="Smith"),
            follow_redirects = True
            )
        self.assertEqual(response.status_code, 200)


class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(
            url_for('delete'),
            data = dict(book_title="Shark"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)

    def test_delete_post3(self):
        response = self.client.post(
            url_for('delete_user'),
            data = dict(id=1),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)
