import psycopg2.extras
from database_handle import conn

with conn:

    def fetch_hug_recipants():
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("Select name from hugs")
            data = cursor.fetchall()
        return data


    def check_for_hug_recipiant(person):

        with conn.cursor() as cursor:
            sql = "SELECT name FROM hugs WHERE name LIKE %s"
            cursor.execute(sql, (person,))
            data = cursor.fetchone()
            if not data:
                return False    
            return True


    def increment_hug(person):
        with conn.cursor() as cursor:
            sql = "UPDATE hugs SET amount = amount + 1 WHERE name LIKE %s"
            cursor.execute(sql, (person,))
            conn.commit()
        return


    def fetch_hugs(person = None):
        
        if person:
           with conn.cursor() as cursor:
            sql = "Select amount from hugs WHERE name LIKE %s"
            cursor.execute(sql, (person,))
            data = cursor.fetchone()
            return data
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(
                f"Select * from hugs")
            data = cursor.fetchall()
            return data

    def add_hug_recipiant(person):
        with conn.cursor() as cursor:
            sql = "INSERT INTO hugs (name) VALUES (%s)"
            cursor.execute(sql, (person,))
            conn.commit()
        return
