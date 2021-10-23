import psycopg2.extras
from database_handle import conn


with conn:

    def check(category_name):

        with conn.cursor() as cursor:
            sql = "Select id from categories where name LIKE %s"
            cursor.execute(sql, (category_name,))
            data = cursor.fetchone()
            if data:
                return data
            return False

    def add(category_name,server_id):
        with conn.cursor() as cursor:
            sql = "INSERT INTO categories(name,server_id) VALUES(%s,%s)"
            cursor.execute(sql, (category_name, server_id))
            conn.commit()
