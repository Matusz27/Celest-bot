from database_handle import conn


with conn:

    def check(server_id):

        with conn.cursor() as cursor:
            sql = "Select id from guilds where server_id = %s"
            cursor.execute(sql, (int(server_id),))
            data = cursor.fetchone()
            if data:
                return data
            return False

    def add(server_id):
        with conn.cursor() as cursor:
            sql = "INSERT INTO guilds(server_id) VALUES(%s)"
            cursor.execute(sql, (int(server_id),))
            conn.commit()
        
