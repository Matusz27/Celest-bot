import psycopg2.extras
from database_handle import conn


with conn:

    def check(category_name):

        with conn.cursor() as cursor:
            sql = "Select * from catogries where name LIKE %s"
            cursor.execute(sql, (category_name,))
            data = cursor.fetchone()
            if data:
                return data
            return False

    def add(category_name):
        with conn.cursor() as cursor:
            sql = "INSERT INTO catogries(name) VALUES(%s)"
            cursor.execute(sql, (category_name,))
