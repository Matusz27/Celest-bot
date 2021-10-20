import psycopg2.extras
from database_handle import conn


with conn:

    def fetch_servers():

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("Select * from servers")
            data = cursor.fetchall()
        return data
