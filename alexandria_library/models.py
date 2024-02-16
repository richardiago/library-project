import uuid
from datetime import datetime
from sqlalchemy import Uuid
from alexandria_library import db

class User(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile = db.Column(Uuid, db.ForeignKey('users_profiles.id'), nullable=False)
    registerDate = db.Column(db.Date, nullable=False, default=datetime.today())

    borrows = db.relationship('BookBorrowing', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"
    
class Book(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(60), nullable=False)
    publishDate = db.Column(db.Date, nullable=False)
    registerDate = db.Column(db.Date, nullable=False, default=datetime.today())

    borrows = db.relationship('BookBorrowing', backref='book', lazy=True)
    genres = db.relationship('Genre', secondary='book_genre', backref=db.backref('books', lazy='dynamic'))

    def __repr__(self):
        return f"Book('{self.name}', '{self.author}')"
    
class BookStock(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)
    bookId = db.Column(Uuid, db.ForeignKey('book.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    registerDate = db.Column(db.Date, nullable=False, default=datetime.today())

    def __repr__(self):
        return f"BookStock('{self.bookId}', '{self.quantity}')"
    
class Genre(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), nullable=False)
    registerDate = db.Column(db.Date, nullable=False, default=datetime.today())

    def __repr__(self):
        return f"Genre('{self.name}')"
    
class BookGenre(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)
    bookId = db.Column(Uuid, db.ForeignKey('book.id'), nullable=False)
    genreId = db.Column(Uuid, db.ForeignKey('genre.id'), nullable=False)
    registerDate = db.Column(db.Date, nullable=False, default=datetime.today())

    def __repr__(self):
        return f"BookGenre('{self.book_id}', '{self.genre_id}')"
    
class UsersProfiles(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)
    profile = db.Column(db.String(80), nullable=False, unique=True)
    registerDate = db.Column(db.Date, nullable=False, default=datetime.today())

    def __repr__(self):
        return f"User Profile('{self.profile}')"
    
class BookBorrowing(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)
    userId = db.Column(Uuid, db.ForeignKey('user.id'), nullable=False)
    bookId = db.Column(Uuid, db.ForeignKey('book.id'), nullable=False)
    returnDate = db.Column(db.Date, nullable=False)
    registerDate = db.Column(db.Date, nullable=False, default=datetime.today())

    def __repr__(self):
        return f"BookBorrowing('{self.userId}', '{self.bookId}', '{self.registerDate}', '{self.returnDate}')"