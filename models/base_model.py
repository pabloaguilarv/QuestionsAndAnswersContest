import sqlite3 as sql

class BaseModel:
    def __init__(self, name):
        self._connection = sql.connect(name)
        self._cursor = self._connection.cursor()


    def __enter__(self):
        return self
    

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._connection.close()


    @property
    def connection(self):
        return self._connection


    @property
    def cursor(self):
        return self._cursor


    def execute(self, sql, params=None):
        self._cursor.execute(sql,params or ())
    

    def executescript(self,sql,params=None):
        self._cursor.executescript(sql, params or ())
    

    def fetchOne(self):
        return self._cursor.fetchone()
    

    def fetchAll(self):
        return self._cursor.fetchall()


    def commit(self):
        self._connection.commit()
    
    
    def close(self, commit=True):
        if commit:
            self._connection.commit()
        self._connection.close()