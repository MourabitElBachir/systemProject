import sqlite3
import pandas as pd

class Database:

    def __init__(self, database, table):
        self.database = database
        self.table = table
        self.connection = sqlite3.connect(database)

    def select(self, table):
        self.connection.execute(f"SELECT * FROM {table}")

    #def insert(self, dictionnaire):
        #if type(dictionnaire) is dict:


