import psycopg2
import psycopg2.extras
from config import config



DB_HOST = config.DB_HOST
DB_NAME = config.DB_NAME
DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASS

conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD, host = DB_HOST)

with conn:
    
    def fetch_servers():
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("Select * from servers")
            data = cursor.fetchall()
        return data


    def fetch_hug_recipants():
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("Select name from hugs")
            data = cursor.fetchall()
        return data


    def check_for_hug_recipiant(person):

        with conn.cursor() as cursor:
            cursor.execute(f"SELECT name FROM hugs WHERE name LIKE '{person}'", )
            data = cursor.fetchone()
            if not data:
                return False    
            return True


    def increment_hug(person):
        with conn.cursor() as cursor:
            cursor.execute(
                f"UPDATE hugs SET amount = amount + 1 WHERE name LIKE '{person}'")
            conn.commit()
        return


    def fetch_hugs(person = None):
        
        if person:
           with conn.cursor() as cursor:
            cursor.execute(
                f"Select amount from hugs WHERE name LIKE '{person}'")
            data = cursor.fetchone()
            return data
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(
                f"Select * from hugs")
            data = cursor.fetchall()
            return data

    def add_hug_recipiant(person):
        with conn.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO hugs (name) VALUES ('{person}')")
            conn.commit()
        return
