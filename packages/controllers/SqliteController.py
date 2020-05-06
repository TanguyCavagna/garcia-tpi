"""Contient la classe de contrôle de la base de données Sqlite

@author: Tanguy Cavagna
@copyright: Copyright 2020, TPI
@version: 1.1.0
@date: 2020-05-05
"""
import sqlite3, pathlib, sys, os, itertools
from datetime import datetime
from os import path, getcwd
from glob import glob
from importlib import import_module

class SqliteController:

    FETCH_ALL = 0
    FETCH_ONE = 1
    NO_FETCH = 2

    connection = None

    def __init__(self):
        pass

    def __get_cursor(self) -> object:
        return self.get_instance().cursor()

    def __dict_factory(self, cursor, row):
        """Used to return fetch as dict
            see: https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query

            Arguments:
                cursor {object} -- Cursor of the connection
                row {object} -- Returned rows

            Returns:
                dict -- Full dict
        """
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_instance(self) -> object:
        if self.connection is None:
            self.connection = sqlite3.connect("/home/cavagnat/Documents/programmation/python/garcia-tpi/static/database/garcia.db", detect_types=sqlite3.PARSE_DECLTYPES)
            self.connection.row_factory = self.__dict_factory

        return self.connection

    def execute_many(self, query, values) -> None:
        cursor = self.__get_cursor()

        cursor.executemany(query, values)

        self.get_instance().commit()

    def execute(self, query, values = None, fetch_mode = 2):
        """Exécute une requete en base

            Arguments:
                query {str} -- Requete à executer

            Keyword Arguments:
                values {tuple} -- Valeurs à utilisé (default: {None})
                fetch_mode {int} -- Type de fetch voulu (default: {2}) -> pas de fetch

            Returns:
                None|[]|int -- Si pas de fetch, retourne le last_row_id, sinon retourne le fetch voulu
        """
        cursor = self.__get_cursor()

        if values is not None:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        last_row_id = cursor.lastrowid

        self.get_instance().commit()

        if fetch_mode == self.FETCH_ONE:
            result = cursor.fetchone()
        elif fetch_mode == self.FETCH_ALL:
            result = cursor.fetchall()
        else:
            result = None

        if (fetch_mode == self.NO_FETCH):
            return last_row_id
        else:
            return result

    def __get_eloquents(self):
        eloquents = []

        sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../migrations"))
        for file in glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../migrations/*Table.py")):
            name = os.path.splitext(os.path.basename(file))[0]
            eloquents.append(getattr(import_module(name), name))

        return eloquents

    def migrate(self):
        """Migre les tables
        """
        queries = []

        for module in self.__get_eloquents():
            queries.append(module.setup())

        for query in sorted(queries, key=lambda k: k['pos']):
            self.execute(query['query'])
        
        return True

    def seed(self):
        """Seed les tables
        """
        queries = []

        for module in self.__get_eloquents():
            queries.append(module.seed())

        for query in queries:
            if query is not None:
                self.execute(query['query'])
        
        return True
        