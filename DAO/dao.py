import psycopg2
from config import DBconfig

class InfoDAO:
    def __init__(self):
        #connect to DB here

    def noFilter(self):
        cursor = self.conn.cursor()
        query = '''Select *
                From information;'''
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def filterByRace(self, aRace):
        cursor = self.conn.cursor()
        query = '''Select *
                From information
                Where race = %s;'''
        cursor.execute(query,(aRace,))
        result = cursor.fetchone()
        return result
    
    def filterByAge(self, minAge, maxAge):
        cursor = self.conn.cursor()
        query = '''Select *
                From information
                WHERE age BETWEEN %s and %s;'''
        cursor.execute(query,(minAge, maxAge,))
        result = cursor.fetchone()
        return result

    def filterByPopulation(self, minPop, maxPop):
        cursor = self.conn.cursor()
        query = '''Select *
                From information
                WHERE population BETWEEN %s and %s;'''
        cursor.execute(query,(minPop, maxPop,))
        result = cursor.fetchone()
        return result

    def filterByIncome(self,minIncome, maxIncome):
        cursor = self.conn.cursor()
        query = '''Select *
                From information
                WHERE income BETWEEN %s and %s;'''
        cursor.execute(query,(minIncome, maxIncome,))
        result = cursor.fetchone()
        return result

    def filterByR_A(self, aRace, minAge,maxAge):
        cursor = self.conn.cursor()
        query = '''Select *
                From information
                WHERE race = %s
                AND age BETWEEN %s and %s;'''
        cursor.execute(query,(aRace, minAge, maxAge,))
        result = cursor.fetchone()
        return result

    def filterByR_P(self, aRace, minPop, maxPop):
        cursor = self.conn.cursor()
        query = '''Select *
                From information
                WHERE race = %s
                AND population BETWEEN %s and %s;'''
        cursor.execute(query,(aRace, minPop, maxPop,))
        result = cursor.fetchone()
        return result

    def filterByR_I(self, aRace, minInc,maxInc):
        cursor = self.conn.cursor()
        query = '''Select *
                From information
                WHERE race = %s
                AND income BETWEEN %s and %s;'''
        cursor.execute(query,(aRace, minInc, maxInc,))
        result = cursor.fetchone()
        return result
    
    def filterByA_Pop(minAge,maxAge,minPop,maxPop):
        cursor = self.conn.cursor()
        query = '''Select *
                From information
                WHERE age BETWEEN %s and %s
                AND population BETWEEN %s and %s;'''
        cursor.execute(query,(minAge,maxAge,minPop,maxPop,))
        result = cursor.fetchone()
        return result

        def filterByA_Income(minAge,maxAge,minInc,maxInc):
            cursor = self.conn.cursor()
            query = '''Select *
                    From information
                    WHERE age BETWEEN %s and %s
                    AND income BETWEEN %s and %s;'''
            cursor.execute(query,(minAge,maxAge,minInc,maxInc,))
            result = cursor.fetchone()
            return result

        def filterByP_Income(minPop,maxPop,minInc,maxInc):
            cursor = self.conn.cursor()
            query = '''Select *
                    From information
                    WHERE population BETWEEN %s and %s
                    AND income BETWEEN %s and %s;'''
            cursor.execute(query,(minPop,maxPop,minInc,maxInc,))
            result = cursor.fetchone()
            return result
        
        def filterByA_Population(minAge,maxAge,minPop,maxPop):
            cursor = self.conn.cursor()
            query = '''Select *
                    From information
                    WHERE age BETWEEN %s and %s
                    AND population BETWEEN %s and %s;'''
            cursor.execute(query,(minAge,maxAge,minPop,maxPop,))
            result = cursor.fetchone()
            return result

        def filterByA_Pop_Inc(minAge,maxAge,minPop,maxPop,minInc,maxInc):
            cursor = self.conn.cursor()
            query = '''Select *
                    From information
                    WHERE age BETWEEN %s and %s
                    AND population BETWEEN %s and %s
                    AND income BETWEEN %s and %s;'''
            cursor.execute(query,(minAge,maxAge,minPop,maxPop,minInc,maxInc,))
            result = cursor.fetchone()
            return result

        def filterByR_A_Pop_Inc(aRace,minAge,maxAge,minPop,maxPop,minInc,maxInc):
            cursor = self.conn.cursor()
            query = '''Select *
                    From information
                    WHERE race = %s
                    AND age BETWEEN %s and %s
                    AND population BETWEEN %s and %s
                    AND income BETWEEN %s and %s;'''
            cursor.execute(query,(aRace,minAge,maxAge,minPop,maxPop,minInc,maxInc,))
            result = cursor.fetchone()
            return result