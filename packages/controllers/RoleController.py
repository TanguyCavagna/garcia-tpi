"""Contient la classe de contrôle des roles

Les roles sont : User, Admin

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.0.0
@date: 2020-05-05
"""
from .SqliteController import SqliteController
from ..models.Role import Role

class RoleController:

    def __init__(self):
        pass
    
    def get_all(self) -> [Role]:
        """Get all the types
        
            Returns:
                [Role] -- List of roles object
        """
        rows = SqliteController().execute("SELECT `idRole`, `nameRole` FROM `role`", fetch_mode=SqliteController().FETCH_ALL)
        roles = [Role(r['idRole'], r['nameRole']) for r in rows]

        return roles

    def get_all_as_dict(self) -> dict:
        """Get all the types as a dictionary
        
            Returns:
                dict -- Dictionary that contains all the types as "name": id
        """
        roles = {}
        for r in self.get_all():
            roles.update({r.name: r.id})

        return roles

    def get_default(self) -> Role:
        """Récupère le role par défaut

            Returns:
                Role -- Role par défaut
        """
        try:
            sql_get_default = "SELECT `idRole`, `nameRole` FROM `role` WHERE `nameRole` LIKE 'User'"
            row = SqliteController().execute(sql_get_default, fetch_mode=SqliteController().FETCH_ONE)

            if row is not None:
                return Role(row['idRole'], row['nameRole'])
            else:
                return row
        except Exception as e:
            raise e

    def get_by_id(self, id: int) -> Role:
        """Récupère le role par l'id

            Returns:
                Role -- Role trouvé
        """
        try:
            sql_get_default = "SELECT `idRole`, `nameRole` FROM `role` WHERE `idRole` = ?"
            row = SqliteController().execute(sql_get_default, values=(id,), fetch_mode=SqliteController().FETCH_ONE)

            if row is not None:
                return Role(row['idRole'], row['nameRole'])
            else:
                return row
        except Exception as e:
            raise e
