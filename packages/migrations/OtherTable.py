from Blueprint import Blueprint
from Schema import Schema
from Migration import Migration

class OtherTable(Migration):
    
    def __init__(self):
        pass

    def setup():
        return Schema().create('other_table', [
            Blueprint().id('id'),
            Blueprint().string('column')
        ], 1)