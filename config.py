import os
class Config:
    SECRET_KEY = 'mysecertpass123'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:jassu123@localhost/library_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'jwt-secret-key'