"""Contient le model d'un user

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-05
"""
from flask_login import UserMixin

class User(UserMixin):
    """Héritage pour pouvoir utiliser cette classe comme current_user du flask_login
    """

    def __init__(self, id, last_name, first_name, email, phone, role):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone = phone
        self.role = role

    def serialize(self):
        return {
            'id': self.id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'email': self.email,
            'phone': self.phone
        }