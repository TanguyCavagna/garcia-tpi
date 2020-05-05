"""Contient la classe de contrôle des utilisateurs

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-05
"""
from .SqliteController import SqliteController
from .RoleController import RoleController
from ..models.User import User

class UserController:

    def __init__(self):
        pass
        
    #email: str, password: str, last_name: str, first_name: str, phone: str
    def insert(self) -> bool:
        pass