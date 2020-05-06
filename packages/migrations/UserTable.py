from Blueprint import Blueprint
from Schema import Schema
from Migration import Migration

class UserTable(Migration):
    
    def __init__(self):
        pass

    def setup():
        return Schema().create('user', [
            Blueprint().id('idUser'),
            {**Blueprint().string('lastnameUser'), **Blueprint().nullable(False)},
            {**Blueprint().string('firstnameUser'), **Blueprint().nullable(False)},
            {**Blueprint().string('emailUser'), **Blueprint().nullable(False)},
            {**Blueprint().string('passwordUser'), **Blueprint().nullable(False)},
            {**Blueprint().string('phoneUser'), **Blueprint().nullable(False)},
            {**Blueprint().string('lastConnectDate'), **Blueprint().nullable(True)},
            {**Blueprint().foreign('idRole'), **Blueprint().references('idRole'), **Blueprint().on('role')}
        ], 1)