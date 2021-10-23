from database_handle import conn


with conn:

    def check(roles_name):

        with conn.cursor() as cursor:
            sql = "Select * from roles where name LIKE %s"
            cursor.execute(sql, (roles_name,))
            data = cursor.fetchone()
            if data:
                return data
            return False

    def add(role_name, emote, category_id):
        with conn.cursor() as cursor:
            sql = "INSERT INTO roles(name,emote,category) VALUES(%s,%s,%s)"
            cursor.execute(sql, (role_name, emote, int(category_id)))
            conn.commit()
