import psycopg2.extras
from database_handle import conn


with conn:

    def check_server(server_id):

        with conn.cursor() as cursor:
            sql = "Select id from guilds where server_id LIKE %s"
            cursor.execute(sql, (server_id,))
            data = cursor.fetchone()
            if data:
                return data
            return False

    def add(server_id):
        with conn.cursor() as cursor:
            sql = "INSERT INTO guilds(server_id) VALUES(%s)"
            cursor.execute(sql, (server_id,))
        