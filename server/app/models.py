from app import db
from datetime import datetime
from flask import current_app
from passlib.hash import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class BaseMixin:

    @classmethod
    def find(cls, **kwargs):
        return cls.query.filter_by(**kwargs)

    @classmethod
    def first(cls, **kwargs):
        return cls.find(**kwargs).first()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def save(self):
        db.session.commit()


class User(db.Model, BaseMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    phone = db.Column(db.String(64), nullable=False)
    is_forwarder = db.Column(db.Boolean, nullable=False)
    _password = db.Column('password', db.String(72), nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.using(rounds=current_app.config['BCRYPT_ROUNDS']).hash(plaintext)

    def has_password(self, plaintext):
        return bcrypt.verify(plaintext, self._password)


class Trip(db.Model, BaseMixin):
    __tablename__ = 'trips'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True, nullable=False)
    type = db.Column(db.String(64), nullable=False)
    departure_country = db.Column(db.String(64), nullable=False)
    departure_port = db.Column(db.String(64), nullable=False)
    arrival_country = db.Column(db.String(64), nullable=False)
    arrival_port = db.Column(db.String(64), nullable=False)
    planned_time = db.Column(db.String(64), nullable=False)
    estimated_arrival_time = db.Column(db.String(64), nullable=False)
    estimated_at_real_time = db.Column(db.String(64), nullable=False)
    consignor = db.Column(db.String(64), nullable=False)
    consignee = db.Column(db.String(64), nullable=False)
    cargo = db.Column(db.String(64), nullable=False)
    cargo_weight = db.Column(db.String(64), nullable=False)
    total_cargo_weight = db.Column(db.String(64), nullable=False)
    status = db.Column(db.String(64), nullable=False)
    tr_ex = db.Column(db.String(64), nullable=False)
    custom_reference = db.Column(db.String(64), nullable=False)
    container_nr = db.Column(db.String(64), nullable=False)
    container_type = db.Column(db.String(64), nullable=False)
    car_type = db.Column(db.String(64), nullable=False)
    car_model = db.Column(db.String(64), nullable=False)
    number_plate = db.Column(db.String(64), nullable=False)
    trailer_plate = db.Column(db.String(64), nullable=False)
    carrier = db.Column(db.String(64), nullable=False)


class RevokedToken(db.Model, BaseMixin):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120), nullable=False)
    expires = db.Column(db.BigInteger, nullable=False)

    @classmethod
    def new(cls, raw_token):
        return cls(jti=raw_token['jti'], expires=(raw_token['exp'] + 1))

    @classmethod
    def is_blacklisted(cls, token):
        return cls.first(jti=token) is not None

    @classmethod
    def remove_expired_tokens(cls):
        cls.query.filter(cls.expires <= datetime.now().timestamp()).delete()
