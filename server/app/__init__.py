from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# App initialization
app = Flask(__name__)
app.config.from_object('config')

# Flask modules initialization
api = Api(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

# Import remaning files
from app import models, resources, debug

# Register API resources
api.add_resource(debug.Exec, '/debug/exec')
api.add_resource(debug.UserAdd, '/debug/useradd')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.Login, '/login')
api.add_resource(resources.LogoutAccess, '/logout/access')
api.add_resource(resources.LogoutRefresh, '/logout/refresh')
api.add_resource(resources.UserProfile, '/user/profile')
api.add_resource(resources.UserIsLoggedIn, '/user/isloggedin')

# Setup JWT token blacklist checking routine
@jwt.token_in_blacklist_loader
def token_blacklist_checker(token):
    return models.RevokedToken.is_blacklisted(token['jti'])
