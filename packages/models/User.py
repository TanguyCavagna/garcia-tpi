"""Contient le model d'un user

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-05
"""

class User:

    def __init__(self, id, last_name, first_name, email, phone):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone = phone

    def serialize(self):
        return {
            'id': self.id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'email': self.email,
            'phone': self.phone
        }