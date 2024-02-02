import uuid
from sqlalchemy import Uuid
from alexandria_library import db

class User(db.Model):
    id = db.Column(Uuid, primary_key=True, default=uuid.uuid4)