# Written by: Sepehr Bazyar
from psycopg2 import connect
from psycopg2._psycopg import connection, cursor

from abc import ABC, abstractmethod
from typing import Any, List

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
            logging.info(f"{__name__}: Connection Succeeded.")
        except:
            logging.error(f"{__name__}: Connection Failed.")

    def __call__(self, table_name: str, **kwargs) -> None:
        SQL = f"""
CREATE TABLE {table_name} (
    {','.join([k + ' ' + v for k, v in kwargs])}
);
"""
        self.cursor.execute(SQL)
        logging.info(f"{__name__}: Create Table Succeeded.")

    def create(self, table_name: str, *args: List[str]) -> None:
        SQL = f"""
INSERT INTO {table_name}
VALUES ({','.join(args)} );
"""
        self.cursor.execute(SQL)
        self.conn.commit()
        logging.info(f"{__name__}: Create Row Succeeded.")

    def read(self, table_name: str, *args: List[str]) -> tuple:
        SQL = f"""
SELECT {','.join(args) or '*'}
FROM {table_name};
"""
        self.cursor.execute(SQL)
        logging.info(f"{__name__}: Read Table Succeeded.")
        return self.cursor.fetchall()

    def update(self, table_name: str, column: str, value: Any, **kwargs):
        SQL = f"""
UPDATE {table_name}
SET {','.join([k + ' = ' + v for k, v in kwargs])}
WHERE {column} = {value};
"""
        self.cursor.execute(SQL)
        self.conn.commit()
        logging.info(f"{__name__}: Update Row Succeeded.")

    def delete(self):
        pass

    def __del__(self):
        self.conn.close()
        logging.warning(f"{__name__}: Data Base Closed.")
