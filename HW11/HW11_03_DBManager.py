# Written by: Sepehr Bazyar
from psycopg2 import connect
from psycopg2._psycopg import connection, cursor

from abc import ABC, abstractmethod

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)-10s - %(message)s')


class BaseManager(ABC):
    @abstractmethod
    def create(self): pass

    @abstractmethod
    def read(self): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def delete(self): pass


class DatabaseManager(BaseManager):
    def __init__(self, database: str, user: str, password: str, host: str, port: str) -> None:
        try:
            self.conn: connection = connect(
                database=database, user=user, password=password, host=host, port=port)
            self.cursor: cursor = self.conn.cursor
            self.tables = {}
            logging.info(f"{__name__}: Connection Succeeded.")
        except:
            logging.error(f"{__name__}: Connection Failed.")

    def __call__(self, table_name: str, **kwargs):
        self.tables[table_name] = kwargs
        SQL = f"""
CREATE TABLE {table_name} (
    {','.join([k + ' ' + v for k, v in kwargs])}
);
"""
        self.cursor.execute(SQL)
        logging.info(f"{__name__}: Create Table Succeeded.")

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def __del__(self):
        self.conn.close()
        logging.warning(f"{__name__}: Data Base Closed.")
