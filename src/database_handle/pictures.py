import psycopg2
import psycopg2.extras
from database_handle import conn




with conn:
    
    def check_for_hug_recipiant(person):

        with conn.cursor() as cursor:
            cursor.execute(
                f"SELECT name FROM hugs WHERE name LIKE '{person}'", )
            data = cursor.fetchone()
            if not data:
                return False
            return True
