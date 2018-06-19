import psycopg2
from config import DBconfig

class InfoDAO:
    def __init__(self):
        #connect to DB here

    def filterByRace(self, aRace):
        cursor = self.conn.cursor()
        query = '''Select *
                From information
                Where race = %s;'''
        cursor.execute(query,(aRace,))
        result = cursor.fetchone()
        return result