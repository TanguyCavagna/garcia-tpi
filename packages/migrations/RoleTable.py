from Blueprint import Blueprint
from Schema import Schema
from Migration import Migration

class RoleTable(Migration):
    
    def __init__(self):
        pass

    def setup():
        return Schema().create('role', [
            Blueprint().id('idRole'),
            {**Blueprint().string('nameRole'), **Blueprint().nullable(False)}
        ], 1)

    def seed():
        return Schema().insert('role', [
            {
                'idRole': 1,
                'nameRole': 'User'
            },
            {
                'idRole': 2,
                'nameRole': 'Admin'
            }
        ])