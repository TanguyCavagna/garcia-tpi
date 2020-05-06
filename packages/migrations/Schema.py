from Blueprint import Blueprint

class Schema:

    def __init__(self):
        pass

    def create(self, table_name, blueprints, position=None):
        create_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ("

        for bp in blueprints:
            if bp.get('column') is not None:
                create_query += f"`{bp.get('column')}` "
            else:
                create_query += f"`{bp.get('foreign')}` "

            if bp.get('foreign') is None:
                create_query += bp.get('type') + " "
            else:
                create_query += 'integer '

            if bp.get('nullable') is not None and bp.get('nullable') == False:
                create_query += 'NOT NULL '
            else:
                create_query += 'NULL '

            if bp.get('primary_key') is not None and bp.get('primary_key') == True:
                create_query += 'PRIMARY KEY '

            if bp.get('default') is not None:
                create_query += f'DEFAULT \'{bp.get("default")}\' '

            if bp.get('foreign') is not None:
                create_query += f'REFERENCES `{bp.get("on")}`(`{bp.get("references")}`) '

            create_query += ','

        create_query = create_query[:-1] + ")"

        return { 'pos': position, 'query': create_query }

    def insert(self, table_name, entries):
        insert_query = f"INSERT INTO {table_name}("

        for entry in entries:
            for key, _ in entry.items():
                insert_query += f'`{key}`,'
            break

        insert_query = insert_query[:-1] + ') VALUES'

        for entry in entries:
            insert_query += '('
            for _, value in entry.items():
                insert_query += f"'{value}',"
            insert_query = insert_query[:-1] + '),'

        return { 'query': insert_query[:-1] }
