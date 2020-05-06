class Blueprint:

    def __init__(self):
        pass

    def increments(self):
        return { 'auto_increment': True }

    def nullable(self, state=False):
        return { 'nullable': state }

    def primary_key(self):
        return { 'primary_key': True }

    def default(self, value):
        return { 'default': value }

    def integer(self, column_name):
        return {
            'type': 'integer',
            'column': column_name
        }

    def string(self, column_name):
        return {
            'type': 'text',
            'column': column_name
        }

    def timestamp(self, column_name):
        return {
            'type': 'timestamp',
            'column': column_name
        }

    def foreign(self, column_name):
        return { 'foreign': column_name, **self.nullable(False) }

    def references(self, references_column):
        return { 'references': references_column }

    def on(self, referenced_table):
        return { 'on': referenced_table }

    def id(self, column_name):
        return {**self.integer(column_name), **self.increments(), **self.nullable(), **self.primary_key()}