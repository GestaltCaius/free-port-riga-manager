from app import models
from flask_restful import Resource, reqparse
import flask_jwt_extended as jwt
import datetime


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='This field cannot be blank.')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank.')

    def post(self):
        data = self.parser.parse_args()
        user = models.User.first(email=data['email'])
        if not user or not user.has_password(data['password']):
            return {'message': 'Login failed'}

        access_token = jwt.create_access_token(identity=user.id)
        refresh_token = jwt.create_refresh_token(identity=user.id)

        return {
            'message': 'Login success',
            'access_token': access_token,
            'refresh_token': refresh_token
        }


class LogoutAccess(Resource):
    @jwt.jwt_required
    def post(self):
        try:
            models.RevokedToken.remove_expired_tokens()
            models.RevokedToken.new(jwt.get_raw_jwt()).add()
            return {'message': 'Access token logout successful'}
        except:
            return {'message': 'Error'}


class LogoutRefresh(Resource):
    @jwt.jwt_refresh_token_required
    def post(self):
        try:
            models.RevokedToken.remove_expired_tokens()
            models.RevokedToken(jti=jwt.get_raw_jwt()['jti']).add()
            return {'message': 'Refresh token logout successful'}
        except:
            return {'message': 'Error'}


class TokenRefresh(Resource):
    @jwt.jwt_refresh_token_required
    def post(self):
        return {'access_token': jwt.create_access_token(identity=jwt.get_jwt_identity())}


class UserIsLoggedIn(Resource):
    @jwt.jwt_required
    def get(self):
        return {'message': 'OK'}


class UserProfile(Resource):
    @jwt.jwt_required
    def get(self):
        print(jwt.get_raw_jwt())
        user = models.User.first(id=jwt.get_jwt_identity())
        if not user:
            return {'message': 'Error'}

        return {
            'message': 'User profile',
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone': user.phone,
            'is_forwarder': user.is_forwarder
        }
