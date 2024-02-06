from datetime import datetime
import uuid
from sqlalchemy import Uuid
from alexandria_library import db

class User(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    registerDate = db.Column(db.Date, nullable=False, default=datetime.today())
    registerDate2 = db.Column(db.Date, nullable=False, default=datetime.today())

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"
    
class Book(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)