import os

class Config:
    SECRET_KEY = '352b6fb4ef6d6138f10698066b2b1bf6' #os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USER')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')