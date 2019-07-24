import datetime
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080
BCRYPT_ROUNDS = 12
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=10)
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
JWT_SECRET_KEY = b'\x01\xcf\x82\x07\xdae\xbb\xe9\x81\xbe\x8b\xb7\xb2vt7\xcbd\x88\xc6\x06UQ@'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
