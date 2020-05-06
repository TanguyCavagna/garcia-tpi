from Blueprint import Blueprint
from Schema import Schema
from Migration import Migration

class TestTable(Migration):
    
    def __init__(self):
        pass

    def setup():
        return Schema().create('test_table', [
            Blueprint().id('id'),
            {**Blueprint().string('test'), **Blueprint().default('Salut')},
            {**Blueprint().foreign('id_other'), **Blueprint().references('id'), **Blueprint().on('other_table')}
        ], 2)